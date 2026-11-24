---
title: "How to measure the use of software by AI Agent"
date: "2026-08-16T10:00:00+08:00"
lang: en
permalink: "/en/notes/agent-usage-measurement-standard/"
generated_translation: true
content_id: agent-usage-measurement-standard
knowledge_topic: agent-systems
knowledge_units: [agent-measurement]
translation_of: /notes/agent-usage-measurement-standard/
---







<!doctype html>
<html lang="en">
  <head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <meta name="theme-color" content="#f4f5f2">
    <script>
      (function () {
        var theme;
        try { theme = localStorage.getItem('theme'); } catch (error) {}
        var dark = theme === 'dark' || (theme !== 'light' && window.matchMedia('(prefers-color-scheme: dark)').matches);
        document.documentElement.dataset.theme = dark ? 'dark' : 'light';
        document.querySelector('meta[name="theme-color"]').content = dark ? '#121513' : '#f4f5f2';
      })();
    </script>
    <meta name="author" content="Roy.Tong">
    
    <link rel="icon" type="image/svg+xml" href="/assets/favicon.svg">
    <link rel="stylesheet" href="/assets/css/style.css?v=20261109-1">
    <link rel="stylesheet" href="/assets/css/knowledge.css?v=20260901-v3">




      <link rel="alternate" hreflang="en" href="https://roy-tong.github.io/en/notes/agent-usage-measurement-standard/">
      <link rel="alternate" hreflang="zh-CN" href="https://roy-tong.github.io/notes/agent-usage-measurement-standard/">
      <link rel="alternate" hreflang="x-default" href="https://roy-tong.github.io/notes/agent-usage-measurement-standard/">
    <link type="application/atom+xml" rel="alternate" href="https://roy-tong.github.io/feed.xml" title="Roy.Tong"/>
    <!-- Begin Jekyll SEO tag v2.8.0 -->
<title>How to measure the use of software by AI Agent | Roy.Tong</title>
<meta name="generator" content="Jekyll v3.9.5"/>
<meta property="og:title" content="How to measure the use of software by AI Agent">
<meta name="author" content="Roy.Tong"/>
<meta property="og:locale" content="en_US">
<meta name="description" content="When software consumers change from people to agents, and economic units change from software seats to callable capabilities, measurement problems come before payment problems. AgentMeasure proposes a unified measurement basis for CaaS and Agent Capability Economy - Reach → Choice → Use → Utility → Value.">
<meta property="og:description" content="When software consumers change from people to agents, and economic units change from software seats to callable capabilities, measurement problems come before payment problems. AgentMeasure proposes a unified measurement basis for CaaS and Agent Capability Economy - Reach → Choice → Use → Utility → Value.">
<link rel="canonical" href="https://roy-tong.github.io/en/notes/agent-usage-measurement-standard/">
<meta property="og:url" content="https://roy-tong.github.io/en/notes/agent-usage-measurement-standard/">
<meta property="og:site_name" content="Roy.Tong"/>
<meta property="og:type" content="article"/>
<meta property="article:published_time" content="2026-08-16T10:00:00+08:00"/>
<meta name="twitter:card" content="summary"/>
<meta property="twitter:title" content="How to measure the use of software by AI Agent">
<script type="application/ld+json">
{"@context":"https://schema.org","@type":"BlogPosting","author":{"@type":"Person","name":"Roy.Tong"},"dateModified":"2026-08-16T10:00:00+08:00","datePublished":"2026-08-16T10:00:00+08:00","description":"当软件消费者从人变成 Agent、经济单元从软件席位转向可调用能力，计量问题先于支付问题出现。AgentMeasure 提出面向 CaaS 与 Agent Capability Economy 的统一计量基础——Reach → Choice → Use → Utility → Value。","headline":"如何度量 AI Agent 对软件的使用","mainEntityOfPage":{"@type":"WebPage","@id":"https://roy-tong.github.io/notes/agent-usage-measurement-standard/"},"publisher":{"@type":"Organization","logo":{"@type":"ImageObject","url":"https://roy-tong.github.io/assets/images/social-preview.png"},"name":"Roy.Tong"},"url":"https://roy-tong.github.io/notes/agent-usage-measurement-standard/"}</script>
<!-- End Jekyll SEO tag -->

  </head>
  <body>
    
    
    
    <a class="skip-link" href="#main">Jump to the text</a>

    <header class="site-header">
      <div class="shell nav-wrap">
        <a class="brand" href="/en/" aria-label="Return to the home page">
          <span class="brand-mark">R</span>
          <span>Roy.Tong</span>
        </a>

        <button class="menu-toggle" type="button" aria-expanded="false" aria-controls="site-navigation" aria-label="Turn on the navigation">
          <svg viewbox="0 0 24 24" aria-hidden="true">
            <path d="M4 7h16M4 12h16M4 17h16"/>
          </svg>
        </button>

        <nav class="nav" id="site-navigation" aria-label="Main navigation">
          
            <a href="/en/essays/">Article</a>
          
            <a href="/en/knowledge/">Knowledge base</a>
          
            <a href="/en/projects/">Project</a>
          
            <a href="/en/about/">About</a>
          
            <a href="/en/support/">Contact</a>
          
          <div class="nav-tools">
            <a class="language-toggle" href="/notes/agent-usage-measurement-standard/" hreflang="zh-CN" lang="zh-CN" data-language-switch data-target-language="zh-CN" aria-label="切换至中文" title="切换至中文">中文</a>
            <button class="theme-toggle" type="button" aria-pressed="false" aria-label="Switch to dark mode" title="Switch to dark mode">
              <svg class="theme-icon" viewbox="0 0 24 24" aria-hidden="true">
                <circle cx="12" cy="12" r="4"/>
                <path d="M12 2v2M12 20v2M4.93 4.93l1.42 1.42M17.65 17.65l1.42 1.42M2 12h2M20 12h2M4.93 19.07l1.42-1.42M17.65 6.35l1.42-1.42"/>
              </svg>
            </button>
          </div>
        </nav>
      </div>
    </header>

    <main id="main"><p class="translation-note" aria-label="Translation note">Machine-assisted translation. <a href="/notes/agent-usage-measurement-standard/">Read the Chinese original</a>.</p>
      




<article class="post shell reading-shell">
  <header class="post-header">
    <a class="eyebrow back-link" href="/en/archive/">← Back to the article</a>
    <h1>How to measure the use of software by AI Agent</h1>
    <p class="post-subtitle">Unified measurement basis for CaaS and Agent Capability Economy</p>
    <div class="post-meta">
      <time datetime="2026-08-16T10:00:00+08:00">2026-08-16</time>
      <span>18 minutes to read</span>
      
      <a class="post-translation" href="/notes/agent-usage-measurement-standard/" hreflang="zh-CN">阅读中文版 →</a>
      
        <span class="post-tags">
          <a href="/en/tags/#agent">#Agent</a><a href="/en/tags/#%E5%BA%A6%E9%87%8F%E6%A0%87%E5%87%86">#Measurance standard</a><a href="/en/tags/#capability%20economy">#Capability Economy</a>
        </span>
      
    </div>
  </header>

  <div class="prose">
    <p><em>Whitepaper v0.2 · AgentMeasure Standard Draft 0.4</em></p>

<blockquote>
  <p>Author: Roy Tong (Xiarui)

Reference implementation: AgentMeasure repository (GitHub).</p>
</blockquote>

<h2 id="摘要">Summarize</h2>

<p>AI Agent is increasingly<strong>Represent users and organizations</strong>Select, call and trade with the software. When Skill, MCP server,

When API and CLI interfaces are becoming easier and easier to create and distribute, the economic value is increasingly concentrated on the scarce capabilities behind them:

Exclusive data, computing power, execution, authority, transaction and real-world performance.</p>

<p>This causes the problem of measurement before the problem of payment. An ability should be able to be reliably priced, compared, billed and

Optimization, ecology must first be &quot;what is the choice, what is the first operation, what is the successful delivery, what is the result is consumed,

What is the result and what is the billing unit&quot; reached a consensus.</p>

<p>AgentMeasure proposes a set of open measurement standards for this emerging Capability Economy: Reach →

The common data language of Choice → Use → Utility → Value, plus future Metering, Marketplace and

The payment track can construct the measurement semantics on it. The goal is not the dashboard, but to let<strong>Capability as a Service

(CaaS, usage in this article) becomes the basis of measurement that is possible</strong>。</p>

<h2 id="一从-saas-到-capability-economy">I. From SaaS to Capability Economy</h2>

<p>Software distribution once had a readable link: download, installation and use. Each era has its own economic unit. The following description

The transformation is<strong>Increment, not substitution</strong>: coexisting with seat-based SaaS and request-based API,

Callable capabilities are becoming a new economic unit of software consumption of Agent intermediary.</p>

<div class="language-text highlighter-rouge"><div class="highlight"><pre class="highlight"><code>SaaS
人 → 应用 → 席位 / 月

API Economy
软件 → API → 请求 / Token

Capability Economy
Agent → Capability → 操作 / 结果
</code></pre></div></div>

<p>Three forces promote the migration to the third line:</p>

<p><strong>The interface is absorbed by Agent.</strong>UI and workflow are increasingly executed by Agent instead of being presented to others. Software

All that&#x27;s left is a callable coat - skill file, MCP tool, CLI, endpoint.</p>

<p><strong>Distributed products are being commercialized.</strong>Open Skill, open MCP adapter, open CLI, anyone can

Create and release within a few hours.<strong>Interfaces may become cheap and easy to make; capabilities are still scarce deliverables.</strong></p>

<p><strong>Scarcity is moving down.</strong>The scarcity layer is no longer the application shell, but the access rights controlled by the call outer shell:</p>

<div class="language-text highlighter-rouge"><div class="highlight"><pre class="highlight"><code>数据 · 算力 · 动作 · 权限 · 信任 · 真实世界履约
</code></pre></div></div>

<p>Search ability is scarce because of indexing; reservation ability is scarce because of the ability to confirm reservations; and payment ability is scarce because of the ability to move money.

When business value is concentrated on ability, the natural economic unit becomes operation, quantity, effect, result - or any of them.

One item of income share.</p>

<p><strong>If Capability becomes an economic unit, Capability measurement becomes infrastructure.</strong>This is the argument of this article.</p>

<h3 id="论点与假设thesis-and-assumptions">Thesis and assumptions (Thesis and assumptions)</h3>

<p>AgentMeasure is based on three<strong>It has not been fully confirmed yet.</strong>On the trend judgment of:</p>

<ol>
  <li>Agent will mediate more and more software selection and execution.</li>
  <li>More software capabilities will be exposed independently from its human UI.</li>
  <li>The business model based on use, effect and result will coexist with seat-based pricing.</li>
</ol>

<p>Even if these trends develop unevenly, measurement standards are still useful: objects, quality rules and claims that discipline itself is established as

A set of Agent software measurement standards.</p>

<h2 id="二先计量后变现measurement-before-monetization">II. Measurement Before Monetization</h2>

<p>To be able to price, bill and build a reputation, CaaS must first have a common measurement semantics. Four questions illustrate this point:</p>

<div class="language-text highlighter-rouge"><div class="highlight"><pre class="highlight"><code>一个用户任务 → 1 个 Operation → 3 次重试
收 1 次钱还是 3 次？

工具成功返回 → Agent 忽略了结果
价值交付了吗？

预订 API 执行了 → 预订从未被确认
能力履约了吗？

任务成功 → 没有这个能力也能成功吗？
Provider 能主张价值吗？

</code></pre></div></div>

<p>These questions cannot be answered by the original number of calls, nor can they be answered by the payment track. They need about<em>operation / attempt / delivery / consumption / effect / outcome</em>The consistent definition of, and

Turn observations into consistent rules of these objects. This consensus is the entry point:<strong>Measure first, then realize</strong>。</p>

<h3 id="现实证据商业先于计量到来">Realistic evidence: commerce comes before measurement</h3>

<p>This is not a hypothesis - the payment and discovery infrastructure of Agent intermediary commerce already exists:</p>

<ul>
  <li><strong>Cloudflare Agents SDK</strong>Allow MCP Tool to be priced by a single call and charged by x402

(<a href="https://developers.cloudflare.com/agents/agentic-payments/x402/charge-for-mcp-tools/">Charge for MCP tools</a>）。</li>
  <li><strong>Coinbase x402 Bazaar</strong>It is the discovery layer: Agent searches for services with price and schema, and through MCP

Complete the paid call (<a href="https://docs.cdp.coinbase.com/x402/bazaar">x402 Bazaar</a>）。</li>
  <li><strong>Agentic Commerce Protocol (ACP) of OpenAI and Stripe</strong>Already in the real agentic

Used in the commerce process (<a href="https://www.digitaltransactions.net/openai-and-stripe-are-the-latest-fintechs-to-enable-agentic-commerce/">Report</a>）。</li>
</ul>

<p>This proves the argument of this section:<strong>Payment and discovery infrastructure comes before the common capability measurement semantics</strong>——

This is exactly the vacancy that AgentMeasure wants to fill.</p>

<h2 id="三测量对象">III. Objects of measurement</h2>

<p><strong>Observation is a unit of evidence, not a unit of business measurement.</strong>AgentMeasure first define the business unit:</p>

<div class="language-text highlighter-rouge"><div class="highlight"><pre class="highlight"><code>Provider
    ↓
Software Entity
    ↓
Capability
    ↓
Interaction Surface
</code></pre></div></div>

<blockquote>
  <p><strong>Capability is the main function and measurement object. Offering is the commercial package of one or more Capability.</strong>——Defined in Commercial Extension (experimental), never insert Core measurement spectrum.</p>
</blockquote>

<table>
  <thead>
    <tr>
      <th>Object</th>
      <th>Definition</th>
      <th>Tier</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Software Entity</td>
      <td>The measured software: Tool, Skill, API, Data Source, Agent, Application, Runtime Capability</td>
      <td>Market</td>
    </tr>
    <tr>
      <td>Capability</td>
      <td>Named functions of entities - main functions and measurement objects</td>
      <td>Market</td>
    </tr>
    <tr>
      <td>Interaction Surface</td>
      <td>The observable call interface of the ability (mcp_tool, cli_command, http_endpoint...)</td>
      <td>Market</td>
    </tr>
    <tr>
      <td>Decision Opportunity</td>
      <td>A tool selection decision</td>
      <td>Behavior</td>
    </tr>
    <tr>
      <td>Candidate Set</td>
      <td>The collection of candidates really provided by the decision</td>
      <td>Behavior</td>
    </tr>
    <tr>
      <td>Presentation</td>
      <td>A selectable appears in the candidate set.</td>
      <td>Behavior</td>
    </tr>
    <tr>
      <td>Selection</td>
      <td>Agent selects a selectable</td>
      <td>Behavior</td>
    </tr>
    <tr>
      <td>Operation</td>
      <td>For a task to a Capability once<strong>Logical use</strong></td>
      <td>Behavior</td>
    </tr>
    <tr>
      <td>Attempt</td>
      <td>An actual execution of Operation (<strong>Retry = Multiple Attempts</strong>）</td>
      <td>Behavior</td>
    </tr>
    <tr>
      <td>Result / Effect</td>
      <td>What has the ability returned / What has the world changed?</td>
      <td>Behavior</td>
    </tr>
    <tr>
      <td>Task</td>
      <td>The task unit served by Operation</td>
      <td>Behavior</td>
    </tr>
    <tr>
      <td>Client</td>
      <td>Independent Agent runtime / installation</td>
      <td>Market</td>
    </tr>
    <tr>
      <td>Project</td>
      <td>Software projects belonging to package/MCP/skill</td>
      <td>Market</td>
    </tr>
    <tr>
      <td>Category</td>
      <td>Comparable capability categories (search, booking...)</td>
      <td>Market</td>
    </tr>
    <tr>
      <td>Observation</td>
      <td>Evidence record of measurement facts (authentication and signature are optional, defined by verification profiles)</td>
      <td><strong>Evidence</strong></td>
    </tr>
  </tbody>
</table>

<p>Observe what happened in<strong>Interaction Surface</strong>Layer; belongs to<strong>Software Entity</strong>It can be read by machine.

Registry analysis - never guess when observing.</p>

<p><strong>Pricing is not the object of the core model.</strong> <code class="language-plaintext highlighter-rouge">Offering</code>——Cite one or more commercial packaging of Capability,

Including allowed surface, pricing policy, service level objectives and commercial constraints - defined in Commercial Extension

(Experimental, non-normative), so that the evolution of measurement semantics is not kidnapped by any payment design.</p>

<h3 id="分布事件distribution-events">Distribution events (Distribution events)</h3>

<p>After commercial attribution enters the scope, discovery regains commercial significance - but does not become the denominator of choice:</p>

<div class="language-text highlighter-rouge"><div class="highlight"><pre class="highlight"><code>Published → Listed → Retrieved / Discovered → Presented
</code></pre></div></div>

<p><code class="language-plaintext highlighter-rouge">Presented</code>It is still the denominator of the selection index;<code class="language-plaintext highlighter-rouge">Discovered</code>It&#x27;s a distribution attribution event, answer<em>Which Skill / Registry / Marketplace brings Capability to use</em>。</p>

<h2 id="四agentcapability-交互模型">IV. Agent–Capability Interaction Model</h2>

<p><strong>Reach → Value is the measurement angle, not the universal execution state machine.</strong>Different categories of abilities have different meaningful links:</p>

<div class="language-text highlighter-rouge"><div class="highlight"><pre class="highlight"><code>Information   操作 → 结果 → 消费
Action        操作 → 效应 → 确认
Transaction   操作 → 授权 → 提交 / 结算
</code></pre></div></div>

<p>Interaction Class (information / action / transaction / computation /

Communication / control / storage / sensing) decide which link and which Utility signals are applicable

Meaningful. The search results are<em>Consume</em>; The reservation is<em>Confirm</em>; paid to be<em>Settle an account</em>. Put all the abilities into an assembly line,

The output numbers will lose their meaning.</p>

<h2 id="五测量框架">V. Measurement framework</h2>

<p>Definition of AgentMeasure<strong>Metric Families</strong>, does not define the global North Star.</p>

<p><strong>M1 Distribution — Reach。</strong>Has the ability entered the Agent world?<code class="language-plaintext highlighter-rouge">Available Clients · Eligible Opportunities · Presentations · Presentation Rate · Distribution Coverage</code></p>

<p><strong>M2 Choice - the most Agent-native.</strong>Will Agent choose it when he has a chance?<code class="language-plaintext highlighter-rouge">选择数 · Observed Selection Rate（Observed Selected ÷ Presented）· Conditional Choice Share · 首选率</code></p>

<p><strong>M3 Execution — Use。</strong>Is it easy to use after choosing it? Draft 0.4 Separate Count Operation and Attempt——

This is exactly the difference that Metering needs in the future:</p>

<div class="language-text highlighter-rouge"><div class="highlight"><pre class="highlight"><code>Operations · Attempts · Attempts per Operation
Operation 完成率 · Operation 成功率
Attempt 失败率 · 重试率 · 延迟
</code></pre></div></div>

<p><strong>M4 Utility - Effective use.</strong>Does the ability deliver available information or trigger the expected effect?</p>

<div class="language-text highlighter-rouge"><div class="highlight"><pre class="highlight"><code>Result Utility     已交付 · 已消费 · 已接受
Effect Utility     已应用 · 已确认 · 已回退 / 失败
</code></pre></div></div>

<p><strong>M5 Outcome — Value。</strong>Have you improved the task?<code class="language-plaintext highlighter-rouge">任务成功关联 · 增量提升 · 节省时间 · 节省成本</code></p>

<p><strong>Relationship measurement</strong>(Degraded from an independent chapter to a subsection): Trial → Active → Repeated → Preferred →

Dependent. The most irreplaceable Dependent is still the long-term asset signal.</p>

<h2 id="六测量质量与声称纪律">VI. Measuring quality and claiming discipline</h2>

<p>The quality of evidence is not the quality of covering, neither of which is a qualified quality, nor is it a methodology. A group is 100% real but only covers

The incident of 2% Agent is not market data.</p>

<div class="language-text highlighter-rouge"><div class="highlight"><pre class="highlight"><code>Measurement Quality
├── Provenance / Evidence Strength  观察来自哪里？其来源被支持得多强？
├── Coverage                        我们看到了多少世界？
├── Qualification                   这算不算真实生产使用？
├── Sampling                        采样了吗？不确定性多少？
├── Identity                        标识归一得怎么样？
└── Method/version                  用什么统计、哪个规范版本？
</code></pre></div></div>

<p><strong>Limited use.</strong>Each observation carries two axes - Usage Context (flow source) and Validity (observation whether

True).<strong>Strict Qualified Usage</strong> = <code class="language-plaintext highlighter-rouge">production</code> + <code class="language-plaintext highlighter-rouge">validity=normal</code>: of public indicators

Default caliber. The context/validity of unknown is disclosed separately, and it is never included silently - no &quot;report unknown →

The motivation of &quot;entering the ranking list&quot;. Retry is another Attempt of the same Operation, which is reserved as a reliability signal and does not count

Use logically many times.</p>

<p><strong>Claim discipline.</strong>Each public indicator carries Measurement Label: numerator, denominator, observable population, qualified

Crowd, runtime coverage, grain, choice mode, decision authority, selection constraint.

Observed choices are never said to be preferences; associations are never said to be cause and effect; unobservable choices are never said to be negative.</p>

<h2 id="七测量与计量measurement-and-metering">VII. Measurement and Metering (Measurement and Metering)</h2>

<p>The bridge from the measurement standard to CaaS is semantic:<strong>Measurement unit ≠ Billing unit</strong>, and the three measurement concepts must

Absolutely separate--<strong>Event</strong>Why is it billed?<strong>Unit</strong>In what unit is it?<strong>Quantity</strong>What is the unit:</p>

<table>
  <thead>
    <tr>
      <th>Ability</th>
      <th>billable_event</th>
      <th>billable_unit</th>
      <th>billable_quantity</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Seek</td>
      <td><code class="language-plaintext highlighter-rouge">operation_succeeded</code></td>
      <td>operation</td>
      <td>1</td>
    </tr>
    <tr>
      <td>Data</td>
      <td><code class="language-plaintext highlighter-rouge">result_delivered</code></td>
      <td>record</td>
      <td>1,382</td>
    </tr>
    <tr>
      <td>Computing power</td>
      <td><code class="language-plaintext highlighter-rouge">compute_completed</code></td>
      <td>gpu_second</td>
      <td>47.2</td>
    </tr>
    <tr>
      <td>Action</td>
      <td><code class="language-plaintext highlighter-rouge">effect_confirmed</code></td>
      <td>operation</td>
      <td>1</td>
    </tr>
    <tr>
      <td>Reserve</td>
      <td><code class="language-plaintext highlighter-rouge">effect_confirmed</code></td>
      <td>booking</td>
      <td>1</td>
    </tr>
    <tr>
      <td>Clue</td>
      <td><code class="language-plaintext highlighter-rouge">outcome_qualified</code></td>
      <td>qualified_lead</td>
      <td>5</td>
    </tr>
    <tr>
      <td>E-commerce</td>
      <td><code class="language-plaintext highlighter-rouge">transaction_settled</code></td>
      <td>transaction</td>
      <td>0.03 (income share)</td>
    </tr>
  </tbody>
</table>

<p>Therefore, measurement semantics is defined by Offering:</p>

<div class="language-text highlighter-rouge"><div class="highlight"><pre class="highlight"><code>Billable Event        哪个测量事实触发计费
Billable Unit         计量单位（操作、记录、GPU-秒、效应…）
Billable Quantity     单位如何计数（按策略：attempts、确认…）
Pricing Model         按操作 · 按数量 · 按效应 · 按结果 · 收入分成
Pricing Policy        版本化的价格规则（flat、阶梯、企业协议、surge…）
Quote                 单次调用实际适用的条款（quote_id、policy 版本、单价）
Metering Policy       测量事实 → 计费事实的映射（规则、排除），版本化
Metering Ledger       可重放、可纠错的计量事实账本（revision / supersedes / reversal）
Commercial Attribution  哪些参与方贡献了发现 / 选择 / 收入
</code></pre></div></div>

<p><strong>Payment is not within the scope.</strong>AgentMeasure does not define payment track, wallet, settlement currency, merchant record relationship or

Financial escrow. It outputs the facts of payment system consumption - qualified operation, confirmed effect, qualified result, billing quantity,

Business attribution.</p>

<blockquote>
  <p><strong>AgentMeasure standardizes economic facts and does not move money.</strong></p>
</blockquote>

<h2 id="八归因与增量">VIII. Attribution and increment</h2>

<p><strong>Ability to participate in successful tasks does not mean that it leads to success.</strong></p>

<ul>
  <li><strong>Attribution measurement</strong>(Observational): Which abilities participate in the task chain - can only support the conclusions of &quot;association&quot; and &quot;participation in the execution chain&quot;.</li>
  <li><strong>Incremental measurement</strong>(Counterfactual): How much additional value does the existence of ability create - random comparison is the strongest

Evidence, but many abilities cannot be turned off randomly. Therefore, cause and effect claim to follow<strong>Value Evidence Ladder</strong>：</li>
</ul>

<div class="language-text highlighter-rouge"><div class="highlight"><pre class="highlight"><code>V0 Association            任务成功时参与过
V1 Matched / Observational 控制已知混淆变量比较
V2 Offline Ablation       重放任务、移除能力
V3 Quasi-experiment       switchback / 自然变异
V4 Randomized Holdout     最强因果证据
</code></pre></div></div>

<p>It is only allowed to use the actual output evidence level to support the corresponding causal claim intensity - which is consistent with the discipline of measuring quality.</p>

<p>Business attribution extends the observation side to the distribution chain:</p>

<div class="language-text highlighter-rouge"><div class="highlight"><pre class="highlight"><code>GitHub Skill → Registry → Agent 推荐 → Capability → 支付
</code></pre></div></div>

<p>Who contributed the discovery, choice and income? This is the basis of the future Agent affiliate and income sharing model - and never

It is confused with the causal increment.</p>

<h2 id="九能力信任与可比性capability-trust-and-comparability">IX. Capability Trust and Comparability</h2>

<p>The choice of capable consumers is shaped by many factors. Agent and Marketplace can be in brand, policy, price,

User preferences and platform constraints<strong>Besides</strong>More and more machine-readable performance signals are compared - this is exactly AgentMeasure.

The axis described by the Decision Authority / Selection Constraint model:</p>

<div class="language-text highlighter-rouge"><div class="highlight"><pre class="highlight"><code>Capability Signals
可靠性 · 延迟 · 价格 · 新鲜度 · 消费 · 效应成功 · 结果 · 安全 · 测量覆盖
</code></pre></div></div>

<p>AgentMeasure <strong>Do not calculate the general AgentMeasure Score</strong>. Agent A cares about the price, Agent B cares about the delay,

Agent C cares about privacy. Ranking is the product decision-making of Agent and Marketplace; the standard only defines metable signals.

And the Label that allows them to be compared. Measurement Label is the basis of this comparability.</p>

<h2 id="十观察与部署架构observation--deployment-architecture">X. Observation and Deployment Architecture (Observation&amp; Deployment Architecture）</h2>

<p>Different measurement surfaces can see different things; unilateral access is valuable, but it is claimed that it must match the surface:</p>

<div class="language-text highlighter-rouge"><div class="highlight"><pre class="highlight"><code>分发侧 → Agent Runtime 侧 → Provider 侧 → 效应 / 结果侧
</code></pre></div></div>

<table>
  <thead>
    <tr>
      <th>Surface</th>
      <th>What can I see?</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Registry</td>
      <td>Discovery / Availability</td>
    </tr>
    <tr>
      <td>Agent runtime</td>
      <td>Present / Select / Consume</td>
    </tr>
    <tr>
      <td>Capability provider</td>
      <td>Operation / attempts / result</td>
    </tr>
    <tr>
      <td>Target system</td>
      <td>Effect / Transaction</td>
    </tr>
    <tr>
      <td>Experimental layer</td>
      <td>Incremental</td>
    </tr>
  </tbody>
</table>

<p>Bilateral observation (Agent runtime + provider) constitutes supporting evidence (E2); only the Provider side is enough to support

The usage index of provider-scoped. The standard is not on the request key path: observe asynchronous output, only metadata,

Pseudo-anonymous before the market.</p>

<h2 id="十一互操作">XI. Interoperability</h2>

<p>The standard is transport-neutral and vendor-neutral. The existing infrastructure is used as an example of implementation rather than a prerequisite:

MCP carries life cycle events and trace context; OpenTelemetry carries tool span; Codex/Claude

Code/DeepSeek Harness exposes the observation point of the capability statement; registry provides entity identity. Future payment

The fact of the orbital consumption standard is not the core of the extended standard.</p>

<h2 id="十二不做什么与治理">12. What not to do and manage</h2>

<p>AgentMeasure <strong>No</strong>Payment protocol, Marketplace, wallet or general reputation system. Standard No:</p>

<ul>
  <li>Move money or escrow funds;</li>
  <li>Rank the ability or score the Provider;</li>
  <li>Define what is &quot;good&quot; ability;</li>
  <li>Any central server, Agent-side installation or open source Provider is required.</li>
</ul>

<p>The standard itself is governed by the community (AUP process,<code class="language-plaintext highlighter-rouge">proposals/</code>); The commercial products based on it shall not be controlled

The definition of the standard.</p>

<h2 id="十三开放问题">XIII. Open issues</h2>

<ol>
  <li><strong>Mission boundary</strong>: What is a &quot;task&quot;? Who defines it?</li>
  <li><strong>Effect verification</strong>: How to confirm the effect (reservation confirmation, payment settlement) without deeply integrating each target system?</li>
  <li><strong>Scale increment</strong>: How to run anti-fact experiments across ecology without interfering with production?</li>
  <li><strong>Observability of candidate sets</strong>: Presented is the key denominator, and most runtimes have not exposed the routing layer signal.</li>
  <li><strong>Cross Agent identity</strong>: The same client cross Codex/Claude/DSH - when can we know?</li>
  <li><strong>Consensus of billing units</strong>: What measurement facts will the Provider and the payment track eventually agree on, and what is the cost of mismeasurement?</li>
  <li><strong>Privacy</strong>: How far can the association and retention go under pseudo-anonymity?</li>
</ol>

<h2 id="十四结论">XIV. Conclusion</h2>

<p>Software consumers are changing from people to agents, and economic units are changing from seats to callable capabilities. In the ability being priced,

Before billing and comparison, ecology needs a set of shared measurement language - what is selection, what is operation, what is delivery,

Consumption, effects and results, and which numbers can support which conclusions.</p>

<p>AgentMeasure is the proposal: measure semantics as infrastructure, business semantics as future expansion, and pay to

Other people&#x27;s tracks.<strong>Today: Let developers know how Agent can really use their abilities. Next step: let

Capability can be measured, compared and measured across Agents. Long-term: Become CaaS and Agent Capability

The unified measurement basis of Economy.</strong></p>

<h2 id="参考文献">Reference</h2>

<ol>
  <li>RFC 2119 / BCP 14 — <em>Key words for use in RFCs to Indicate Requirement Levels</em>。</li>
  <li>OpenTelemetry GenAI semantic conventions — <code class="language-plaintext highlighter-rouge">gen_ai.*</code>The tool calls the telemetry field.</li>
  <li>Model Context Protocol (MCP) specification - tool discovery and call surface.</li>
  <li>MCP Registry - server identity entrance of entity resolution.</li>
  <li>EDPB - Pseudo-anonymization guidelines (pseudo-anonymous data may still belong to personal data).</li>
  <li>Cloudflare — <a href="https://developers.cloudflare.com/agents/agentic-payments/x402/charge-for-mcp-tools/">Charge for MCP tools（x402 / Agentic Payments）</a>。</li>
  <li>Coinbase — <a href="https://docs.cdp.coinbase.com/x402/bazaar">x402 Bazaar：Discover &amp; pay over MCP</a>。</li>
  <li>OpenAI / Stripe — Agentic Commerce Protocol (ACP), released in September 2025; see<a href="https://www.digitaltransactions.net/openai-and-stripe-are-the-latest-fintechs-to-enable-agentic-commerce/">Digital Transactions Report</a>。</li>
  <li>AgentMeasure Specification - Core / Metrics / Data / Entity / Quality / Correlation

(<code class="language-plaintext highlighter-rouge">standard/</code>）；Commercial Extension（<code class="language-plaintext highlighter-rouge">extensions/COMMERCIAL.md</code>, experimental);

Machine-readable registry (<code class="language-plaintext highlighter-rouge">schemas/</code>、<code class="language-plaintext highlighter-rouge">registry/</code>); Reference implementation and conformance vectors

Released in the same warehouse.</li>
</ol>

<hr/>

<p><em>The full text of the specification (measurement object, life cycle, indicator family, quality, report) and reference implementation (AgentMeasure) have been open sourced. AgentMeasure 1.0 graduation standard: 2 independent implementations, 3 runtime profiles, 2 tool-side implementations, public conformance + canonical test vectors, 5-10 real projects, published discrepancy report, security and privacy review.</em></p>

  </div>

  

<aside class="kb-related" aria-label="Relevant research materials">
  <h2>Relevant research materials</h2>
  <p>Reports, data and notes are kept in the database and can continue to be consulted. The following is related to the same topic; the evidence directly used in this article shall be subject to the text citation.</p>
  
  <ul></ul>
  <ul>
    <li><a href="/en/knowledge/agent-measurement/">Agent measurement: execution facts, task results and value</a></li>
  </ul>
  <a class="kb-text-link" href="/en/knowledge/">Check all the research materials →</a>
</aside>



  <footer class="post-end">
    <span class="post-end-mark">R</span>
    <div class="post-end-copy">
      
        <strong>Thank you for reading this.</strong>
        <p>I will continue to record my observations on AI, products and entrepreneurship.</p>
      
    </div>
    
      <a class="support-link" href="/en/support/#tip">Support writing<span>♡</span></a>
    
  </footer>
<aside class="kb-related" aria-label="Related research materials"><h2>Related research materials</h2><p>Explore related reports, data summaries and notes in the research library. Direct evidence is cited in the essay itself.</p><a class="kb-text-link" href="/en/knowledge/">Explore the research library →</a></aside>
</article>

    </main>

    <footer class="site-footer">
      <div class="shell footer-grid">
        <div>
          <p class="footer-title">Roy.Tong</p>
          <p>Study how AI becomes products, systems and businesses.</p>
        </div>
        <div class="footer-links">
          
            <a href="/en/knowledge/">Knowledge base</a>
          
            <a href="/en/capability-index/">Ability map</a>
          
            <a href="https://github.com/roy-tong/verovo">Verovo</a>
          
            <a href="https://x.com/elliwoodtong" rel="me">X / Twitter</a>
          
            <a href="https://github.com/roy-tong" rel="me">GitHub</a>
          
            <a href="/en/support/">Contact</a>
          
            <a href="/feed.xml">RSS</a>
          
        </div>
      </div>
      <div class="shell footer-bottom">
        <span>© 2026 Roy.Tong</span>
        <span>Record the facts, and also keep the process of judging the correction.</span>
      </div>
    </footer>

    <script src="/assets/js/main.js?v=20261124-1"></script>
    
  </body>
</html>
