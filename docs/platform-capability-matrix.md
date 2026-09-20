# Platform Capability Matrix

| Platform | Runtime Adapter | Hook Collector | MCP registration | Current coverage rule |
| --- | --- | --- | --- | --- |
| Tigerose | `TigeroseRuntimeBridge` | Yes | Tigerose MCP config | `full` only after bridge lifecycle calls are installed |
| Codex | Pending official local runtime extension | NDJSON Hook Collector | `~/.codex/config.toml` marker block | `partial` until an official runtime extension exposes model/tool internals |
| WorkBuddy | Bundled `@genie/agent-cli` has no safe public extension API | `~/.workbuddy/settings.json` command Hooks | `~/.workbuddy/mcp.json` | `partial`; prompt and tool fields are collected when supplied, while final reply, Token, and duration remain unavailable unless the Hook payload explicitly supplies them |

The installer must report observed capabilities rather than infer them from platform names. “Installed” and “full coverage” are separate states.
