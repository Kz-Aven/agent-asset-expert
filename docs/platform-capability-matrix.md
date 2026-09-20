# Platform Capability Matrix

| Platform | Runtime Adapter | Hook Collector | MCP registration | Current coverage rule |
| --- | --- | --- | --- | --- |
| Tigerose | `TigeroseRuntimeBridge` | Yes | Tigerose MCP config | `full` only after bridge lifecycle calls are installed |
| Codex | Pending official local runtime extension | NDJSON Hook Collector | `~/.codex/config.toml` marker block | `partial` until an official runtime extension exposes model/tool internals |
| WorkBuddy | Bundled `@genie/agent-cli` has no safe public extension API | `~/.workbuddy/settings.json` command Hooks | Not yet exposed by the verified settings schema | `partial` until a verified extension exposes lifecycle events |

The installer must report observed capabilities rather than infer them from platform names. “Installed” and “full coverage” are separate states.
