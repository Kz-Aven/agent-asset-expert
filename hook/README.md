# Hook Collector

Each platform Adapter writes a generated hook descriptor to the local data root. A Hook Collector is observational only: it must never change the host Agent's allow/deny decision or final result. Hook-derived records are always tagged `coverage=partial` unless the Adapter has verified full runtime coverage.

WorkBuddy uses the CodeBuddy-compatible JSON stdin Hook contract. Its settings are at `~/.workbuddy/settings.json`; the installer appends an owned `agent-asset-expert hook --platform workbuddy` command to the five lifecycle events and removes only that command on uninstall.
