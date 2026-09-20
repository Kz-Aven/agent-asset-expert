# Agent Asset Expert

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![Platform](https://img.shields.io/badge/platform-macOS-black.svg)](#支持的集成)

# README-zh

将本地 Agent 的每一次工作，沉淀为可查询、可理解、可评估的数据资产。

## 概述

随着 Agent 承担越来越多的实际工作，对话、工具调用、完成结果、失败记录与用户反馈都会成为重要的业务知识。**Agent Asset Expert** 把这些原本散落在单次会话和日志里的信息保存下来，转化为可持续复用的 Agent 数据资产。

它面向 macOS 本地 Agent 工作流设计，默认在本机存储数据，通过只读 MCP 服务提供访问，并采用 MIT 许可证发布。

> 它用于补充而非替代宿主 Agent 平台：既有会话、日志、权限和 Hook 仍由宿主平台控制；采集失败会与宿主 Agent 隔离。

## 您将获得什么

1. **将本地 Agent 的工作过程和结果沉淀为数据资产。** 保存完成状态、输入输出、工具活动、错误、重试、耗时和 Token 用量。
2. **安装 MCP 后，即可查询数据资产并评估 Agent 能力。** 分析 Agent 可以通过自然语言查询近期工作、查看处理过程、比较性能，并构建有证据支撑的评测集，无需您手动查找内部编号。

## 为什么使用它

- **让历史工作可复用：**将一次性的 Agent 工作转化为可检索记录，用于排障、分析与持续改进。
- **了解工作过程：**在一个地方查看结果、耗时、Token 消耗、错误、重试和可回看的处理步骤。
- **基于证据进行评估：**找出失败任务、人工修改的输出、负面反馈或成功基线，沉淀为可审阅的 Eval Case。
- **保持数据控制权：**数据默认留在您的 Mac 上；MCP 接口仅提供只读访问。
- **支持多个本地 Agent：**每个“平台 / 助理”组合拥有独立本地数据存储，同时可通过 MCP 进行受控的跨助理查询。

## 安装后，你真正拥有的是什么？

安装后，您不只是多了一份日志，而是为每一次委托给助理的工作建立了一份可回看的工作档案。无论任务来自 Tigerose、Codex、WorkBuddy，还是后续接入的本地助理，档案都留在同一台 Mac 上，并可以在一个查询入口中查看。

| 您能看到的内容 | 它回答的问题 | 可以怎样使用 |
| --- | --- | --- |
| **任务原文** | 用户当时希望助理完成什么？ | 找回需求、识别高频问题、整理真实用户意图。 |
| **助理最终回复** | 助理最终交付了什么？ | 审核质量、沉淀优秀范例、对比不同助理的回答风格。 |
| **完成过程** | 助理查了什么资料、使用了哪些能力、调用了哪些本地工具？ | 复盘失败、发现绕路、判断工具或技能是否真正带来价值。 |
| **时间与成本** | 任务完成了吗？花了多久？消耗了多少模型额度？ | 控制成本、定位慢任务、发现不稳定环节。 |
| **当时的工作环境** | 使用的是哪个助理版本、提示词、技能、工具和外部服务？ | 在升级后解释质量变化，并尽可能复现历史工作。 |
| **人工信号** | 用户是否接受、重试、拒绝或手动修改了结果？ | 找到真正有问题的回答，形成高价值改进样本。 |

不同平台开放的信息深度不同。能直接接入运行时的平台可提供完整的工作过程；只能通过 Hook 接入的平台会如实标明“过程信息有限”，不会把缺失的数据伪装成完整记录。

## 它能支持哪些研究

- **Agent 产品研究：**哪些用户问题最常见，哪些任务完成率低，用户在哪些环节频繁重试或改写结果。
- **能力与质量评测：**从真实工作中挑选失败案例、人工修订案例和优秀案例，建立贴近业务的测试集，而不是只依赖人为编造的问题。
- **成本与效率经营：**比较不同模型、提示词、技能组合和助理之间的耗时、模型额度与成功率，找出高成本低回报的路径。
- **工具和技能投资决策：**判断某个 MCP、技能或工具到底解决了哪些任务、是否减少失败、是否值得继续维护或采购。
- **可靠性与风险治理：**观察错误类型、失败频率、重复尝试和异常任务，优先修复对用户影响最大的薄弱点。
- **组织知识积累：**把优秀的处理方式、常见问题和改进后的答案保存在本地，逐渐形成属于团队自己的 Agent 工作方法库。

它的市场价值不在于“多采一些日志”，而在于让 Agent 从不可解释的黑盒工具，变成可度量、可比较、可改进、可证明业务价值的数字劳动力。对个人开发者，它提供了优化本地助理的证据；对团队和产品方，它提供了从真实使用到评测、迭代和 ROI 证明的连续数据基础。

## 快速开始

### AI-Agent 一键安装

复制下面的提示词，扔给你的本地助理，一键安装本项目

```text
请在我的 macOS 本机安装并验证 Agent Asset Expert。请直接完成以下工作，并在结束后用简洁清单报告每一步的结果、实际修改的配置文件和健康检查结果。

1. 检查 git、Python 3.11+ 和 pipx 是否可用；缺少 pipx 时，使用当前 Python 安装 pipx，并确保其命令目录在 PATH 中。
2. 克隆项目：如果 ~/agent-asset-expert 不存在，执行 git clone https://github.com/Kz-Aven/agent-asset-expert.git ~/agent-asset-expert；如果目录已存在，保留其中的用户改动，不要删除或重置。
3. 安装项目：进入 ~/agent-asset-expert。首次安装执行 pipx install .；此前已通过 pipx 安装时，执行 pipx install --force . 更新为当前本地项目。
4. 安装数据采集器和 MCP：执行 agent-asset-expert install --platform auto。自动检测 Tigerose、Codex、WorkBuddy；只修改本工具拥有的配置项，保留所有已有 MCP 和 Hook，必要时使用工具提供的备份能力。
5. 安装分析 Skill：将 ~/agent-asset-expert/skills/agent-asset-analysis 按当前本地 Agent 平台的标准方式安装为可用 Skill。若当前平台不支持安装本地 Skill，请明确说明，并保留原始 Skill 文件路径供用户手动使用。
6. 验证：执行 agent-asset-expert status 和 agent-asset-expert doctor。若 doctor 提示尚无数据，请说明需要运行一次真实任务才能完成数据采集验证。
7. 不要删除任何已有数据、配置、MCP、Hook 或 Skill；不要上传本机数据；不要修改项目以外的文件，除非完成安装所必需。
```



### 手动安装



克隆项目

```
git clone https://github.com/Kz-Aven/agent-asset-expert.git  && cd agent-asset-expert
```

安装项目

```bash
cd ~/agent-asset-expert
pipx install .
agent-asset-expert install --platform auto
agent-asset-expert doctor
```

将 MCP 服务添加到用于分析的 Agent：

```text
command = "agent-asset-expert"
args = ["mcp"]
```

可向分析 Agent 提问：

> 查询数据分析阿喵最近一次工作的状态、结束原因和 Token，不要让我提供 ID。

> 比较两个助理本周完整工作的完成率、平均 Token 和平均耗时。

> 找出最近 30 天失败且记录完整的工作，按错误码汇总。

## 系统会保存哪些信息

- **结果与性能：**状态、耗时、Token 指标、重试和错误。
- **工作上下文：**用户提出的问题、助理最终回复，以及可获得的中间过程和工具结果。
- **当时的能力配置：**本次工作所使用的 Agent、Skill、Tool、MCP 服务和 Prompt 快照的不可变引用。
- **大内容：**通过受控本地 `content_ref` 引用保存的大型输入或输出。

每条工作记录都有以下标签，帮助您判断它是否适合用于严谨复盘或制作评测集：

| 标签 | 含义 |
| --- | --- |
| `collection_mode` | 采集方式：`runtime_adapter`、`hook_collector` 或 `log_collector`。 |
| `coverage` | 平台提供的是完整还是部分工作过程。 |
| `trace_integrity` | 已采集到的工作过程是否已完整保存。 |

对于严谨复盘或制作评测集，请筛选：

```text
coverage=full
trace_integrity=complete
```

## 支持的集成

### Tigerose

```bash
agent-asset-expert install --platform tigerose
```

该命令会将 `~/Library/Application Support/Tigerose/mcp.json` 中已有的 `agent_assets` 注册项改为指向独立只读 MCP 服务。安装程序会备份原始服务条目，并在卸载时恢复。若 `TIGEROSE_ROOT` 指向本地源代码检出目录，可选的 `TigeroseRuntimeBridge` 可采集轮次、LLM、工具、配置和反馈生命周期数据，记录标记为 `coverage=full`。

### Codex

适配器会检测 `$CODEX_HOME/config.toml`（默认是 `~/.codex/config.toml`），并安装本地 Hook Collector 描述符。请使用快速开始中的命令注册 stdio MCP 服务。部分 Codex 模型内部信息无法通过 Hook 获取，因此记录会准确标记为 `coverage=partial`。

### WorkBuddy

```bash
agent-asset-expert install --platform workbuddy
```

该命令会在 `~/.workbuddy/settings.json` 的 `UserPromptSubmit`、`PostToolUse`、`Stop`、`Interrupt` 和 `SessionEnd` 中添加 Hook 命令。既有 Hook 不会被修改；卸载时仅移除由 Agent Asset Expert 新增的条目。WorkBuddy 当前通过安全的 Hook 方式采集，因此记录会标记为 `coverage=partial`，直到未来扩展 API 提供更完整的运行时访问。

检查安装状态：

```bash
agent-asset-expert status
agent-asset-expert doctor --platform PLATFORM
```

## MCP 能力

只读 MCP 服务提供：

- `list_assistants`
- `list_executions`
- `get_latest_execution`
- `get_execution`
- `get_execution_trace`
- `read_content`
- `summarize_execution_metrics`
- `list_eval_candidates`
- `query_readonly_sql`

优先使用专用工具。`query_readonly_sql` 是受限的兜底能力：可针对一个已注册助理数据库执行一条带参数的 `SELECT`，或 `CTE + SELECT` 查询。为确保安全，它会拒绝写入操作、模式变更、事务、`PRAGMA`、`ATTACH`、注释、多语句和 SQLite 专有函数。

## 数据存储与隐私

工作档案不会存储在此 Git 仓库中，默认保留在您的 Mac：

```text
~/Library/Application Support/AgentAssetExpert/data/
  registry.db
  assistants/{platform}--{assistant_id}.db
  assistants/{platform}--{assistant_id}/contents/sha256/{prefix}/{sha256}
```

每个“平台 / 助理”组合拥有独立数据库。`registry.db` 仅包含用于跨助理发现的受控定位信息和助理元数据，不包含 Prompt、输出或工具结果的正文。

在哈希或持久化之前，Agent Asset Expert 会对 API Key、Secret、Token、Cookie、Password、Authorization 和 Private Key 等凭据类信息脱敏。大型内容通过不透明的本地 `content_ref` 引用保存。

数据会一直保留在本地，直到您明确删除。初始版本依赖 macOS 当前用户目录权限，暂不提供应用层加密。除非您明确接受相关隐私影响，请勿将运行时数据目录放到同步目录或共享目录。

移除集成但保留已采集的工作档案：

```bash
agent-asset-expert uninstall --platform PLATFORM
```

# English

Turn every local Agent task into a data asset you can search, understand, and evaluate.

## Overview

As Agents take on real work, their conversations, tool activity, outcomes, failures, and user feedback become valuable operational knowledge. **Agent Asset Expert** preserves that knowledge instead of letting it disappear into isolated sessions and logs.

It is designed for local macOS Agent workflows. Data stays on your machine by default, is exposed through a read-only MCP server, and the project is released under the MIT License.

> It complements rather than replaces the host platform. Sessions, logs, permissions, and Hooks remain host-controlled; collection failures are isolated from the host Agent.

## What You Get

1. **Reusable records of local Agent work.** It preserves completion status, inputs and outputs, tool activity, errors, retries, duration, and token usage.
2. **Natural-language analysis through MCP.** An analysis Agent can find recent work, inspect the work history, compare performance, and build evidence-backed evaluation datasets without requiring internal IDs.

## Why Use It?

- **Reuse prior work:** turn one-off Agent tasks into searchable evidence for troubleshooting, analysis, and improvement.
- **Understand how work happened:** review outcomes, timing, tokens, errors, retries, and available work history in one place.
- **Evaluate with evidence:** identify failed tasks, edited outputs, negative feedback, and successful baselines as reviewable evaluation cases.
- **Keep control of your data:** data remains on your Mac and MCP access is read-only.
- **Work across local Agents:** each platform/assistant pair has a separate local store, with controlled cross-assistant discovery through MCP.

## What Do You Actually Get After Installation?

Each task delegated to an assistant becomes a reviewable work record. Whether it came from Tigerose, Codex, WorkBuddy, or a future local assistant, it stays on the same Mac and can be found from one query entry point.

| What you can see | Question it answers | How it helps |
| --- | --- | --- |
| **Original request** | What did the user ask the assistant to do? | Recover requirements and identify recurring needs. |
| **Final response** | What did the assistant deliver? | Review quality and preserve good examples. |
| **Work history** | What information, capabilities, and local tools did the assistant use? | Diagnose failures, identify detours, and judge tool value. |
| **Time and cost** | Was the task completed? How long did it take? How many model tokens did it use? | Control cost and locate slow or unstable work. |
| **Environment at the time** | Which assistant version, instructions, skills, tools, and services were in use? | Explain quality changes and recreate work when possible. |
| **Human signals** | Did the user accept, retry, reject, or edit the result? | Find responses that genuinely need improvement. |

Runtime integrations can provide fuller work histories. Hook-only integrations identify limited process information rather than pretending missing data exists.

## What Can You Learn From It?

- **Agent product research:** common user needs, weak task categories, and moments where people retry or rewrite results.
- **Capability and quality evaluation:** real failed, edited, and successful work as business-relevant test cases instead of only synthetic prompts.
- **Cost and efficiency management:** compare model, prompt, skill, and assistant combinations by time, token use, and completion rate.
- **Tool and skill investment decisions:** determine which MCP servers, skills, or tools solve real tasks and reduce failure.
- **Reliability and risk management:** prioritize error patterns, repeated attempts, and abnormal tasks with the greatest user impact.
- **Organizational knowledge:** retain proven approaches and improved answers as a local Agent work-method library.

The market value is not simply collecting more logs. It turns an opaque Agent into digital labor that can be measured, compared, improved, and connected to business value. Individuals gain evidence for improving local assistants; teams gain a continuous data foundation from real use through evaluation, iteration, and ROI evidence.

## Quick Start

### One-Prompt Installation for an AI Agent

Copy the complete prompt below into the local AI Agent you use. It clones the project, installs the command-line tool, detects and connects available platforms, installs MCP, installs the analysis Skill, and runs health checks. It must not overwrite existing MCP, Hook, Skill, or user configuration; it should report conflicts and ask before proceeding.

```text
Install and verify Agent Asset Expert on my local macOS machine. Perform the following work directly, then report each result, every configuration file changed, and the health-check outcome in a concise checklist.

1. Check for git, Python 3.11+, and pipx. If pipx is unavailable, install it with the current Python and ensure its command directory is on PATH.
2. Clone the project: if ~/agent-asset-expert does not exist, run git clone https://github.com/Kz-Aven/agent-asset-expert.git ~/agent-asset-expert. If it already exists, preserve user changes; do not delete or reset it.
3. Install the project: enter ~/agent-asset-expert. For a first installation, run pipx install .; if it is already installed through pipx, run pipx install --force . to update it from the local project.
4. Install the collector and MCP: run agent-asset-expert install --platform auto. Detect Tigerose, Codex, and WorkBuddy; change only configuration owned by this tool, preserve every existing MCP and Hook, and use the tool's backups when needed.
5. Install the analysis Skill: install ~/agent-asset-expert/skills/agent-asset-analysis using the current local Agent platform's standard Skill-installation mechanism. If the platform cannot install local Skills, state that clearly and retain the source path for manual use.
6. Verify: run agent-asset-expert status and agent-asset-expert doctor. If doctor reports no data yet, explain that one real Agent task is needed to complete collection verification.
7. Do not delete existing data, configuration, MCP servers, Hooks, or Skills. Do not upload local data. Do not modify files outside the project unless required to complete the installation.
```

### Manual Installation

```bash
cd ~/agent-asset-expert
pipx install .
agent-asset-expert install --platform auto
agent-asset-expert doctor
```

Add the MCP server to the Agent you use for analysis:

```text
command = "agent-asset-expert"
args = ["mcp"]
```

Example questions:

> Find the status, ending reason, and token usage for Data Analysis A Miao's latest task without asking me for an ID.

> Compare two assistants' completion rate, average token usage, and average duration for fully captured work this week.

> Find failed, fully recorded work from the last 30 days and summarize it by error code.

## What Is Saved

- **Outcome and performance:** status, duration, token metrics, retries, and errors.
- **Work context:** the user's request, the final response, and any available intermediate work and tool results.
- **Environment references:** immutable references to the Agent, Skills, Tools, MCP services, and Prompt snapshots used for the work.
- **Large content:** large inputs or outputs held behind controlled local `content_ref` references.

| Label | Meaning |
| --- | --- |
| `collection_mode` | How the work was collected: `runtime_adapter`, `hook_collector`, or `log_collector`. |
| `coverage` | Whether the platform exposed a full or partial work history. |
| `trace_integrity` | Whether every collected part of the work history was saved successfully. |

For rigorous reviews or evaluation datasets, filter for:

```text
coverage=full
trace_integrity=complete
```

## Supported Integrations

### Tigerose

```bash
agent-asset-expert install --platform tigerose
```

This repoints `~/Library/Application Support/Tigerose/mcp.json` `agent_assets` to Agent Asset Expert's standalone read-only MCP server. The installer backs up the original entry and restores it on uninstall. When `TIGEROSE_ROOT` points to a local source checkout, the optional `TigeroseRuntimeBridge` can collect turn, LLM, tool, configuration, and feedback lifecycle data with `coverage=full`.

### Codex

The adapter detects `$CODEX_HOME/config.toml` (default: `~/.codex/config.toml`) and installs a local Hook Collector descriptor. Register the stdio MCP server with the Quick Start command. Some Codex model internals are not exposed through Hooks, so records are accurately labeled `coverage=partial`.

### WorkBuddy

```bash
agent-asset-expert install --platform workbuddy
```

This adds Agent Asset Expert's Hook command to `UserPromptSubmit`, `PostToolUse`, `Stop`, `Interrupt`, and `SessionEnd` in `~/.workbuddy/settings.json`. Existing Hooks are unchanged; uninstall removes only owned entries. WorkBuddy currently uses safe Hook-based collection, so records are labeled `coverage=partial` until a future extension API exposes fuller runtime access.

Check installation status:

```bash
agent-asset-expert status
agent-asset-expert doctor --platform PLATFORM
```

## MCP Capabilities

The read-only MCP server provides:

- `list_assistants`
- `list_executions`
- `get_latest_execution`
- `get_execution`
- `get_execution_trace`
- `read_content`
- `summarize_execution_metrics`
- `list_eval_candidates`
- `query_readonly_sql`

Use focused tools first. `query_readonly_sql` is a restricted fallback for one parameterized portable `SELECT`, or `CTE + SELECT`, against one registered assistant database. It rejects writes, schema changes, transactions, `PRAGMA`, `ATTACH`, comments, multiple statements, and SQLite-only functions.

## Data Location and Privacy

Work records are never stored in this Git repository. By default, they remain on your Mac:

```text
~/Library/Application Support/AgentAssetExpert/data/
  registry.db
  assistants/{platform}--{assistant_id}.db
  assistants/{platform}--{assistant_id}/contents/sha256/{prefix}/{sha256}
```

Each platform/assistant pair has a separate database. `registry.db` only contains controlled locators and assistant metadata for cross-assistant discovery. It contains no Prompt, output, or tool-result body.

Before hashing or persistence, Agent Asset Expert redacts credential-like values including API Key, Secret, Token, Cookie, Password, Authorization, and Private Key. Large content is stored locally behind opaque `content_ref` references.

Data remains local until you explicitly delete it. The initial release relies on current-user macOS directory permissions and does not provide application-layer encryption. Do not place the runtime data directory in a synced or shared directory unless you intentionally accept the privacy implications.

To remove an integration without deleting collected work records:

```bash
agent-asset-expert uninstall --platform PLATFORM
```

## License

MIT.
