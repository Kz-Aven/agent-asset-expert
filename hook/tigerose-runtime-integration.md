# Tigerose Runtime Integration

Import `TigeroseRuntimeBridge` into the local Tigerose runtime and use one process-level instance. It receives data only after the host runtime has made its own execution decision.

```python
from agent_asset_expert.adapters.tigerose_runtime import TigeroseRuntimeBridge

asset_bridge = TigeroseRuntimeBridge()

# After Tigerose has allocated run_id and resolved the assistant:
asset_bridge.start(run_id, assistant_id, assistant_name, session_id, user_input, snapshots)

# After each completion or tool result:
asset_bridge.llm_finished(run_id, call_id, model_id, request, response, usage, error)
asset_bridge.tool_finished(run_id, call_id, name, arguments, result, outcome)

# In the turn finally block:
asset_bridge.finish(run_id, final_output, status, termination)
```

The application must never let a bridge exception escape. Existing Tigerose `server.agent_assets` instrumentation can be migrated to this bridge one event at a time; runtime behavior and Hook allow/deny decisions stay unchanged.
