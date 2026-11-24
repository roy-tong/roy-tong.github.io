---
title: "Askovo：产品研究需要一个类型系统，而不是一个信心分数"
date: "2026-11-24 12:02:00 +0800"
description: "Orthogonal evidence qualification, structural transaction checks, conclusion gates, and hash-bound research handoffs."
permalink: "/notes/04-askovo-product-research-needs-a-type-system/"
content_id: 04-askovo-product-research-needs-a-type-system
knowledge_topic: product-research
knowledge_units: [demand-evidence, research-workflows]
translation_of: /en/notes/04-askovo-product-research-needs-a-type-system/
lang: zh-CN
tags: [AI Agent]
generated_translation: true
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




      <link rel="alternate" hreflang="en" href="https://roy-tong.github.io/en/notes/04-askovo-product-research-needs-a-type-system/">
      <link rel="alternate" hreflang="zh-CN" href="https://roy-tong.github.io/notes/04-askovo-product-research-needs-a-type-system/">
      <link rel="alternate" hreflang="x-default" href="https://roy-tong.github.io/notes/04-askovo-product-research-needs-a-type-system/">
    <link type="application/atom+xml" rel="alternate" href="https://roy-tong.github.io/feed.xml" title="Roy.Tong"/>
    <!-- Begin Jekyll SEO tag v2.8.0 -->
<title>Askovo：产品研究需要一个类型系统，而不是一个信心分数 | Roy.Tong</title>
<meta name="generator" content="Jekyll v3.9.5"/>
<meta property="og:title" content="Askovo：产品研究需要一个类型系统，而不是一个信心分数">
<meta name="author" content="Roy.Tong"/>
<meta property="og:locale" content="zh_CN">
<meta name="description" content="Orthogonal evidence qualification, structural transaction checks, conclusion gates, and hash-bound research handoffs."/>
<meta property="og:description" content="Orthogonal evidence qualification, structural transaction checks, conclusion gates, and hash-bound research handoffs."/>
<link rel="canonical" href="https://roy-tong.github.io/notes/04-askovo-product-research-needs-a-type-system/">
<meta property="og:url" content="https://roy-tong.github.io/notes/04-askovo-product-research-needs-a-type-system/">
<meta property="og:site_name" content="Roy.Tong"/>
<meta property="og:image" content="https://roy-tong.github.io/assets/images/social-preview.png"/>
<meta property="og:type" content="article"/>
<meta property="article:published_time" content="2026-11-24T12:02:00+08:00"/>
<meta name="twitter:card" content="summary_large_image"/>
<meta property="twitter:image" content="https://roy-tong.github.io/assets/images/social-preview.png"/>
<meta property="twitter:title" content="Askovo：产品研究需要一个类型系统，而不是一个信心分数">
<script type="application/ld+json">
{"@context":"https://schema.org","@type":"BlogPosting","author":{"@type":"Person","name":"Roy.Tong"},"dateModified":"2026-11-24T12:02:00+08:00","datePublished":"2026-11-24T12:02:00+08:00","description":"Orthogonal evidence qualification, structural transaction checks, conclusion gates, and hash-bound research handoffs.","headline":"Askovo: product research needs a type system, not a confidence score","image":"https://roy-tong.github.io/assets/images/social-preview.png","mainEntityOfPage":{"@type":"WebPage","@id":"https://roy-tong.github.io/en/notes/04-askovo-product-research-needs-a-type-system/"},"publisher":{"@type":"Organization","logo":{"@type":"ImageObject","url":"https://roy-tong.github.io/assets/images/social-preview.png"},"name":"Roy.Tong"},"url":"https://roy-tong.github.io/en/notes/04-askovo-product-research-needs-a-type-system/"}</script>
<!-- End Jekyll SEO tag -->

  </head>
  <body>
    
    
    
    <a class="skip-link" href="#main">跳到内容</a>

    <header class="site-header">
      <div class="shell nav-wrap">
        <a class="brand" href="/" aria-label="返回主页">
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
            <a class="language-toggle" href="/en/notes/04-askovo-product-research-needs-a-type-system/" hreflang="en" lang="en" data-language-switch data-target-language="en" aria-label="切换至中文" title="切换至中文">中文</a>
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

    <main id="main"><p class="translation-note" aria-label="翻译说明">机器辅助翻译。<a href="/en/notes/04-askovo-product-research-needs-a-type-system/">阅读英文原文</a>。</p>
      




<article class="post shell reading-shell">
  <header class="post-header">
    <a class="eyebrow back-link" href="/archive/">← 所有写作</a>
    <h1>Askovo：产品研究需要一个类型系统，而不是一个信心分数</h1>
    <p class="post-subtitle">正交证据资格、结构性交易检查、结论门和哈希约束研究交接。</p>
    <div class="post-meta">
      <time datetime="2026-11-24T12:02:00+08:00">2026年11月24日</time>
      <span>7分钟阅读</span>
      
      <a class="post-translation" href="/en/notes/04-askovo-product-research-needs-a-type-system/" hreflang="en">Read in English →</a>
      
        <span class="post-tags">
          <a href="/tags/#ai%20agent">#人工智能代理</a>
        </span>
      
    </div>
  </header>

  <div class="prose">
    <p>GitHub API响应可以确认存储库有220颗星。 相同的回复无法确认有220人使用该产品，将为该产品付费，或因此做出了产品决定。</p>

<p>现在想象一下，记录标记了这个观察结果<code class="language-plaintext highlighter-rouge">E5</code>，系统中最高的证据水平。 标量置信分数没有解释问题的好方法。 观察结果可能非常准确，但仍然是商业结论的错误类型。</p>

<p>Askovo通过将证据资格处理为三个相关但正交的维度来处理这个问题：</p>

<div class="language-text highlighter-rouge"><div class="highlight"><pre class="highlight"><code>measurement_integrity  → is the record itself confirmed, self-reported, unverified, or conflicted?
behavior_kind          → what kind of behavior does the record describe?
claim_eligibility      → which conclusion type may this record support?
</code></pre></div></div>

<p>前两个本身并不能决定第三个。 它们通过明确的规则，其中一些需要人工审查。 这更接近于类型系统而不是分数：一种类型的有效观察不能仅仅因为它可靠就被迫成为无关索赔的证据。</p>

<h2 id="the-qualification-rules-are-deliberately-non-monotonic">资格规则故意不单调</h2>

<p>奔跑<code class="language-plaintext highlighter-rouge">qualify_evidence</code>在具有已确认的来源和断言的E5水平返回的注意力指标上：</p>

<div class="language-json highlighter-rouge"><div class="highlight"><pre class="highlight"><code><span class="p">{</span><span class="w">
  </span><span class="nl">"measurement_integrity"</span><span class="p">:</span><span class="w"> </span><span class="s2">"confirmed_source"</span><span class="p">,</span><span class="w">
  </span><span class="nl">"behavior_kind"</span><span class="p">:</span><span class="w"> </span><span class="s2">"attention_metric"</span><span class="p">,</span><span class="w">
  </span><span class="nl">"claim_eligibility"</span><span class="p">:</span><span class="w"> </span><span class="s2">"descriptive_only"</span><span class="p">,</span><span class="w">
  </span><span class="nl">"needs_requalification"</span><span class="p">:</span><span class="w"> </span><span class="kc">true</span><span class="p">,</span><span class="w">
  </span><span class="nl">"review_required"</span><span class="p">:</span><span class="w"> </span><span class="kc">false</span><span class="w">
</span><span class="p">}</span><span class="w">
</span></code></pre></div></div>

<p>原始的<code class="language-plaintext highlighter-rouge">evidence_level=E5</code>没有重写。 相反，该记录被标记为重新认证。 保留冲突很重要：默默地改变水平将抹去错误如何进入研究的历史。</p>

<p>资格功能不是“更高的诚信意味着更高的商业证据”。 它的分支机构包括：</p>

<table>
  <thead>
    <tr>
      <th>行为</th>
      <th>已确认的来源</th>
      <th>自我报告的</th>
      <th>未经验证或冲突</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td><code class="language-plaintext highlighter-rouge">attention_metric</code></td>
      <td><code class="language-plaintext highlighter-rouge">descriptive_only</code></td>
      <td><code class="language-plaintext highlighter-rouge">none</code></td>
      <td><code class="language-plaintext highlighter-rouge">none</code></td>
    </tr>
    <tr>
      <td><code class="language-plaintext highlighter-rouge">commercial_intent</code></td>
      <td><code class="language-plaintext highlighter-rouge">descriptive_only</code></td>
      <td><code class="language-plaintext highlighter-rouge">descriptive_only</code></td>
      <td><code class="language-plaintext highlighter-rouge">none</code></td>
    </tr>
    <tr>
      <td><code class="language-plaintext highlighter-rouge">commercial_transaction</code></td>
      <td><code class="language-plaintext highlighter-rouge">commercial</code></td>
      <td><code class="language-plaintext highlighter-rouge">none</code>加上评论</td>
      <td><code class="language-plaintext highlighter-rouge">none</code>加上适用时的审查</td>
    </tr>
    <tr>
      <td><code class="language-plaintext highlighter-rouge">problem_behavior</code></td>
      <td><code class="language-plaintext highlighter-rouge">problem</code></td>
      <td><code class="language-plaintext highlighter-rouge">problem</code></td>
      <td><code class="language-plaintext highlighter-rouge">none</code></td>
    </tr>
    <tr>
      <td><code class="language-plaintext highlighter-rouge">solution_acceptance</code></td>
      <td><code class="language-plaintext highlighter-rouge">solution</code></td>
      <td><code class="language-plaintext highlighter-rouge">solution</code></td>
      <td><code class="language-plaintext highlighter-rouge">none</code></td>
    </tr>
    <tr>
      <td>普通陈述</td>
      <td><code class="language-plaintext highlighter-rouge">descriptive_only</code></td>
      <td><code class="language-plaintext highlighter-rouge">none</code></td>
      <td><code class="language-plaintext highlighter-rouge">none</code></td>
    </tr>
  </tbody>
</table>

<p>精确的星星计数仍然很有用——作为一个注意力指标。 自我报告的购买意向可以描述需求语言，而不会成为交易。 没有可核实来源的索赔付款不会仅仅因为索赔人使用了“已支付”一词而成为商业证据。</p>

<p>推导还消耗特定于源的字段。 经过验证的购买和交易关联状态可以确认商业交易；认捐或调整的众筹状态描述商业意图；跟踪器、资金和评级快照是关注度指标。 这使词汇与来源实际测量的内容保持一致。</p>

<h2 id="evidence-levels-still-matter-but-imports-have-structural-ceilings">证据水平仍然很重要，但进口有结构性上限</h2>

<p>Askovo保留了E0-E5等级，用于更广泛的研究方法。 导入层通过证据形式应用单独的上限：</p>

<div class="language-python highlighter-rouge"><div class="highlight"><pre class="highlight"><code><span class="n">IMPORT_LEVEL_CAPS</span> <span class="o">=</span> <span class="p">{</span>
    <span class="s">"self_report"</span><span class="p">:</span> <span class="s">"E2"</span><span class="p">,</span>
    <span class="s">"behavior_log"</span><span class="p">:</span> <span class="s">"E2"</span><span class="p">,</span>
    <span class="s">"transaction"</span><span class="p">:</span> <span class="s">"E5"</span><span class="p">,</span>
    <span class="s">"purchase"</span><span class="p">:</span> <span class="s">"E5"</span><span class="p">,</span>
<span class="p">}</span>
</code></pre></div></div>

<p>自我报告或行为日志不能在E3接受或E4+/E5商业级别导入。 如果请求的级别超过表格的上限，文件将被拒绝。 行不能将其级别提高到为导入声明的上限之上，混合行保留每行的衍生级别。</p>

<p>在允许E4-/E4+/E5之前，交易和购买表格需要额外的结构：</p>

<div class="language-text highlighter-rouge"><div class="highlight"><pre class="highlight"><code>counterparty
occurred_at
amount
source_ref
evidence_ref
</code></pre></div></div>

<p>默认值不填写这些字段。 如果缺少任何，该行将保留在E2和<code class="language-plaintext highlighter-rouge">level_basis</code>记录规则：</p>

<div class="language-text highlighter-rouge"><div class="highlight"><pre class="highlight"><code>transaction structure incomplete: missing counterparty, amount; E5 held at E2
</code></pre></div></div>

<p>这会产生两种不同的故障行为，容易混淆：</p>

<ul>
  <li>请求E5的导入自我报告未能通过导入政策检查；</li>
  <li>请求E5的交易表单行可以进入管道，但不完整的行在结构上被降级为E2。</li>
</ul>

<p>命令的<code class="language-plaintext highlighter-rouge">--evidence-form transaction</code>因此，旗帜不是凭证。 它只选择真实交易记录必须满足的规则。 当我为这篇文章运行它们时，15个导入和结论门测试通过了，包括每个缺失的交易字段、混合行、未知级别和声称是交易的纯文本。</p>

<h2 id="source-count-is-not-independent-source-count">来源计数不是独立的来源计数</h2>

<p>定量研究还有另一个胁迫性问题：1000条复制的记录看起来比一条记录大。 Askovo用单独的身份密钥计算独立源：</p>

<div class="language-text highlighter-rouge"><div class="highlight"><pre class="highlight"><code>source_url, if present
→ otherwise collection_run_id + source_ref
→ otherwise record_id / normalized_text_hash / object identity fallback
</code></pre></div></div>

<p>独立源计数是该键集的基数。 在500条记录中重复的一个URL仍然是一个来源。 这并没有使这500条记录变得无用；频率、分发和文本分析仍然很重要。 它防止记录量伪装成独立的佐证实。</p>

<p>这种区别在内部高尔夫设备研究中至关重要，通常用于说明Askovo。 它在24个月内分析了来自八个社区的109,429个重复评论，并将拟议的序列从专用相机硬件更改为首先验证软件和出口。 语料库是一个方便样本。 它的规模支持对该语料库的定量分析，而不是市场流行率估计或109,429个独立确认。</p>

<p>类型感知阅读会对同一数据提出更好的问题：哪些记录描述了当前行为，哪些记录描述了接受，哪些是反例，哪些只是注意力指标，哪些来源是真正不同的？</p>

<h2 id="the-formal-conclusion-gate-is-separate-from-node-confidence">正式结论门与节点置信是分开的</h2>

<p>Askovo在其MCP模式中公开了六个索赔类别：<code class="language-plaintext highlighter-rouge">need</code>, <code class="language-plaintext highlighter-rouge">acceptance</code>, <code class="language-plaintext highlighter-rouge">usability</code>, <code class="language-plaintext highlighter-rouge">performance</code>, <code class="language-plaintext highlighter-rouge">commercial</code>，还有<code class="language-plaintext highlighter-rouge">safety</code>。 他们不应该共享一个接受标准。 面试可能支持需求而不证明性能；点击可能描述可用性而不确定定价；供应商断言不能确定安全性。</p>

<p>交付层增加了最后一个门，用于将某事称为正式业务结论：</p>

<div class="language-text highlighter-rouge"><div class="highlight"><pre class="highlight"><code>business node is validated
+ qualifying E4+/E5 commercial evidence is present
+ full audit passes
= formal conclusion
</code></pre></div></div>

<p>否则，输出仍然是当前的判断，有命名的差距和下一个证据行动。 没有商业证据的经过验证的业务节点仍然被门禁。 干净的商业记录无法挽救失败的全面审计。 多个链是独立评估的，因此一个支持良好的链不能将其地位借给另一个链。</p>

<p>这个门比单个节点的显示状态更严格，而且是故意的。 产品团队可以使用当前的判断来决定下一步要调查什么，而无需将其作为商业证据。</p>

<h2 id="context-export-is-a-type-preserving-handoff">上下文导出是一种类型保存的交接</h2>

<p>移交给Growovo引入了一种不同的故障模式：研究场所到达下游，看起来像经过验证的事实。 Askovo的上下文导出器将七个链节点中的每一个映射到三个状态之一：</p>

<div class="language-python highlighter-rouge"><div class="highlight"><pre class="highlight"><code><span class="k">if</span> <span class="n">node_status</span> <span class="o">==</span> <span class="s">"validated"</span> <span class="ow">and</span> <span class="n">evidence_refs</span> <span class="ow">and</span> <span class="ow">not</span> <span class="n">unresolved_refs</span><span class="p">:</span>
    <span class="n">status</span> <span class="o">=</span> <span class="s">"evidence_supported"</span>
<span class="k">elif</span> <span class="n">node_status</span> <span class="o">==</span> <span class="s">"hypothesis"</span><span class="p">:</span>
    <span class="n">status</span> <span class="o">=</span> <span class="s">"hypothesis"</span>
<span class="k">else</span><span class="p">:</span>
    <span class="n">status</span> <span class="o">=</span> <span class="s">"insufficient_evidence"</span>
</code></pre></div></div>

<p>缺少证据ID的经过验证的节点被降级为<code class="language-plaintext highlighter-rouge">insufficient_evidence</code>。 被拒绝和被取消优先级的节点也仍然是事实。 一个没有外部引用的节点得到一个<code class="language-plaintext highlighter-rouge">status_record_only</code>参考它自己的推理记录，这显然不是外部研究证据。</p>

<p>出口需要三个人类定义的输入：</p>

<ul>
  <li><code class="language-plaintext highlighter-rouge">--approved-by</code>，因为转发研究场所是一种批准行为；</li>
  <li>至少一个<code class="language-plaintext highlighter-rouge">--value-event</code>，因为Askovo无法发明下游价值指标；</li>
  <li>至少一个非目标，要么已经在产品/业务节点中声明，要么提供<code class="language-plaintext highlighter-rouge">--non-goal</code>.</li>
</ul>

<p>命令是：</p>

<div class="language-bash highlighter-rouge"><div class="highlight"><pre class="highlight"><code>askovo context <span class="nb">export </span>STUDY <span class="nt">--out</span> NEW_DIR <span class="se">\</span>
  <span class="nt">--approved-by</span> <span class="s2">"Product owner"</span> <span class="se">\</span>
  <span class="nt">--value-event</span> <span class="s2">"A product owner records a decision disposition"</span>
</code></pre></div></div>

<p>它写入两个不可变的文件：</p>

<div class="language-text highlighter-rouge"><div class="highlight"><pre class="highlight"><code>&lt;context_id&gt;.&lt;version&gt;.payload.json  # claims, evidence refs, value events, non-goals
&lt;context_id&gt;.&lt;version&gt;.json         # same payload + source ref + content_sha256
</code></pre></div></div>

<p>默认版本是<code class="language-plaintext highlighter-rouge">reasoning-&lt;first 12 hex of the reasoning file SHA-256&gt;</code>。 有效载荷使用排序的密钥进行序列化，信封的<code class="language-plaintext highlighter-rouge">content_sha256</code>哈希那些确切的字节。 Growovo在导入过程中重新计算有效负载哈希，因此两个文件必须保持在原始路径上。 重新导出同一版本拒绝覆盖任一文件；如果信封创建失败，新创建的有效负载将被删除。</p>

<p>我在合成样品上运行了出口商，然后故意将一个产品节点更改为<code class="language-plaintext highlighter-rouge">validated</code>有一个不存在的证据ID和一个业务节点<code class="language-plaintext highlighter-rouge">hypothesis</code>。 由此产生的预测是：</p>

<div class="language-text highlighter-rouge"><div class="highlight"><pre class="highlight"><code>total:                7
evidence_supported:   5
hypothesis:           1
insufficient_evidence: 1

PR01:product
  status: insufficient_evidence
  unresolved: ["missing-evidence-id"]

PR01:business
  status: hypothesis
</code></pre></div></div>

<p>这是重要的交接行为。 突变的产品节点仍然说<code class="language-plaintext highlighter-rouge">validated</code>在源头，但下游收到一个未解决的证据缺口，而不是升级的索赔。</p>

<h2 id="a-second-use-should-preserve-the-same-distinctions">第二次使用应该保持相同的区别</h2>

<p>第二个决定或研究审查只有在保留这些类型边界时才有用。 新的GitHub指标应该仍然是注意力观察。 新交易应该带来其行级结构和来源。 复制的URL不应对独立的佐证实进行。 更改后的证据引用应该产生一个新的推理版本和不同的交接哈希。</p>

<p>这赋予了二次使用测量的具体形状：</p>

<ul>
  <li>计算新的和删除的独立来源；</li>
  <li>比较资格分布，而不仅仅是证据总数；</li>
  <li>保留重新资格冲突以供人力审查；</li>
  <li>比较导出的有效负载中的声明状态；</li>
  <li>记录哪些结论仍然是当前的判断；</li>
  <li>记录业主的实际处置和审查会议记录。</li>
</ul>

<p>工程权衡是Askovo同时保持几个“好证据”的概念。 这比显示一个置信百分比需要更多的工作。 它还使该系统更难被滥用为通用答案生成器。 最容易阅读的分数通常是隐藏类型错误的分数。</p>

<h3 id="source-and-verification-links">来源和验证链接</h3>

<ul>
  <li><a href="https://github.com/roy-tong/Askovo/blob/main/skills/askovo/scripts/sure_engine.py"><code class="language-plaintext highlighter-rouge">sure_engine.py</code>：进口上限、证据资格和上下文出口</a></li>
  <li><a href="https://github.com/roy-tong/Askovo/blob/main/tests/test_p0_import_levels.py">导入级别测试</a></li>
  <li><a href="https://github.com/roy-tong/Askovo/blob/main/tests/test_delivery_conclusion_gate.py">交付结论-门测试</a></li>
  <li><a href="https://github.com/roy-tong/Askovo/blob/main/tests/test_context_export.py">上下文导出测试</a></li>
  <li><a href="https://github.com/roy-tong/Askovo/blob/main/CHANGELOG.md">Askovo更改日志</a></li>
</ul>


  </div>

  

<aside class="kb-related" aria-label="相关研究材料">
  <h2>相关研究材料</h2>
  <p>在研究图书馆中探索相关报告、数据摘要和笔记。 这些链接显示了主题联系；文章本身引用了直接证据。</p>
  
  <ul>
    
  </ul>
  <ul>
    
      
        <li><a href="/knowledge/demand-evidence/">要求证据</a></li>
      
    
      
        <li><a href="/knowledge/research-workflows/">研究工作流程</a></li>
      
    
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
