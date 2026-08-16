---
layout: post
title: "工具经济需要客观数据：Agent 调用测量的标准与体系"
subtitle: "Agent 正在成为软件分发最重要的新渠道，但工具作者对自己工具被 Agent 用了多少次、成功与否、谁在用——一无所知。"
date: 2026-08-16 08:00:00 +0800
reading_time: 12
tags:
  - Agent
  - 开源
  - 数据标准
description: 本文提出一套客观测量 Agent 调用的三层标准（识别/证明/聚合）与开源中间件 agent-used，让"Agent 使用量"成为像 npm 下载量一样可信的开发者决策数据。
---

Agent 正在成为软件分发最重要的新渠道。工具作者却对这一层消费完全盲区。

过去十年，开发者判断"我的项目有没有人用"靠三个数字：下载量、star、issue。它们不完美，但客观、可比较、可追溯。

2026 年，一个新的消费群体出现：Agent。Claude Code、Codex、Cursor 会替用户选择工具、安装 skill、调用 MCP server。对很多工具来说，**Agent 推荐正在成为比搜索更重要的入口**——用户不再浏览 README，而是问 Agent"我要一个研究监测工具"，Agent 替他选。

但工具作者看到什么？

| 渠道 | 你能看到什么 | 缺失 |
| --- | --- | --- |
| GitHub star / clone | 人是否关注 | Agent 是否使用？ |
| skills.sh 安装数 | CLI 自报遥测 | 可刷、无 API、无验证 |
| MCP registry | 被收录 | 官方明确不做采纳数据 |
| llms.txt | 声明了 | 审计显示 97% 的 llms.txt 零 AI 请求 |
| Agent 会话 | 无 | 完全黑箱 |

**Agent 经济正在成为一场没有记分牌的比赛。** 没有客观数据，开发者只能靠感觉决策：该不该继续维护这个 MCP server？该把算力投到哪个工具？该不该为 Agent 优化 README？

## 为什么是现在

标准正在 2026 年形成：AAIF（Agentic AI Foundation）2025 年 12 月成立，MCP、goose、AGENTS.md 入基金会；gh skill 2026 年 4 月上线，GitHub 正式把 repo 变成 agent 资产；OpenTelemetry GenAI 语义约定包含 Execute tool span（Development 状态）；IETF 出现 11 个 agent 发现草案。

**谁定义"Agent 使用量"的口径，谁就拿到下一个 npm 下载量的定义权。**

## 三层测量标准

任何客观测量体系需要回答三个问题：谁在调用（识别）、调用是否真实（证明）、总量是多少（聚合）。

**L1 识别——谁在调用。** MCP 协议自带的 `clientInfo {name, version}` 零成本完成；HTTP 用请求头；CLI 用环境变量。尽力而为：不自报时记 `unknown`，不拒绝服务。

**L2 证明——调用是真的。** 被调方签发可验证回执（HMAC 签名 + nonce 防重放）。**关键：计数发生在被调方**——wrapper 坐在真实调用边界，调用方无法自报。这是与所有自报式遥测的本质区别。

**L3 聚合——总量可信。** 开放事件格式（JSONL，schema 公开）+ 聚合 API + README 徽章（"本月 N 次 Agent 调用"）+ 异常检测与独立信号交叉验证。

## 实现：一行命令接入的中间件

不要求项目改造内部——wrap 一层：

```bash
# MCP server（被调方计数）
agent-used wrap -- npx @your/mcp-server

# Agent 侧（调用方计数，与 wrapper 交叉验证）
agent-used hook install --agent codex    # 写 ~/.codex/hooks.json

# 本地聚合 → README 徽章
python3 aggregator.py import --events ~/.agent-used/events/agent-use-events.jsonl
python3 aggregator.py serve --port 8787
```

Codex 和 Claude Code 都提供用户级 hooks（PostToolUse 等 11 种事件），在工具调用边界注入脚本**不需要平台合作**——这意味着调用方计数今天就能落地，平台原生支持是升级路径而非前置条件。两侧数据交叉验证，可信度高于任何单侧计数。

事件只含元数据：工具名、结果、粗粒度耗时、宿主、时间。**参数、内容、路径、身份——代码级保证不记录**（测试断言防泄漏）。

## 政策与伦理：不碰的红线

1. **不自动 star / follow**：GitHub AUP 明确禁止 automated starring（rank abuse）——本体系测量"使用"，永远不激励 Agent 去 star
2. **不爬 GitHub**：数据来自用户自有工具事件；交叉验证走官方 API
3. **不伪造**：被调方计数 + 签名，伪造即违约
4. **只收聚合**：`DO_NOT_TRACK=1` 全程生效，默认本地、opt-in 上传

## 采用路径

**Agent 平台路径**：hooks 已证明用户侧注入可行；下一步以白皮书 + 标准草案对齐 AAIF / OTel GenAI，推动"被调方计数"成为平台原生能力——对工具作者是免费的客观数据，对平台是生态吸引力。

**代码平台路径**：gh skill 已把 repo 变成 agent 资产但无使用指标；agent-used 的验证层（签名 + 异常检测）是 GitHub 生态缺的那块。保持接触。

两条路，一条走通即可。

## 行动号召

- **工具作者**：接入 agent-used，用真实数据决定方向
- **Agent 厂商**：采纳 L1 识别头，让 Agent 调用可被测量——对生态是净收益
- **标准社区**：参与口径讨论（AAIF / OTel GenAI）
- **读者**：转发这份白皮书，把"Agent 使用量"变成行业公共品

项目开源在 [github.com/roy-tong/agent-used](https://github.com/roy-tong/agent-used)（事件标准、wrapper、hook SDK、聚合器，MIT），事件 schema 与 SPEC 全文在仓库内。反馈请开 Issue，或直接在 X 找我。
