from __future__ import annotations

from agent_asset_expert.mcp_server import ReadonlyTools
from agent_asset_expert.adapters.tigerose_runtime import TigeroseRuntimeBridge
from agent_asset_expert.cli import _install_codex_hooks, _install_tigerose_mcp, _install_workbuddy_hooks, _install_workbuddy_mcp, _uninstall_codex_hooks, _uninstall_tigerose_mcp, _uninstall_workbuddy_hooks, _uninstall_workbuddy_mcp
from agent_asset_expert.hook_lifecycle import HookLifecycleCollector
from agent_asset_expert.recorder import ObservationRecorder
from agent_asset_expert.storage import AssetStore


def test_redacts_and_routes_identical_content_per_assistant(tmp_path):
    store = AssetStore(tmp_path)
    first = store.record_execution(platform="tigerose", assistant_id="a", assistant_name="甲", source_execution_id="one", session_id="s", user_input={"token": "secret", "prompt": "same"}, output="same")
    second = store.record_execution(platform="codex", assistant_id="a", assistant_name="乙", source_execution_id="two", session_id="s", user_input={"token": "secret", "prompt": "same"}, output="same")
    first_row = ReadonlyTools(store).execution({"execution_id": first})["execution"]
    second_row = ReadonlyTools(store).execution({"execution_id": second})["execution"]
    assert first_row["input_content_ref"] != second_row["input_content_ref"]
    assert "secret" not in store.read_content(first_row["input_content_ref"])
    assert "[REDACTED]" in store.read_content(first_row["input_content_ref"])


def test_latest_execution_resolves_human_name_and_sql_is_readonly(tmp_path):
    store = AssetStore(tmp_path)
    store.record_execution(platform="tigerose", assistant_id="demo", assistant_name="数据分析阿喵", source_execution_id="one", session_id="s", user_input="hello", output="done")
    tools = ReadonlyTools(store)
    latest = tools.latest({"assistant_name": "数据分析阿喵"})
    assert latest["execution"]["status"] == "completed"
    assert tools.sql({"assistant_key": "tigerose--demo", "sql": "SELECT execution_id FROM execution", "parameters": {}})
    try:
        tools.sql({"assistant_key": "tigerose--demo", "sql": "DELETE FROM execution", "parameters": {}})
    except ValueError as exc:
        assert "read-only" in str(exc)
    else:
        raise AssertionError("write SQL was accepted")


def test_feedback_snapshot_and_strict_eval_candidates(tmp_path):
    store = AssetStore(tmp_path)
    execution_id = store.record_execution(platform="tigerose", assistant_id="demo", assistant_name="数据分析阿喵", source_execution_id="failed", session_id="s", user_input="hello", output="failed", status="failed")
    store.snapshot(execution_id, "agent", "demo", {"prompt": "v1"}, "primary_agent")
    store.feedback(execution_id, "rejected", "answer was incomplete", "revised answer")
    candidates = ReadonlyTools(store).eval_candidates({"strict_only": True})
    assert candidates == [{"execution_id": execution_id, "assistant_name": "数据分析阿喵", "source_platform": "tigerose", "status": "failed", "coverage": "full", "trace_integrity": "complete", "reason_code": "failure"}]


def test_tigerose_bridge_records_full_trace_and_snapshot(tmp_path):
    store = AssetStore(tmp_path)
    bridge = TigeroseRuntimeBridge(ObservationRecorder(store))
    bridge.start("run-1", "assistant", "开发专家阿兔", "session", "build it", [{"asset_type": "agent", "asset_id": "assistant", "value": {"prompt": "v1"}, "purpose": "primary_agent"}])
    bridge.llm_finished("run-1", "llm-1", "model", {"messages": []}, "plan")
    bridge.tool_finished("run-1", "tool-1", "bash", {"cmd": "pytest"}, "ok")
    execution_id = bridge.finish("run-1", "done", "completed", "completed")
    execution = ReadonlyTools(store).execution({"execution_id": execution_id})["execution"]
    assert execution["coverage"] == "full"
    assert len(ReadonlyTools(store).trace({"execution_id": execution_id})) == 2
    key, conn = store.locate_execution(execution_id)
    with conn:
        assert conn.execute("SELECT COUNT(*) FROM execution_config_ref WHERE execution_id=?", (execution_id,)).fetchone()[0] == 1


def test_workbuddy_hook_lifecycle_and_owned_settings_entries(tmp_path, monkeypatch):
    monkeypatch.setenv("AGENT_ASSET_EXPERT_HOME", str(tmp_path / "assets"))
    settings = tmp_path / "settings.json"
    settings.write_text('{"hooks":{"Stop":[{"hooks":[{"type":"command","command":"existing"}]}]}}', encoding="utf-8")
    _install_workbuddy_hooks(settings)
    _install_workbuddy_hooks(settings)
    value = __import__("json").loads(settings.read_text(encoding="utf-8"))
    commands = [child.get("command") for matcher in value["hooks"]["Stop"] for child in matcher["hooks"]]
    assert sum(command.endswith("agent-asset-expert hook --platform workbuddy") for command in commands) == 1
    collector = HookLifecycleCollector(ObservationRecorder(AssetStore(tmp_path / "assets")))
    collector.ingest({"hook_event_name": "UserPromptSubmit", "source_platform": "workbuddy", "session_id": "s", "turn_id": "t", "workspace": "/project", "prompt": "hello"})
    collector.ingest({"hook_event_name": "PostToolUse", "source_platform": "workbuddy", "session_id": "s", "turn_id": "t", "tool_name": "bash", "tool_input": {"cmd": "pwd"}, "result_summary": "ok"})
    execution_id = collector.ingest({"hook_event_name": "Stop", "source_platform": "workbuddy", "session_id": "s", "turn_id": "t"})
    execution = ReadonlyTools(AssetStore(tmp_path / "assets")).execution({"execution_id": execution_id})["execution"]
    assert execution["coverage"] == "partial"
    assert len(ReadonlyTools(AssetStore(tmp_path / "assets")).trace({"execution_id": execution_id})) == 1
    _uninstall_workbuddy_hooks(settings)
    value = __import__("json").loads(settings.read_text(encoding="utf-8"))
    assert value["hooks"]["Stop"] == [{"hooks": [{"type": "command", "command": "existing"}]}]


def test_workbuddy_mcp_is_owned_and_restored(tmp_path, monkeypatch):
    monkeypatch.setenv("AGENT_ASSET_EXPERT_HOME", str(tmp_path / "assets"))
    path = tmp_path / "mcp.json"
    path.write_text('{"mcpServers":{"other":{"command":"other"}}}', encoding="utf-8")
    owned = _install_workbuddy_mcp(path)
    value = __import__("json").loads(path.read_text(encoding="utf-8"))
    assert value["mcpServers"]["agent_asset_expert"]["args"] == ["mcp"]
    _uninstall_workbuddy_mcp(path, __import__("pathlib").Path(owned["backup"]))
    value = __import__("json").loads(path.read_text(encoding="utf-8"))
    assert "agent_asset_expert" not in value["mcpServers"]


def test_collector_accepts_pretty_printed_hook_json(monkeypatch):
    import io
    from agent_asset_expert import collector

    received = []
    monkeypatch.setattr(collector, "ingest", lambda value: received.append(value))
    monkeypatch.setattr(collector.sys, "stdin", io.StringIO('{\n  "hook_event_name": "Stop"\n}\n'))
    collector.main()
    assert received == [{"hook_event_name": "Stop"}]


def test_codex_hook_entries_are_owned_and_removed(tmp_path, monkeypatch):
    monkeypatch.setenv("AGENT_ASSET_EXPERT_HOME", str(tmp_path / "assets"))
    path = tmp_path / "hooks.json"
    path.write_text('{"hooks":{"UserPromptSubmit":[{"hooks":[{"type":"command","command":"existing"}]}],"Stop":[]}}', encoding="utf-8")
    _install_codex_hooks(path)
    _install_codex_hooks(path)
    value = __import__("json").loads(path.read_text(encoding="utf-8"))
    assert sum(child.get("command") == "agent-asset-expert hook --platform codex" for matcher in value["hooks"]["UserPromptSubmit"] for child in matcher["hooks"]) == 1
    _uninstall_codex_hooks(path)
    value = __import__("json").loads(path.read_text(encoding="utf-8"))
    assert value["hooks"]["UserPromptSubmit"] == [{"hooks": [{"type": "command", "command": "existing"}]}]


def test_tigerose_mcp_entry_is_restored_without_replacing_other_servers(tmp_path, monkeypatch):
    monkeypatch.setenv("AGENT_ASSET_EXPERT_HOME", str(tmp_path / "assets"))
    path = tmp_path / "mcp.json"
    path.write_text('{"servers":{"agent_assets":{"command":"python","args":["-m","old"]},"other":{"command":"other"}}}', encoding="utf-8")
    owned = _install_tigerose_mcp(path)
    current = __import__("json").loads(path.read_text(encoding="utf-8"))
    assert current["servers"]["agent_assets"]["command"] == "agent-asset-expert"
    current["servers"]["other"]["description"] = "user change"
    path.write_text(__import__("json").dumps(current), encoding="utf-8")
    _uninstall_tigerose_mcp(path, __import__("pathlib").Path(owned["backup"]))
    restored = __import__("json").loads(path.read_text(encoding="utf-8"))
    assert restored["servers"]["agent_assets"]["command"] == "python"
    assert restored["servers"]["other"]["description"] == "user change"
