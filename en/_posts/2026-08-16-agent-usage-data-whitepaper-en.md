---
layout: post
lang: en
title: "The Tool Economy Needs Objective Data: A Standard for Measuring Agent Tool Calls"
subtitle: "Agents are becoming the most important new distribution channel for software — yet tool authors have no idea how often their tools are called, whether calls succeed, or who is calling."
date: 2026-08-16 08:00:00 +0800
reading_time: 10
tags:
  - agent
  - open source
  - measurement
description: A three-layer standard (identify / attest / aggregate) and an open-source middleware, agent-used, to make "agent usage" as credible a developer decision metric as npm downloads.
permalink: /en/notes/agent-usage-data-whitepaper/
---

Agents are becoming the most important new distribution channel for software. Tool authors are blind to that layer.

For a decade, developers judged "is anyone using my project" with three numbers: downloads, stars, issues. Imperfect, but objective, comparable, traceable.

In 2026 a new class of consumer arrived: agents. Claude Code, Codex and Cursor pick tools for users, install skills, call MCP servers. For many tools, **agent recommendation is becoming a bigger entry point than search** — users stop browsing READMEs and ask an agent "I need a research monitor," and the agent chooses.

What can tool authors see?

| Channel | What you see | What's missing |
| --- | --- | --- |
| GitHub stars / clones | Humans | Did agents use it? |
| skills.sh installs | CLI self-report | Gameable, no API, no verification |
| MCP registry | Listed | The registry explicitly publishes no adoption data |
| llms.txt | Declared | Audits show 97% of llms.txt files get zero AI requests |
| Agent sessions | Nothing | Complete black box |

**The agent economy is being played without a scoreboard.** Without objective data, developers decide by feel: should I keep maintaining this MCP server? Where should compute go? Should I optimize the README for agents?

## Why now

The standards are forming in 2026: AAIF (Agentic AI Foundation) launched in December 2025, folding MCP, goose and AGENTS.md into the foundation; `gh skill` shipped in April 2026, making repos first-class agent assets; OpenTelemetry's GenAI semantic conventions include the Execute tool span (still Development status); IETF has 11 competing agent-discovery drafts.

**Whoever defines the "agent usage" metric owns the definition of the next npm download count.**

## A three-layer measurement standard

Any objective measurement system must answer: who is calling (identify), is the call real (attest), what is the total (aggregate).

**L1 Identify — who is calling.** MCP's native `clientInfo {name, version}` costs nothing; HTTP uses request headers; CLIs use environment variables. Best effort: unknown callers are recorded as `unknown`, never rejected.

**L2 Attest — the call is real.** The callee issues a verifiable receipt (HMAC signature, nonce anti-replay). **The key: counting happens on the callee side** — the wrapper sits at the real call boundary, so callers cannot self-report. This is the fundamental difference from every self-reported telemetry system.

**L3 Aggregate — totals are credible.** Open event format (JSONL, public schema) + aggregation API + README badge ("agent calls N/mo") + anomaly detection cross-checked against independent signals.

## Implementation: one-command middleware

No internal refactoring required — wrap a layer:

```bash
# MCP server (callee-side counting)
agent-used wrap -- npx @your/mcp-server

# Agent side (caller-side counting, cross-validated with the wrapper)
agent-used hook install --agent codex    # writes ~/.codex/hooks.json

# Aggregate locally → README badge
python3 aggregator.py import --events ~/.agent-used/events/agent-use-events.jsonl
python3 aggregator.py serve --port 8787
```

Both Codex and Claude Code provide user-level hooks (PostToolUse and 10 other events) that inject scripts at the tool-call boundary — **no platform partnership required**. Caller-side counting works today; native platform support is an upgrade path, not a prerequisite. Cross-validating both sides beats any single-sided count.

Events contain metadata only: tool name, outcome, coarse duration, host, time. **Arguments, content, paths, identity — excluded at the code level** (leak tests assert this).

## Policy and ethics: lines we don't cross

1. **No automated stars or follows** — GitHub's AUP explicitly prohibits automated starring (rank abuse). This system measures usage and never incentivizes agents to star.
2. **No GitHub scraping** — data comes from the user's own tool events; cross-checks use the official API.
3. **No forgery** — callee-side counting plus signatures; forgery is a violation.
4. **Aggregates only** — `DO_NOT_TRACK=1` honored end-to-end; local by default, opt-in upload.

## Adoption paths

**Agent-platform path**: hooks prove user-side injection works today; next step is aligning the standard with AAIF / OTel GenAI so callee-side attestation becomes a native platform capability — free objective data for tool authors, ecosystem gravity for platforms.

**Code-platform path**: `gh skill` made repos agent assets without usage metrics; agent-used's verification layer (signatures + anomaly detection) is what the GitHub ecosystem is missing. Keeping contact.

Either path, if one works, the thing works.

## Call to action

- **Tool authors**: adopt agent-used and decide with real data.
- **Agent vendors**: adopt L1 identification headers — measurable agent calls are a net win for the ecosystem.
- **Standards community**: join the metric discussion (AAIF / OTel GenAI).
- **Readers**: share this, and make "agent usage" a public good.

The project is open source at [github.com/roy-tong/agent-used](https://github.com/roy-tong/agent-used) (event standard, wrapper, hook SDK, aggregator — MIT). The full schema and SPEC live in the repo. Feedback via Issues, or find me on X.
