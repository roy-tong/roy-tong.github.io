---
title: "应该如何衡量人工智能代理的软件使用情况"
date: "2026-08-16T10:00:00+08:00"
lang: zh
permalink: "/notes/how-agent-usage-should-be-measured/"
generated_translation: true
content_id: how-agent-usage-should-be-measured
knowledge_topic: agent-systems
knowledge_units: [agent-measurement]
translation_of: /en/notes/how-agent-usage-should-be-measured/
---







<!doctype html>
<html lang="zh-CN">
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




      <link rel="alternate" hreflang="en" href="https://roy-tong.github.io/en/notes/how-agent-usage-should-be-measured/">
      <link rel="alternate" hreflang="zh-CN" href="https://roy-tong.github.io/notes/how-agent-usage-should-be-measured/">
      <link rel="alternate" hreflang="x-default" href="https://roy-tong.github.io/notes/how-agent-usage-should-be-measured/">
    <link type="application/atom+xml" rel="alternate" href="https://roy-tong.github.io/feed.xml" title="Roy.Tong"/>
    <!-- Begin Jekyll SEO tag v2.8.0 -->
<title>应该如何衡量人工智能代理的软件使用情况 | Roy.Tong</title>
<meta name="generator" content="Jekyll v3.9.5"/>
<meta property="og:title" content="应该如何衡量人工智能代理的软件使用情况">
<meta name="author" content="Roy.Tong"/>
<meta property="og:locale" content="zh_CN">
<meta name="description" content="随着软件消费者从人类转变为代理，经济单位从席位转变为可调用能力，测量先于支付。 AgentMeasure为CaaS提出了一个开放的测量基础——范围→选择→使用→效用→价值。">
<meta property="og:description" content="随着软件消费者从人类转变为代理，经济单位从席位转变为可调用能力，测量先于支付。 AgentMeasure为CaaS提出了一个开放的测量基础——范围→选择→使用→效用→价值。">
<link rel="canonical" href="https://roy-tong.github.io/notes/how-agent-usage-should-be-measured/">
<meta property="og:url" content="https://roy-tong.github.io/notes/how-agent-usage-should-be-measured/">
<meta property="og:site_name" content="Roy.Tong"/>
<meta property="og:image" content="https://roy-tong.github.io/assets/images/social-preview.png"/>
<meta property="og:type" content="article"/>
<meta property="article:published_time" content="2026-08-16T10:00:00+08:00"/>
<meta name="twitter:card" content="summary_large_image"/>
<meta property="twitter:image" content="https://roy-tong.github.io/assets/images/social-preview.png"/>
<meta property="twitter:title" content="应该如何衡量人工智能代理的软件使用情况">
<script type="application/ld+json">
{"@context":"https://schema.org","@type":"BlogPosting","author":{"@type":"Person","name":"Roy.Tong"},"dateModified":"2026-08-16T10:00:00+08:00","datePublished":"2026-08-16T10:00:00+08:00","description":"As the software consumer shifts from humans to agents and the economic unit from seats to callable capabilities, measurement precedes payment. AgentMeasure proposes an open measurement foundation for CaaS — Reach → Choice → Use → Utility → Value.","headline":"How Software Usage by AI Agents Should Be Measured","image":"https://roy-tong.github.io/assets/images/social-preview.png","mainEntityOfPage":{"@type":"WebPage","@id":"https://roy-tong.github.io/en/notes/how-agent-usage-should-be-measured/"},"publisher":{"@type":"Organization","logo":{"@type":"ImageObject","url":"https://roy-tong.github.io/assets/images/social-preview.png"},"name":"Roy.Tong"},"url":"https://roy-tong.github.io/en/notes/how-agent-usage-should-be-measured/"}</script>
<!-- End Jekyll SEO tag -->

  </head>
  <body>
    
    
    
    <a class="skip-link" href="#main">跳到内容</a>

    <header class="site-header">
      <div class="shell nav-wrap">
        <a class="brand" href="/en/" aria-label="返回主页">
          <span class="brand-mark">字母R</span>
          <span>罗伊·通</span>
        </a>

        <button class="menu-toggle" type="button" aria-expanded="false" aria-controls="site-navigation" aria-label="打开导航">
          <svg viewbox="0 0 24 24" aria-hidden="true">
            <path d="M4 7h16M4 12h16M4 17h16"/>
          </svg>
        </button>

        <nav class="nav" id="site-navigation" aria-label="主导航">
          
            <a href="/essays/">论文</a>
          
            <a href="/knowledge/">研究</a>
          
            <a href="/projects/">项目</a>
          
            <a href="/about/">关于</a>
          
            <a href="/support/">联系</a>
          
          <div class="nav-tools">
            <a class="language-toggle" href="/en/notes/how-agent-usage-should-be-measured/" hreflang="en" lang="en" data-language-switch data-target-language="en" aria-label="View in English" title="View in English">EN</a>
            <button class="theme-toggle" type="button" aria-pressed="false" aria-label="切换到黑暗模式" title="切换到黑暗模式">
              <svg class="theme-icon" viewbox="0 0 24 24" aria-hidden="true">
                <circle cx="12" cy="12" r="4"/>
                <path d="M12 2v2M12 20v2M4.93 4.93l1.42 1.42M17.65 17.65l1.42 1.42M2 12h2M20 12h2M4.93 19.07l1.42-1.42M17.65 6.35l1.42-1.42"/>
              </svg>
            </button>
          </div>
        </nav>
      </div>
    </header>

    <main id="main"><p class="translation-note" aria-label="翻译说明">机器辅助翻译。<a href="/en/notes/how-agent-usage-should-be-measured/">阅读英文原文</a>。</p>
      




<article class="post shell reading-shell">
  <header class="post-header">
    <a class="eyebrow back-link" href="/archive/">← 所有写作</a>
    <h1>应该如何衡量人工智能代理的软件使用情况</h1>
    <p class="post-subtitle">能力即服务和代理能力经济的衡量基础</p>
    <div class="post-meta">
      <time datetime="2026-08-16T10:00:00+08:00">2026年8月16日</time>
      <span>14分钟阅读</span>
      
      <a class="post-translation" href="/en/notes/how-agent-usage-should-be-measured/" hreflang="en">Read in English →</a>
      
        <span class="post-tags">
          <a href="/tags/#agent">#代理</a><a href="/tags/#measurement">#测量</a><a href="/tags/#capability%20economy">#能力经济</a><a href="/tags/#caas">#Caas</a>
        </span>
      
    </div>
  </header>

  <div class="prose">
    <p><em>白皮书v0.2 · 代理测量标准草案0.4</em></p>

<blockquote>
  <p>罗伊·汤

参考实现位于AgentMeasure存储库中。</p>
</blockquote>

<h2 id="0-abstract">0. 摘要</h2>

<p>人工智能代理越来越多地代表选择、调用和交易软件

用户和组织。 作为技能、MCP服务器、API和CLI等接口

创造和分发变得更加容易，经济价值越来越多地转向

它们背后的稀缺能力：专有数据、计算、执行，

权限、交易和现实世界的实现。</p>

<p>这在产生付款问题之前会产生测量问题。 一种能力

在生态系统同意之前，无法可靠地定价、比较、计费或优化

关于什么构成了选择、操作、成功交付、消费

结果、结果和计费单位。</p>

<p>AgentMeasure为这一新兴能力提出了一个开放的测量标准

经济：一种通用的数据语言——范围、选择、使用、效用、价值——加上

计量、市场和支付轨道以后可以构建的测量语义

上。 目标不是仪表板。 它是测量基础，使

能力作为一种服务（CaaS，如本文所用）是可能的。</p>

<h2 id="1-from-saas-to-capability-economy">1. 从SaaS到能力经济</h2>

<p>软件分发曾经有一个可读的链：下载、安装、使用。 每个的

时代有自己的经济单位。 下面描述的班次是<strong>添加剂，不是

替代</strong>：与基于座位的SaaS和基于请求的API一起，可调用

能力正在成为代理介导软件的新经济单位

消费。</p>

<div class="language-text highlighter-rouge"><div class="highlight"><pre class="highlight"><code>SaaS
Human → Application → Seat / Month

API Economy
Software → API → Request / Token

Capability Economy
Agent → Capability → Operation / Outcome
</code></pre></div></div>

<p>三股力量正在推动向第三排的转变。</p>

<p><strong>接口正在被代理吸收。</strong>用户界面和工作流程越来越

由代理人执行，没有呈现给人类。 软件剩下的是一个

可调用的表面——一个技能文件、一个MCP工具、一个CLI、一个端点。</p>

<p><strong>分销人工制品正在商品化。</strong>开放式技能、开放式 MCP 适配器、

开放CLI可以在几个小时内由任何人编写和发布。 接口可能会变成

制造成本低；交付能力仍然稀缺。</p>

<p><strong>稀缺性向下移动。</strong>稀缺层不再是应用程序外壳；它是

可调用表面控制访问的内容：</p>

<div class="language-text highlighter-rouge"><div class="highlight"><pre class="highlight"><code>Data · Compute · Action · Permission · Trust · Real-world fulfillment
</code></pre></div></div>

<p>搜索能力因其索引而稀缺；预订能力，因为它

可以确认预订；支付能力，因为它可以转移资金。 什么时候

商业价值集中在能力上，自然经济单位成为

操作、数量、效果、结果——或任何收入份额

他们。</p>

<p><strong>如果能力成为经济单位，能力测量就变成了

基础设施。</strong>这就是本文的论点。</p>

<h3 id="thesis-and-assumptions">论文和假设</h3>

<p>AgentMeasure建立在三个趋势判断之上<strong>尚未完全建立</strong>:</p>

<ol>
  <li>代理将调解越来越多的软件选择和执行。</li>
  <li>更多软件功能将独立于其人类用户界面而公开。</li>
  <li>基于使用、效果和结果的商业模式将与基于座位的商业模式共存

定价。</li>
</ol>

<p>即使这些趋势进展不平衡，测量标准仍然有用：

对象、质量规则和索赔纪律作为代理人独立

软件测量标准。</p>

<h2 id="2-measurement-before-monetization">2. 货币化前的测量</h2>

<p>在CaaS拥有定价、计费和声誉之前，它需要共同的测量

语义学。 四个问题表明了要点：</p>

<div class="language-text highlighter-rouge"><div class="highlight"><pre class="highlight"><code>One user task → 1 Operation → 3 retries
Charge 1 time or 3?

Tool returned successfully → Agent ignored the result
Was value delivered?

Booking API executed → reservation was never confirmed
Was the capability fulfilled?

Task succeeded → would it succeed without the capability?
Can the provider claim value?
</code></pre></div></div>

<p>这些问题都不能通过原始呼叫计数来回答，而且这些问题都不能

由支付铁路回答。 他们要求商定的定义<em>操作</em>, <em>努力</em>,
<em>交付</em>, <em>消耗</em>, <em>效果</em>和<em>结果</em>—并商定的转弯规则

对这些物体的观察。 那个协议是楔子：<strong>之前的测量

货币化</strong>.</p>

<h3 id="emerging-evidence-commerce-is-arriving-before-measurement">新出现的证据：商业在测量之前到达</h3>

<p>前提不是假设的——支付和发现基础设施

代理介导的商业已经存在：</p>

<ul>
  <li><strong>Cloudflare代理SDK</strong>允许MCP工具按通话定价，并通过

X402（<a href="https://developers.cloudflare.com/agents/agentic-payments/x402/charge-for-mcp-tools/">为 MCP 工具收费</a>).</li>
  <li><strong>Coinbase x402 集市</strong>是一个发现层，代理在其中搜索服务

价格和模式，以及通过MCP完成付费通话

（<a href="https://docs.cdp.coinbase.com/x402/bazaar">X402集市</a>).</li>
  <li><strong>OpenAI和Stripe的代理商业协议（ACP）</strong>正在实际使用

代理商业流动（<a href="https://www.digitaltransactions.net/openai-and-stripe-are-the-latest-fintechs-to-enable-agentic-commerce/">公告报道</a>).</li>
</ul>

<p>这些证明了本节的论点：<strong>支付和发现基础设施是

在通用能力测量语义之前到达</strong>— 差距代理测量

填充。</p>

<h2 id="3-measurement-objects">3. 测量对象</h2>

<p>观察是一个<em>证据单位</em>，不是一个<em>业务测量单位</em>。 代理测量

首先定义业务部门：</p>

<div class="language-text highlighter-rouge"><div class="highlight"><pre class="highlight"><code>Provider
    ↓
Software Entity
    ↓
Capability
    ↓
Interaction Surface
</code></pre></div></div>

<blockquote>
  <p><strong>能力是主要的功能和测量对象。 供品是

一种或多种能力的商业包装</strong>—在商业中定义

扩展（实验性），从未插入到核心测量系中。</p>
</blockquote>

<table>
  <thead>
    <tr>
      <th>对象</th>
      <th>定义</th>
      <th>层</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>软件实体</td>
      <td>被测量的软件：工具、技能、API、数据源、代理、应用程序、运行时能力</td>
      <td>市场</td>
    </tr>
    <tr>
      <td>能力</td>
      <td>实体的命名函数——主要功能和测量对象</td>
      <td>市场</td>
    </tr>
    <tr>
      <td>交互表面</td>
      <td>功能的可观察调用接口（mcp_tool、cli_command、http_endpoint、...）</td>
      <td>市场</td>
    </tr>
    <tr>
      <td>决策机会</td>
      <td>一个工具选择决定</td>
      <td>行为</td>
    </tr>
    <tr>
      <td>候选人集</td>
      <td>该决定中实际提供的套装</td>
      <td>行为</td>
    </tr>
    <tr>
      <td>展示</td>
      <td>在候选集合中出现的可选择</td>
      <td>行为</td>
    </tr>
    <tr>
      <td>选择</td>
      <td>经纪人选择一个可选择的</td>
      <td>行为</td>
    </tr>
    <tr>
      <td>操作</td>
      <td>一项任务能力的逻辑用途</td>
      <td>行为</td>
    </tr>
    <tr>
      <td>努力</td>
      <td>一次操作的执行（<strong>重试=多次尝试</strong>)</td>
      <td>行为</td>
    </tr>
    <tr>
      <td>结果/效果</td>
      <td>能力恢复了什么/世界上发生了什么变化</td>
      <td>行为</td>
    </tr>
    <tr>
      <td>工作</td>
      <td>业务所服务的工作单位</td>
      <td>行为</td>
    </tr>
    <tr>
      <td>顾客</td>
      <td>独立代理运行时/安装</td>
      <td>市场</td>
    </tr>
    <tr>
      <td>预测</td>
      <td>软件实体包/工具/技能汇总到</td>
      <td>市场</td>
    </tr>
    <tr>
      <td>范畴</td>
      <td>可比的能力等级（搜索、预订、...）</td>
      <td>市场</td>
    </tr>
    <tr>
      <td>观察</td>
      <td>测量事实的证据记录（认证和签名是可选的，由验证配置文件定义）</td>
      <td>证据</td>
    </tr>
  </tbody>
</table>

<p>观察发生在<strong>交互表面</strong>；归因解决为<strong>软件

实体</strong>通过机器可读的注册表——在观察时从未被猜到。</p>

<p>定价是故意的<strong>不</strong>核心模型的对象。 一个<code class="language-plaintext highlighter-rouge">Offering</code>—

参考一个或多个功能的商业包装，带有允许的表面，

定价政策、服务水平目标和商业约束——定义在

商业扩展（实验性、非规范性），因此测量

语义可以在不与任何支付设计相结合的情况下不断发展。</p>

<h3 id="distribution-events">分发事件</h3>

<p>随着商业归因的范围，发现重新获得了商业意义——没有

成为选择分母：</p>

<div class="language-text highlighter-rouge"><div class="highlight"><pre class="highlight"><code>Published → Listed → Retrieved / Discovered → Presented
</code></pre></div></div>

<p><code class="language-plaintext highlighter-rouge">Presented</code>仍然是选择指标的分母；<code class="language-plaintext highlighter-rouge">Discovered</code>是一个

分配-归因事件，回答<em>哪个技能/注册/市场

带来能力使用</em>.</p>

<h2 id="4-agentcapability-interaction-model">4. 代理-能力互动模型</h2>

<p><strong>到达→值是一个测量视图，而不是一个通用执行状态机器。</strong>不同类别的能力有不同的有意义的链：</p>

<div class="language-text highlighter-rouge"><div class="highlight"><pre class="highlight"><code>Information   Operation → Result → Consumption
Action        Operation → Effect → Confirmation
Transaction   Operation → Authorization → Commit / Settlement
</code></pre></div></div>

<p>交互类（信息/操作/交易/计算/

通信/控制/存储/传感）决定哪个链适用和

因此，哪些实用信号是有意义的。 搜索结果是<em>消耗的</em>；一个

预订是<em>坚定的</em>；付款是<em>持续不变的</em>。 迫使每个能力都通过一个

管道会产生意味着不同事物的数字。</p>

<h2 id="5-measurement-framework">5. 测量框架</h2>

<p>代理测量定义<strong>公制家族</strong>，不是通用的关键绩效指标。</p>

<p><strong>M1 分布 — Reach。</strong>是代理世界的能力吗？<code class="language-plaintext highlighter-rouge">Available Clients · Eligible Opportunities · Presentations · Presentation Rate ·
Distribution Coverage</code></p>

<p><strong>M2 Choice——最代理的原生家庭。</strong>当经纪人有机会时，做了吗

选择能力？<code class="language-plaintext highlighter-rouge">Selections · Observed Selection Rate (Observed Selected ÷ Presented) · Conditional
Choice Share · First-choice Rate</code></p>

<p><strong>M3执行——使用。</strong>选择后可以使用吗？ 草案0.4模型计数

操作和尝试分开——计量的区别最终会

需要：</p>

<div class="language-text highlighter-rouge"><div class="highlight"><pre class="highlight"><code>Operations · Attempts · Attempts per Operation
Operation Completion Rate · Operation Success Rate
Attempt Failure Rate · Retry Rate · Latency
</code></pre></div></div>

<p><strong>M4实用工具——有效使用。</strong>该功能是否提供了可用的信息或

引起预期效果？</p>

<div class="language-text highlighter-rouge"><div class="highlight"><pre class="highlight"><code>Result Utility      Delivered · Consumed · Accepted
Effect Utility      Applied · Confirmed · Reversed / Failed
</code></pre></div></div>

<p><strong>M5结果——价值。</strong>它改进了任务吗？<code class="language-plaintext highlighter-rouge">Task Success Association · Incremental Lift · Time Saved · Cost Saved</code></p>

<p><strong>关系</strong>（以前是单独的章节，现在是小节）：试用→活跃→

重复→首选→依赖。 依赖性——最不可替代的——仍然是

长期资产信号。</p>

<h2 id="6-measurement-quality--claim-discipline">6. 测量质量&amp;索赔纪律</h2>

<p>证据质量不是覆盖质量；两者都不是资格质量；没有

是方法论。 覆盖2%的代理的一组完全证实的事件不是

市场数据。</p>

<div class="language-text highlighter-rouge"><div class="highlight"><pre class="highlight"><code>Measurement Quality
├── Provenance / Evidence Strength   where did this observation come from, and how
│                                    strongly is its origin supported?
├── Coverage                         how much of the world did we see?
├── Qualification                    does this count as real production use?
├── Sampling                         sampled? with what uncertainty?
├── Identity                         how well do identifiers resolve to entities?
└── Method/version                   which statistics, which spec version?
</code></pre></div></div>

<p><strong>合格的使用。</strong>每个观察都带有两个轴——使用上下文（其中

流量来自）和有效性（观察结果是否真实）。<strong>严厉的

合格的使用</strong> = <code class="language-plaintext highlighter-rouge">production</code> + <code class="language-plaintext highlighter-rouge">validity=normal</code>：公共指标的默认值。

未知的上下文/有效性单独披露，从未默含——不

“报告未知→制作排行榜”激励。 重试是额外的尝试

相同的操作，作为可靠性信号保留，而不是作为不同的逻辑用途。</p>

<p><strong>要求纪律。</strong>每个已发布的指标都带有测量标签：分子，

分母，可观察人口，合格人口，运行时间覆盖，谷物，

选择模式、决策权、选择约束。 观察到的选择从来都不是

呈现为偏好；关联从未呈现为因果关系；无法观察到的是

从未被解释为负面的。</p>

<h2 id="7-measurement-and-metering">7. 测量和计量</h2>

<p>从测量标准到CaaS的桥梁是语义的：<strong>测量单位≠

计费单位</strong>，三个计量概念必须分开——<strong>活动</strong>是

为什么账单触发，<strong>单位</strong>是被计算在内的东西，<strong>数</strong>有多少：</p>

<table>
  <thead>
    <tr>
      <th>能力</th>
      <th>计费_事件</th>
      <th>计费_单位</th>
      <th>计费_数量</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>搜索</td>
      <td><code class="language-plaintext highlighter-rouge">operation_succeeded</code></td>
      <td>操作</td>
      <td>1</td>
    </tr>
    <tr>
      <td>数据</td>
      <td><code class="language-plaintext highlighter-rouge">result_delivered</code></td>
      <td>最高纪录</td>
      <td>1,382</td>
    </tr>
    <tr>
      <td>计算</td>
      <td><code class="language-plaintext highlighter-rouge">compute_completed</code></td>
      <td>Gpu_秒</td>
      <td>47.2</td>
    </tr>
    <tr>
      <td>情节</td>
      <td><code class="language-plaintext highlighter-rouge">effect_confirmed</code></td>
      <td>操作</td>
      <td>1</td>
    </tr>
    <tr>
      <td>预约</td>
      <td><code class="language-plaintext highlighter-rouge">effect_confirmed</code></td>
      <td>预约</td>
      <td>1</td>
    </tr>
    <tr>
      <td>线索生成</td>
      <td><code class="language-plaintext highlighter-rouge">outcome_qualified</code></td>
      <td>合格的_领导</td>
      <td>5</td>
    </tr>
    <tr>
      <td>贸易</td>
      <td><code class="language-plaintext highlighter-rouge">transaction_settled</code></td>
      <td>交易</td>
      <td>0.03（收入份额）</td>
    </tr>
  </tbody>
</table>

<p>因此，计量语义定义，根据产品：</p>

<div class="language-text highlighter-rouge"><div class="highlight"><pre class="highlight"><code>Billable Event       which measured fact triggers a charge
Billable Unit        the unit of quantity (operation, record, GPU-second, effect…)
Billable Quantity    how the unit is counted (per policy: attempts, confirmations…)
Pricing Model        per-operation · per-quantity · per-effect · per-outcome · revenue share
Pricing Policy       versioned price rules (flat, volume tiers, enterprise agreement, surge…)
Quote                the terms actually applicable to one call (quote_id, policy version, unit price)
Metering Policy      how measurement facts map to billable facts (rules, exclusions), versioned
Metering Ledger      replayable, correctable record of metered facts (revision / supersedes / reversal)
Commercial Attribution  which parties contributed to discovery / selection / revenue
</code></pre></div></div>

<p><strong>付款超出了范围。</strong>AgentMeasure没有定义支付栏、钱包，

结算货币、记录商家关系或金融托管。 它

产生事实——合格的操作、确认的效果、合格的结果，

计费数量，商业归因——支付系统消耗。</p>

<blockquote>
  <p><strong>AgentMeasure规范经济事实，而不是货币流动。</strong></p>
</blockquote>

<h2 id="8-attribution-and-incrementality">8. 归因和增量</h2>

<p><strong>能力参与成功任务并不能证明它造成了

成功。</strong></p>

<ul>
  <li><strong>归因测量</strong>是观察性的：哪些能力参与了

任务链。 它支持索赔<em>协会</em>和<em>贡献

执行链</em>—没有更多。</li>
  <li><strong>增量测量</strong>是反事实：有多少额外价值

能力创造？ 随机比较是最有力的证据，但许多

功能不能随机关闭。 因此，索赔遵循一个<strong>价值

证据梯子</strong>:</li>
</ul>

<div class="language-text highlighter-rouge"><div class="highlight"><pre class="highlight"><code>V0 Association             participated when the task succeeded
V1 Matched / Observational known confounders controlled
V2 Offline Ablation        replay tasks with the capability removed
V3 Quasi-experiment        switchback / natural variation
V4 Randomized Holdout      strongest causal evidence
</code></pre></div></div>

<p>只有实际提出的证据才能支持相应的因果主张

强度——与测量质量相同的学科。</p>

<p>商业归因沿着分销链扩展了观察面：</p>

<div class="language-text highlighter-rouge"><div class="highlight"><pre class="highlight"><code>GitHub Skill → Registry → Agent Recommendation → Capability → Payment
</code></pre></div></div>

<p>谁为发现、选择和收入做出了贡献？ 这是未来的基础

代理附属和收入分享模式——绝不能将其与

因果递增性。</p>

<h2 id="9-capability-trust-and-comparability">9. 能力信任和可比性</h2>

<p>能力消费者的选择是由许多因素决定的。 代理商和市场

可以越来越多地比较机器可读的性能信号<strong>在...旁边</strong>品牌，

政策、价格、用户偏好和平台约束——正是轴心

AgentMeasure的决策权限/选择约束模型描述了：</p>

<div class="language-text highlighter-rouge"><div class="highlight"><pre class="highlight"><code>Capability Signals
Reliability · Latency · Price · Freshness · Consumption · Effect Success
Outcome · Safety · Measurement Coverage
</code></pre></div></div>

<p>代理测量<strong>不计算通用代理测量分数</strong>。 代理人A关心

关于价格，代理B关于延迟，代理C关于隐私。 排名是一种产品

代理商和市场的决定；该标准只定义可比信号

以及使它们可比的标签。 测量标签是基础

这个可比性。</p>

<h2 id="10-observation--deployment-architecture">10. 观察&amp;部署架构</h2>

<p>测量表面在它们能看到的东西上有所不同；单面采用是有价值的，

但声明必须与表面相符：</p>

<div class="language-text highlighter-rouge"><div class="highlight"><pre class="highlight"><code>Distribution Side → Agent Runtime Side → Provider Side → Effect / Outcome Side
</code></pre></div></div>

<table>
  <thead>
    <tr>
      <th>表面</th>
      <th>可以看到</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>登记处</td>
      <td>发现/可用性</td>
    </tr>
    <tr>
      <td>代理运行时间</td>
      <td>演示/选择/消费</td>
    </tr>
    <tr>
      <td>能力提供者</td>
      <td>操作/尝试/结果</td>
    </tr>
    <tr>
      <td>目标系统</td>
      <td>效果/交易</td>
    </tr>
    <tr>
      <td>实验层</td>
      <td>增量</td>
    </tr>
  </tbody>
</table>

<p>双面观察（代理运行时间+提供程序）可实现佐证实（E2）；

仅提供商端就足以满足提供商范围的使用指标。 标准是

不在关键请求路径上：观察是非同步发出的，元数据

只有，在坚持之前被假名化。</p>

<h2 id="11-interoperability">11. 互操作性</h2>

<p>标准是运输中立和供应商中立。 当前基础设施绑定

将其作为实现示例，而不是作为先决条件：MCP承载生命周期事件

和跟踪上下文；OpenTelemetry携带工具跨度；Codex、Claude Code和DeepSeek

使用声明的能力矩阵的线束暴露观察点；注册表

提供实体身份。 支付轨道，当它们到达时，会消耗标准的

事实，而不是扩展其核心。</p>

<h2 id="12-non-goals-and-governance">12. 非目标和治理</h2>

<p>代理测量是<strong>不</strong>支付协议、市场、钱包或通用

声誉系统。 该标准不：</p>

<ul>
  <li>转移资金或托管资金；</li>
  <li>排名能力或评分提供者；</li>
  <li>定义什么是“好”能力；</li>
  <li>需要任何中央服务器、代理端安装或开源提供商。</li>
</ul>

<p>标准本身是社区管理的（AUP流程，<code class="language-plaintext highlighter-rouge">proposals/</code>）；商业的

基于它构建的产品不得控制标准的定义。</p>

<h2 id="13-open-questions">13. 开放式问题</h2>

<ol>
  <li><strong>任务边界。</strong>“任务”的单位是什么，谁来定义它？</li>
  <li><strong>效果验证。</strong>如何确认效果（预订确认，付款

解决）没有深度整合到每个目标系统中？</li>
  <li><strong>规模的增量。</strong>如何在...上进行反事实实验

不干扰生产的生态系统？</li>
  <li><strong>候选集的可观察性。</strong>演讲是关键分母；大多数

运行时尚未暴露它。</li>
  <li><strong>跨代理身份。</strong>Codex、Claude和DSH的同一客户——什么时候

可以知道吗？</li>
  <li><strong>计费单位共识。</strong>哪些测量事实将提供商和付款

轨道实际上达成了一致，测量错误的代价是什么？</li>
  <li><strong>隐私。</strong>在假名下，相关性和保留能走多远？</li>
</ol>

<h2 id="14-conclusion">14. 缔结</h2>

<p>软件消费者正在从人类转变为代理，而经济单位是

从座位转变为可呼叫能力。 在能力定价之前，

账单和比较，生态系统需要一种共享的测量语言——什么

选择是，什么是操作，什么是交付，什么是消费，什么是效果和

结果是，哪些数字可以支持哪些结论。</p>

<p>代理测量是那个提案：测量语义作为基础设施，商业

语义是未来的延伸，支付是别人的轨道。<strong>衡量如何

代理今天使用软件功能；使功能具有可比性和可衡量性

接下来；为长期的能力即服务建立衡量基础

术语。</strong></p>

<h2 id="references">参考资料</h2>

<ol>
  <li>RFC 2119 / BCP 14 —<em>RFC中用于指示要求级别的关键词</em>.</li>
  <li>OpenTelemetry GenAI语义约定——<code class="language-plaintext highlighter-rouge">gen_ai.*</code>工具呼叫遥测字段。</li>
  <li>模型上下文协议（MCP）规范——工具发现和调用表面。</li>
  <li>MCP注册表——服务器身份作为实体解析的入口点。</li>
  <li>EDPB——关于假名化的指导（假名化的数据可能仍然是个人数据）。</li>
  <li>Cloudflare —<a href="https://developers.cloudflare.com/agents/agentic-payments/x402/charge-for-mcp-tools/">MCP 工具收费（x402/代理付款）</a>.</li>
  <li>Coinbase —<a href="https://docs.cdp.coinbase.com/x402/bazaar">X402集市：发现&amp;支付超过MCP</a>.</li>
  <li>OpenAI / Stripe — 代理商业协议（ACP），于2025年9月宣布；见<a href="https://www.digitaltransactions.net/openai-and-stripe-are-the-latest-fintechs-to-enable-agentic-commerce/">数字交易覆盖范围</a>.</li>
  <li>AgentMeasure规范——核心、指标、数据、实体、质量、相关性

（<code class="language-plaintext highlighter-rouge">standard/</code>）；商业扩展（<code class="language-plaintext highlighter-rouge">extensions/COMMERCIAL.md</code>，实验）；

机器可读的注册表（<code class="language-plaintext highlighter-rouge">schemas/</code>, <code class="language-plaintext highlighter-rouge">registry/</code>）；参考实施和

同一存储库中的一致性向量。</li>
</ol>

<hr/>

<p><em>规范规范（测量对象、生命周期、公制家族、

质量、报告）和参考实施（AgentMeasure）已发布

公开地。 升级到AgentMeasure 1.0需要两个独立的实现，三个

运行时配置文件，两个工具端实现，一个公共一致性套件

规范测试向量，5-10个真实项目，已发布的差异报告，以及

安全和隐私审查。</em></p>

  </div>

  

<aside class="kb-related" aria-label="相关研究材料">
  <h2>相关研究材料</h2>
  <p>在研究图书馆中探索相关报告、数据摘要和笔记。 这些链接显示了主题联系；文章本身引用了直接证据。</p>
  
  <ul></ul>
  <ul>
    <li><a href="/knowledge/agent-measurement/">Agent 计量：执行事实、任务结果与价值</a></li>
  </ul>
  <a class="kb-text-link" href="/knowledge/">探索研究图书馆→</a>
</aside>



  <footer class="post-end">
    <span class="post-end-mark">字母R</span>
    <div class="post-end-copy">
      
        <strong>感谢您的阅读。</strong>
        <p>我一直在写关于人工智能、产品和从头开始建造东西的文章。</p>
      
    </div>
    
      <a class="support-link" href="/support/#tip">支持写作<span>♡</span></a>
    
  </footer>
<aside class="kb-related" aria-label="相关研究资料"><h2>相关研究资料</h2><p>报告、数据与笔记保留在资料库里，可继续查阅。文章直接使用的证据，以正文引用为准。</p><a class="kb-text-link" href="/knowledge/">查阅全部研究资料 →</a></aside>
</article>

    </main>

    <footer class="site-footer">
      <div class="shell footer-grid">
        <div>
          <p class="footer-title">罗伊·通</p>
          <p>人工智能如何成为产品、系统和市场。</p>
        </div>
        <div class="footer-links">
          
            <a href="/knowledge/">研究图书馆</a>
          
            <a href="/capability-index/">能力指数</a>
          
            <a href="https://github.com/roy-tong/verovo">维罗沃</a>
          
            <a href="https://x.com/elliwoodtong" rel="me">X/推特</a>
          
            <a href="https://github.com/roy-tong" rel="me">GitHub</a>
          
            <a href="/support/">联系</a>
          
            <a href="/feed.xml">RSS</a>
          
        </div>
      </div>
      <div class="shell footer-bottom">
        <span>© 2026 Roy.Tong</span>
        <span>事实、判断、实验和修改。</span>
      </div>
    </footer>

    <script src="/assets/js/main.js?v=20261124-1"></script>
    
  </body>
</html>
