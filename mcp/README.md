# MCP

Register the stdio server with a local Agent using:

```text
command = "agent-asset-expert"
args = ["mcp"]
```

The server has no write tools. Start with `list_assistants`, `get_latest_execution`, and `summarize_execution_metrics`; use `query_readonly_sql` only when a domain tool cannot answer the question.
