# Hook Collector

Each platform Adapter writes a generated hook descriptor to the local data root. A Hook Collector is observational only: it must never change the host Agent's allow/deny decision or final result. Hook-derived records are always tagged `coverage=partial` unless the Adapter has verified full runtime coverage.

WorkBuddy uses the CodeBuddy-compatible JSON stdin Hook contract. Its settings are at `~/.workbuddy/settings.json`; the installer resolves an absolute `agent-asset-expert` command before appending owned Hook entries to the five lifecycle events, and removes both legacy bare commands and current absolute commands on uninstall. The collector accepts both one complete JSON document and NDJSON.

WorkBuddy Hook payloads are partial observations. They reliably preserve user prompts and tool activity when present, but do not claim final replies, model tokens, or duration unless WorkBuddy explicitly provides those fields. Reading transcripts is deliberately not enabled until the transcript format and permitted paths are verified.
