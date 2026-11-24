---
title: "We audited 110 AI usage tools: where the numbers are wrong"
date: "2026-10-02T13:00:00+08:00"
lang: en
permalink: "/en/notes/ai-usage-metering-audit-zh/"
generated_translation: true
content_id: ai-usage-metering-audit-zh
knowledge_topic: agent-systems
knowledge_units: [agent-measurement]
translation_of: /notes/ai-usage-metering-audit-zh/
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




      <link rel="alternate" hreflang="en" href="https://roy-tong.github.io/en/notes/ai-usage-metering-audit-zh/">
      <link rel="alternate" hreflang="zh-CN" href="https://roy-tong.github.io/notes/ai-usage-metering-audit-zh/">
      <link rel="alternate" hreflang="x-default" href="https://roy-tong.github.io/notes/ai-usage-metering-audit-zh/">
    <link type="application/atom+xml" rel="alternate" href="https://roy-tong.github.io/feed.xml" title="Roy.Tong"/>
    <!-- Begin Jekyll SEO tag v2.8.0 -->
<title>We audited 110 AI usage tools: where the numbers are wrong | Roy.Tong</title>
<meta name="generator" content="Jekyll v3.9.5"/>
<meta property="og:title" content="We audited 110 AI usage tools: where the numbers are wrong">
<meta name="author" content="Roy.Tong"/>
<meta property="og:locale" content="en_US">
<meta name="description" content="The billing of AI products is changing from monthly to volume and result. Each number comes from a meter, and most of the watches are in the hands of manufacturers. In the past month, we audited 110 AI usage tools for open source token, cost calculation and budget management. The core judgment first...">
<meta property="og:description" content="The billing of AI products is changing from monthly to volume and result. Each number comes from a meter, and most of the watches are in the hands of manufacturers. In the past month, we audited 110 AI usage tools for open source token, cost calculation and budget management. The core judgment first...">
<link rel="canonical" href="https://roy-tong.github.io/en/notes/ai-usage-metering-audit-zh/">
<meta property="og:url" content="https://roy-tong.github.io/en/notes/ai-usage-metering-audit-zh/">
<meta property="og:site_name" content="Roy.Tong"/>
<meta property="og:image" content="https://roy-tong.github.io/assets/images/social-preview.png"/>
<meta property="og:type" content="article"/>
<meta property="article:published_time" content="2026-10-02T13:00:00+08:00"/>
<meta name="twitter:card" content="summary_large_image"/>
<meta property="twitter:image" content="https://roy-tong.github.io/assets/images/social-preview.png"/>
<meta property="twitter:title" content="We audited 110 AI usage tools: where the numbers are wrong">
<script type="application/ld+json">
{"@context":"https://schema.org","@type":"BlogPosting","author":{"@type":"Person","name":"Roy.Tong"},"dateModified":"2026-10-02T13:00:00+08:00","datePublished":"2026-10-02T13:00:00+08:00","description":"AI 产品的计费正在从包月转向按量与按结果，每个数字都出自一只表（meter），表多半握在厂商手里。过去一个月，我们审计了开源侧数 token、算成本、管预算的 110 个 AI 用量工具。核心判断先…","headline":"我们审计了 110 个 AI 用量工具：数字都在哪里出错","image":"https://roy-tong.github.io/assets/images/social-preview.png","mainEntityOfPage":{"@type":"WebPage","@id":"https://roy-tong.github.io/notes/ai-usage-metering-audit-zh/"},"publisher":{"@type":"Organization","logo":{"@type":"ImageObject","url":"https://roy-tong.github.io/assets/images/social-preview.png"},"name":"Roy.Tong"},"url":"https://roy-tong.github.io/notes/ai-usage-metering-audit-zh/"}</script>
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
            <a class="language-toggle" href="/notes/ai-usage-metering-audit-zh/" hreflang="zh-CN" lang="zh-CN" data-language-switch data-target-language="zh-CN" aria-label="切换至中文" title="切换至中文">中文</a>
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

    <main id="main"><p class="translation-note" aria-label="Translation note">Machine-assisted translation. <a href="/notes/ai-usage-metering-audit-zh/">Read the Chinese original</a>.</p>
      




<article class="post shell reading-shell">
  <header class="post-header">
    <a class="eyebrow back-link" href="/en/archive/">← Back to the article</a>
    <h1>We audited 110 AI usage tools: where are the numbers wrong?</h1>
    <p class="post-subtitle">Five bug families, an independent reproduction, 23 upstream mergers, and the first external real case after release.</p>
    <div class="post-meta">
      <time datetime="2026-10-02T13:00:00+08:00">2026-10-02</time>
      <span>5 minutes to read</span>
      
      <a class="post-translation" href="/notes/ai-usage-metering-audit-zh/" hreflang="zh-CN">阅读中文版 →</a>
      
        <span class="post-tags">
          <a href="/en/tags/#agent">#Agent</a><a href="/en/tags/#agentmeasure">#AgentMeasure</a><a href="/en/tags/#%E8%AE%A1%E9%87%8F">#Measurement</a><a href="/en/tags/#%E5%BC%80%E6%BA%90">#Open source</a>
        </span>
      
    </div>
  </header>

  <div class="prose">
    <p>The billing of AI products is changing from monthly to volume and result. Each number comes from a meter, and most of the watches are in the hands of manufacturers. In the past month, we audited 110 AI usage tools for open source token, cost calculation and budget management. The core judgment first gave: 45+ verified bugs converged into five recurring families; 23 fixes have been merged into the upstream, including langfuse of 34k star; an external developer reproduced all 236 checks and also quantified a path to reduce the usage by about 99% (see<a href="https://github.com/roy-tong/AgentMeasure/blob/main/campaigns/audit-report-2026-09.md">The original of the audit</a>). These bugs are not delicate, but each one will be passed along the aggregation chain into the bottom line of the bill.</p>

<h2 id="表在厂商手里">The watch is in the hands of the manufacturer.</h2>

<p><a href="/en/notes/every-agent-usage-number-is-self-reported/">&quot;Each Agent usage number is self-reported&quot;</a>The judge is the person who publishes the numbers; this article goes to the inside layer to judge the table that makes the numbers. The open source code can be read, the bug can be verified, and the exposed problem model commercial products have no reason to be immune.</p>

<p>Why now? Three facts are enough. 2026-06-15, Salesforce signed a final agreement to acquire Intercom&#x27;s customer service Agent Fin for about $3.6B, and about $100M of its $400M annualized revenue comes from settlement billing (<a href="https://investor.salesforce.com/news/news-details/2026/Salesforce-Signs-Definitive-Agreement-to-Acquire-Fin/default.aspx">Salesforce Investor Announcement</a>、<a href="https://www.rte.ie/news/business/2026/0615/1578570-salesforce-agrees-to-buy-irish-tech-firm-fin-for-36bn/">RTE</a>; The transaction at the time of signing the contract is subject to regulatory approval); Zendesk is reconstructed to be billed according to &quot;Verified Resolution&quot;, and the models and standards used to determine are Zendesk&#x27;s own (<a href="https://support.zendesk.com/hc/en-us/articles/9570369117338-About-automated-resolution-tiers">Zendesk Help Center</a>、<a href="https://www.techradar.com/pro/zendesk-links-ai-pricing-to-verified-resolution-outcomes">TechRadar</a>); HubSpot changed Breeze Customer Agent to $0.50 per resolved conversation, which is defined as &quot;dialogue without manual transfer&quot; (<a href="https://www.hubspot.com/company-news/hubspots-customer-agent-and-prospecting-agent-now-you-pay-when-the-task-is-complete">HubSpot Official News</a>）。</p>

<p>The nominal unit is the same, but the price is not equivalent: in the example of Clelp, the same 100,000 resolutions per month, Fin and Zendesk are about $612K a year (<a href="https://clelp.ai/blog/outcome-based-ai-pricing-nobody-audits-the-outcome">Clelp</a>）。<strong>vendor runs the meter</strong>——The running table, the fixed unit, and the bill are the same company.</p>

<h2 id="审计方法">Audit method</h2>

<p>There are four audit aspects: price list, cache bucket, stream aggregation, and de-weighting. The iron rule is real-data-first - use real data first, then use synthetic data - each claim comes with a reproducible inspection command (audit original). Three disciplines, each corresponding to a family of bugs: classification before normalization, first determine what the event is before calculating how much it is worth; the claimed billing path is checked one by one, and the manufacturer calculates it according to what the manufacturer says; the window and fixture are anchored, and the time window and test fixture are explicitly fixed.</p>

<h2 id="五个-bug-家族五个具体例子">Five bug families, five specific examples</h2>

<p>Let&#x27;s give the panorama first:</p>

<table>
  <thead>
    <tr>
      <th>#</th>
      <th>Clan</th>
      <th>One sentence description</th>
      <th>Direct consequences</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>1</td>
      <td>The price list is outdated.</td>
      <td>The price list lacks the current model generation.</td>
      <td>All downstream summary inheritance errors</td>
    </tr>
    <tr>
      <td>2</td>
      <td>Cache multiplier wrong manufacturer</td>
      <td>A multiplier set for all manufacturers</td>
      <td>Every line looks right, but the total number is wrong.</td>
    </tr>
    <tr>
      <td>3</td>
      <td>Re-send collapse</td>
      <td>Byte-level retry is counted repeatedly.</td>
      <td>Double meter, or reverse leak meter</td>
    </tr>
    <tr>
      <td>4</td>
      <td>Absent when zero</td>
      <td>The missing field is read as 0</td>
      <td>&quot;Unknown&quot; becomes &quot;free&quot;</td>
    </tr>
    <tr>
      <td>5</td>
      <td>Window semantics</td>
      <td>Wall clock anchoring plus absolute date fixture</td>
      <td>The test is all green, and one day it will fail collectively.</td>
    </tr>
  </tbody>
</table>

<h3 id="家族一价表陈旧七个体检五个不合格">Family I: The price list is outdated - seven physical examinations, five are not qualified</h3>

<p>The most common and boring: there is no model of the current generation in the price list. In a batch of seven tools, five of the rate lines have expired or are missing (audited originals). The tool doesn&#x27;t know that it doesn&#x27;t know, and the downstream summary inherits this error as it is.</p>

<h3 id="家族二缓存乘数错厂商anthropic-的折扣套在-openai-头上">Family II: Cache multiplier wrong manufacturer - Anthropic&#x27;s discount is set on OpenAI</h3>

<p>Each manufacturer charges for the reading and writing of the cache according to different multipliers. The common shortcut is to hard-code the ratio of one company to everyone. I found a tool to apply Anthropic&#x27;s cache-read discount multiplier to the OpenAI model, and the cache read is calculated as about one-fifth of the actual billing volume (audit original). The most troublesome thing is that every line is reasonable, and no line will call the police in the line-by-line reconciliation.</p>

<h3 id="家族三重发塌缩46-的重发是字节级重复">Family 3: Reissue Collapse - 46% of reissues are byte-level repetitions</h3>

<p>When the stream request is retried, if the byte level of the two attempts is the same, some aggregators will count both. In a public corpus of 604 reissue events, 46% of reissues are byte-level repetitions; if the aggregator does not recognize the attempt identity, this part of the event will be counted according to two workloads (the audit original contains the reproduction command).</p>

<h3 id="家族四absent-被当成-zero">Family 4: absent is regarded as zero</h3>

<p>When the usage field is missing, one in the code<code class="language-plaintext highlighter-rouge">or 0</code>Translate &quot;unknown&quot; into &quot;free&quot;. It reads like defensive programming, but it behaves like an unauthorized discount. This problem cannot be solved at the grammatical level: absent must remain absent, and the aggregation layer should allow the output UNPROVABLE, instead of being forced to hand over a 0.</p>

<p>There is a rule worth looking at side by side in commercial billing: Intercom&#x27;s Fin counts &quot;customers leaving silently&quot; as assumed resolution and billing as usual (<a href="https://www.intercom.com/help/en/articles/8205718-fin-ai-agent-outcomes">Intercom Help Document 8205718</a>); There are buyers in the community who self-reported confirmed resolution 6–7%, assumed nearly 60% - the missing customer response was read as income (<a href="https://community.intercom.com/analyze-fin-93/how-do-you-improve-your-confirmed-resolution-rate-8268">Intercom Community Post 8268</a>). What they share is not the same bug, but the same measurement risk. The system must explicitly write [how to map unknown states to billing states] into the rules.</p>

<h3 id="家族五窗口语义我们自己的-ci-踩过的坑">Family Five: Window Semantics - Our own CI has stepped on the pits</h3>

<p>The quota window is anchored to the clock time, and the test fixture nails the absolute date, so the test can be full green for 30 consecutive days, and then fail on the same day. This example is contributed by ourselves: our CI has fooled us once (audit original).</p>

<h2 id="独立复现">Independent reproduction</h2>

<p>An external developer independently reproduced the whole set of consistency tests - 236 checks were reproduced - and quantified the cache billing of the commercial observable manufacturer AgentOps: four code paths failed, and the affected path usage was reported 98.9% and 95.1% less respectively, and the problem was nailed to the specific commit (<a href="https://github.com/roy-tong/AgentMeasure/tree/main/conformance/evidence/agentops-anthropic-cache-drop-independent">Evidence card</a>，commit <a href="https://github.com/roy-tong/AgentMeasure/commit/010ba15">010ba15</a>Into the warehouse).</p>

<h2 id="23-个上游合并维护者用代码投票">23 upstream mergers: maintainers vote with code</h2>

<p>The fingerprints left by the audit are 23 repairs that have been merged into the upstream: price list update, cache multiplier modified by manufacturer, reissue collapse protection with regression fixture, explicit absent-vs-zero semantics, including langfuse (34k star) and codeburn (11k star) (<a href="https://dev.to/roytong/we-audited-110-ai-usage-tools-here-is-where-the-numbers-go-wrong-5d8h">Complete manuscript in English</a>). Each one starts with the thread that the maintainer has been discussing, and we just added it with the rewappable check. Merge is not a like, but a vote by the maintainer with his own code.</p>

<h2 id="发布后的第一个真实案例">The first real case after the release</h2>

<p>After the report was released, the first real case that emerged from the outside fell into the evidence bank. The usage record of rulestack is publicly available. There is a work on the ledger that counts 436k tokens, and the result of the independent recalculation is 54,154 - about 8 times the difference. The reason is not in the price list, but in the billing semantics of the cache: the same replay cache prefix, every spawn is re-billed as a new input. The path of this case is the path that every billing dispute should take - advocating, recalculation, and citing the source. The judgment and piece-by-article data are in<a href="https://github.com/roy-tong/AgentMeasure/tree/main/conformance/evidence">Evidence card</a>, see the complete record<a href="https://github.com/roy-tong/AgentMeasure/blob/main/campaigns/audit-report-2026-09.md">Audit report</a>（<a href="https://dev.to/roytong/we-audited-110-ai-usage-tools-here-is-where-the-numbers-go-wrong-5d8h">Complete manuscript in English</a>）。</p>

<p>If the bill is calculated according to the &quot;solution quantity&quot; instead of the token, the problem will be changed: the measurement is not the usage, but the result of the supplier&#x27;s own judgment. The local check path of this kind of bill is written in Verovo&#x27;s<a href="https://roy-tong.github.io/Verovo/blog/resolution-bill-check.html">&quot;Your AI customer service bill counts the amount of self-certified solutions&quot;</a>。</p>

<h2 id="厂商该公布的两样东西">Two things that manufacturers should announce</h2>

<p>We have also checked 20 commercial manufacturers. What to do if the meter is wrong: public dispute path or correction policy, either. Among the 20 public documents we have checked, no one has been found as of 2026-09 (<a href="https://dev.to/roytong/we-audited-110-ai-usage-tools-here-is-where-the-numbers-go-wrong-5d8h">Complete manuscript in English</a>). When the manufacturer runs the table, scores its own work, and does not announce the correction process, &quot;trust us&quot; is the whole internal control system. Two minimum standards: a named dispute path and a machine-veriable billing disclosure.</p>

<h2 id="自查你的账单十分钟起步">Check your bill by yourself: starting from ten minutes</h2>

<p>Compress the audit method into a list. It is expected to be honest: the export format of each platform is different, and the inspector consumes standardized usage events. Your export needs to go through a field mapping first - ten minutes is only enough to start.</p>

<ol>
  <li><strong>Export your usage data.</strong>Most platforms support CSV or API export, which is your data.</li>
  <li><strong>Run the open source checker locally.</strong>Conformance pack in<a href="https://github.com/roy-tong/AgentMeasure">github.com/roy-tong/AgentMeasure</a>, MIT protocol, the data does not come out of your machine.</li>
  <li>Ask the five families one by one: Does the price list cover the generation of the model you are using? Is the cache read and write multiplier differentiated by manufacturer? Has the streaming retry been double-counted? Is the missing field<code class="language-plaintext highlighter-rouge">or 0</code>Swallowed? What time is the quota window anchored?</li>
  <li>Check whether it is traceable. EACH JUDGMENT SHOULD BE ABLE TO FOLLOW A NAMED RULE; IT CAN BE PROCESSED AS UNPROVABLE - IT IS PROCESSED AS 0, WHICH IS EQUIVALENT TO A DISCOUNT FOR THE OTHER PARTY.</li>
  <li>Decide the next step with the recalculation result. You can defend the number on the bill that can withstand independent recalculation; if it can&#x27;t be recalculation, you have a receipt in your hand.</li>
</ol>

<p>The settlement specification behind the inspector is<a href="https://github.com/roy-tong/AgentMeasure/blob/main/standard/SETTLEMENT.md">AMS-1</a>. The full version of English (including warehouse discovery index and reproduction command) was first published in<a href="https://dev.to/roytong/we-audited-110-ai-usage-tools-here-is-where-the-numbers-go-wrong-5d8h">dev.to</a>。</p>

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
