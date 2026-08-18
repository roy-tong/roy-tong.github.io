---
layout: post
lang: en
title: "Agent Capability Monthly · Issue 01: The Ecosystem Baseline"
subtitle: "A baseline issue, not a news roundup — fixing the current state, the measurement method, and the data definitions that every future issue will compare against."
date: 2026-08-18 09:30:00 +0800
permalink: /en/notes/agent-capability-monthly-01/
reading_time: 9
tags:
  - agent
  - capability economy
  - monthly report
  - measurement
description: "The baseline issue of Agent Capability Monthly. Fixed eight-section structure: new capabilities, new providers, pricing changes, MCP/Skills ecosystem, agent commerce, measurement developments, top 5 signals, Roy's view. This issue fixes the baseline: 106 agent-invocable capabilities across 11 categories, and why payment companies building metering validates measurement-before-payment."
---

> **Agent Capability Monthly** is a fixed monthly report answering one question: as agents become software consumers, what is happening to the software economy. The structure is fixed in eight sections: new capabilities, new providers, pricing changes, MCP/Skills ecosystem, agent commerce, measurement developments, top 5 signals, Roy's view.
>
> **Issue 01 is the baseline issue**: it does not chase this month's news. It fixes the ecosystem's current state, the measurement method, and the data definitions that every future issue reports deltas against. Facts carry sources and dates; judgments are labeled as judgments.

## 0. Why a monthly report is needed now

As software consumers shift from humans to agents, the old measurement chain (installs, seats, page views) breaks at every link, and no stable discourse for the new measurement layer exists yet. The industry conversation is fragmented: some talk about protocols, some about tools, some about payments, some about observability. This report does one thing: **record the ecosystem with a fixed vocabulary so that change becomes visible.**

Two factual foundations of the baseline:

- **Agent Capability Index** ([public map](/en/capability-index/)): **106 entries / 11 categories** of agent-invocable software, v0.1 seed data with provider, interface, pricing, availability, and source.
- **AgentMeasure** ([open measurement infrastructure](https://github.com/roy-tong/AgentMeasure)): the five-stage chain Reach → Choice → Use → Utility → Value, evidence grading E0–E5, observation context Context × execution validity Validity.

## 1. New capabilities

Baseline definition: **a Capability is a single capability of software that an agent can invoke — not the whole app.** Inclusion criteria: public documentation, a verifiable interface (API / CLI / SDK / MCP / self-hosted), and a stated pricing model.

Baseline distribution (106 entries):

| Category | Count | Notes |
|---|---|---|
| Search | 11 | web / semantic / answer-style search |
| Coding | 10 | repos, CI/CD, package ecosystems |
| Browser | 10 | automation, scraping, hosted browsers |
| Data | 10 | document DBs, analytics, vector DBs |
| Compute | 11 | functions, GPUs, inference |
| Communication | 9 | messaging, email, meetings |
| Payments | 9 | acquiring, subscription billing, financial data |
| Commerce | 7 | e-commerce, seller backends |
| Real-world Action | 7 | delivery, mobility, booking (mostly partner-gated) |
| Creative Tools | 10 | image, video, voice |
| Productivity | 12 | office, project management, files |

**Judgment**: Payments and Real-world Action are the smallest and most unstable categories (partner-gated APIs, opaque pricing). This is the data-layer reflection of the measurement-before-payment gap — the capabilities closest to money are the ones with the least public accounting.

## 2. New providers

Baseline definition: a provider is an organization offering at least one invocable capability. v0.1 skews toward US/EU infrastructure vendors; the Chinese ecosystem (WeChat, Feishu, DingTalk, …) will be filled in v0.2 — which is itself a backlog item and a contribution opportunity ([Add a capability](/en/capability-index/)).

**Judgment**: today's provider structure is heavily concentrated in "agent-era infrastructure" — search, browsers, vector DBs, inference APIs. Consumer-facing real-world capabilities (booking, delivery, payments) remain partner-gated and under-open. The metric worth tracking over the next 12 months is not how many APIs appear, but **how many real-world capabilities start opening to agents**.

## 3. Pricing changes

Baseline facts (sources linked):

- The model price war that began in H2 2025 continues: Claude Opus 4.5 launched and was aggressively discounted, read as price dumping against Google and OpenAI ([reseller.co.nz](https://www.reseller.co.nz/article/4097187/anthropics-claude-opus-4-5-pricing-cut-signals-a-shift-in-the-enterprise-ai-market-3.html), [PYMNTS](https://www.pymnts.com/news/artificial-intelligence/2025/google-and-anthropic-drop-ai-prices-and-release-new-models/)); o3 dropped ~80%, creating a new price-performance tier ([Towards AI](https://newsletter.towardsai.net/p/tai-157-o3-drops-80-to-undercut-rivals)); Q4 2025 model pricing changes are now being tracked systematically ([dataku](https://dataku.ai/blog/every-ai-pricing-change-q4-2025-tracked)).
- Falling inference cost → each agent "thought" is cheaper → **per-call cost share falls while the share of capability/software cost rises**.

**Judgment**: the model price war is the supply-side precondition of the Agent Capability Economy: once inference is no longer the cost center, a software "capability fee" becomes a separately priced, separately billable object. That is the macro condition under which CaaS (Capability as a Service) can exist.

## 4. MCP / Skills ecosystem

Baseline facts:

- **GitHub MCP Registry** launched (2025-09): a central discovery and trust entry point for MCP servers ([InfoWorld](https://www.infoworld.com/article/4061244/github-introduces-registry-for-finding-mcp-servers.html), [DevOps.com](https://devops.com/github-mcp-registry-launches-as-central-hub-for-ai-development-tools/)).
- **MCP's first-year spec release** (2025-11) shifted focus to authorization extensions — from "can connect" to "can safely act on a user's behalf" ([modelcontextprotocol.info](https://modelcontextprotocol.info/blog/first-mcp-anniversary/)).
- Ecosystem scale (established site figures): MCP SDK monthly downloads approached the **100M level by mid-2026**; the top skills.sh skill accumulated ~**2M installs in five months**.
- But the official registry explicitly does not publish adoption or usage data — **the discovery layer is consolidating while the usage layer still has no data** (see §6).

**Judgment**: the MCP ecosystem is moving from "protocol fragmentation" to a three-layer stack — protocol + registry + authorization. Registries solve discovery, authorization solves trust, and neither produces usage data. Measurement is not being replaced; it is being approached — the more standardized the connection layer, the more feasible a unified measurement vocabulary becomes.

## 5. Agent commerce

Baseline facts:

- **Agentic Commerce Protocol (ACP)**: OpenAI and Stripe jointly defined a protocol for agents buying software/services on a user's behalf; Stripe ships an Agent Toolkit with paid-tools and usage-based billing/metering alongside it ([The AI Journal](https://aijourn.com/agent-commerce-protocol-acp-and-google-ap2-the-next-layer-of-autonomous-transactions/), [Stactize](https://stactize.com/artikel/stripes-agentic-commerce-protocol-what-it-means-for-saas-companies-selling-through-cloud-marketplaces/), [DeepWiki: usage-based billing](https://deepwiki.com/stripe/agent-toolkit/4-usage-based-billing-and-metering)).
- **Google AP2** (Agent Payments Protocol): the competing autonomous-transaction protocol candidate ([The AI Journal](https://aijourn.com/agent-commerce-protocol-acp-and-google-ap2-the-next-layer-of-autonomous-transactions/)).
- Established site figures: Cloudflare **x402 / Agentic Payments**, Coinbase **Bazaar**, and ACP are the main 2026 payment-layer players.
- OpenAI DevDay 2025 positioned ChatGPT as an "AI OS" with in-chat apps and commerce as part of the platform narrative ([windowsforum](https://windowsforum.com/threads/openai-devday-2025-chatgpt-as-ai-os-with-in-chat-apps-and-commerce.384079/)).

**Judgment**: the payment layer is converging from "who can charge an agent" into a protocol contest — ACP vs AP2 vs x402 vs Bazaar. But every payment protocol silently assumes that metered usage is reliable. That assumption does not hold today: **payment is the last three layers; measurement is the first layer, and the industry is paying attention to the last three only.**

## 6. Measurement developments

Baseline facts:

- **Stripe's Agent Toolkit** builds usage-based billing and metering directly into the agent payment stack ([DeepWiki](https://deepwiki.com/stripe/agent-toolkit/4.2-usage-based-billing-and-metering)).
- **OpenTelemetry** published an AI agent observability guide; GenAI semantic conventions are still evolving ([opentelemetry.io](https://opentelemetry.io/blog/2025/ai-agent-observability/)).
- Established site figures: **AAIF has been formed**; AgentMeasure published [Benchmark Run #001]({{ '/notes/every-agent-usage-number-is-self-reported-zh/' | relative_url }}) (an evidence audit of six real agent-usage claims: every number is self-reported, nobody publishes the unit definition); the CORE spec is at Draft 0.4.3; Pipeline Validation #001 (42 calls → 84 observations); Measurement Report #001 is reserved for the first external provider.

**Judgment**: measurement is becoming mainstream, but the directions diverge: payment vendors build **metering to bill**, observability tools build **telemetry to debug**, and AgentMeasure argues for a third kind — **verifiable measurement to compare and settle**. Same goal, different vocabularies. Whoever defines a verifiable, cross-vendor "agent usage" first owns the next npm download count. The window is 2026.

## 7. Top 5 signals

1. **Protocols are consolidating; the usage layer still has no data.** MCP now has a registry and authorization extensions, but adoption and usage data remain absent — the faster discovery consolidates, the more visible the measurement gap becomes.
2. **Payment vendors are building metering themselves.** Stripe's Agent Toolkit ships metering, which is the strongest validation yet that "measurement precedes payment" — the largest payment rails are betting on usage metering.
3. **The model price war clears the way for capability pricing.** As inference costs collapse, independent pricing and billing of software capability becomes economically viable for the first time.
4. **Real-world capabilities are the least open.** Payments and Real-world action are the smallest, most partner-gated categories in the index — openness is the next bottleneck and the next opportunity.
5. **The standardization window is open.** AAIF exists, OTel GenAI semantics are not finalized, and ACP/AP2 are unformed — 2026 is the window to define "verifiable agent usage."

## 8. Roy's updated view

The baseline judgment holds, plus one addition:

- **Unchanged**: measurement precedes payment; the five-stage chain (Reach → Choice → Use → Utility → Value) is the irreducible granularity; evidence grading (E0–E5) is the minimum implementation of verifiability.
- **Added**: payment vendors building metering is not a threat — it is validation. It moves measurement from an academic claim into the plumbing of commercial infrastructure. AgentMeasure's position should advance from "proposing a measurement language" to "**acting as the referee and registry for cross-vendor definitions**" — coexisting with ACP/AP2/x402, owned by none of them.
- **Next (Aug–Sep)**: grow the Capability Index to 200+ entries and open provider claiming; publish Measurement Report #001 (first external provider data); make this report a fixed expectation — same day every month.

---

*Related: [Agent Capability Index](/en/capability-index/) · [When the Software Consumer Becomes an Agent](/en/notes/when-the-software-consumer-becomes-an-agent/) · [Every Agent Usage Number Is Self-Reported](/en/notes/every-agent-usage-number-is-self-reported/) · [AgentMeasure](https://github.com/roy-tong/AgentMeasure) · [Subscribe via RSS](/feed.xml) · [中文版](/notes/agent-capability-monthly-01/)
