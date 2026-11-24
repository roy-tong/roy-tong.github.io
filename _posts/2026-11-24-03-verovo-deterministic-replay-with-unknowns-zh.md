---
title: "Verovo：人工智能指控的确定性重播，未知数完好无损"
date: "2026-11-24 12:05:00 +0800"
description: "Decimal arithmetic, counting grain, content-addressed revisions, OCR integrity, and line-level buyer disposition."
permalink: "/notes/03-verovo-deterministic-replay-with-unknowns/"
content_id: 03-verovo-deterministic-replay-with-unknowns
knowledge_topic: agent-systems
knowledge_units: [agent-measurement, evidence-maintenance]
translation_of: /en/notes/03-verovo-deterministic-replay-with-unknowns/
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




      <link rel="alternate" hreflang="en" href="https://roy-tong.github.io/en/notes/03-verovo-deterministic-replay-with-unknowns/">
      <link rel="alternate" hreflang="zh-CN" href="https://roy-tong.github.io/notes/03-verovo-deterministic-replay-with-unknowns/">
      <link rel="alternate" hreflang="x-default" href="https://roy-tong.github.io/notes/03-verovo-deterministic-replay-with-unknowns/">
    <link type="application/atom+xml" rel="alternate" href="https://roy-tong.github.io/feed.xml" title="Roy.Tong"/>
    <!-- Begin Jekyll SEO tag v2.8.0 -->
<title>Verovo：人工智能指控的确定性重播，未知数完好无损 | Roy.Tong</title>
<meta name="generator" content="Jekyll v3.9.5"/>
<meta property="og:title" content="Verovo：人工智能指控的确定性重播，未知数完好无损">
<meta name="author" content="Roy.Tong"/>
<meta property="og:locale" content="zh_CN">
<meta name="description" content="Decimal arithmetic, counting grain, content-addressed revisions, OCR integrity, and line-level buyer disposition."/>
<meta property="og:description" content="Decimal arithmetic, counting grain, content-addressed revisions, OCR integrity, and line-level buyer disposition."/>
<link rel="canonical" href="https://roy-tong.github.io/notes/03-verovo-deterministic-replay-with-unknowns/">
<meta property="og:url" content="https://roy-tong.github.io/notes/03-verovo-deterministic-replay-with-unknowns/">
<meta property="og:site_name" content="Roy.Tong"/>
<meta property="og:image" content="https://roy-tong.github.io/assets/images/social-preview.png"/>
<meta property="og:type" content="article"/>
<meta property="article:published_time" content="2026-11-24T12:05:00+08:00"/>
<meta name="twitter:card" content="summary_large_image"/>
<meta property="twitter:image" content="https://roy-tong.github.io/assets/images/social-preview.png"/>
<meta property="twitter:title" content="Verovo：人工智能指控的确定性重播，未知数完好无损">
<script type="application/ld+json">
{"@context":"https://schema.org","@type":"BlogPosting","author":{"@type":"Person","name":"Roy.Tong"},"dateModified":"2026-11-24T12:05:00+08:00","datePublished":"2026-11-24T12:05:00+08:00","description":"Decimal arithmetic, counting grain, content-addressed revisions, OCR integrity, and line-level buyer disposition.","headline":"Verovo: deterministic replay for AI charges, with the unknowns intact","image":"https://roy-tong.github.io/assets/images/social-preview.png","mainEntityOfPage":{"@type":"WebPage","@id":"https://roy-tong.github.io/en/notes/03-verovo-deterministic-replay-with-unknowns/"},"publisher":{"@type":"Organization","logo":{"@type":"ImageObject","url":"https://roy-tong.github.io/assets/images/social-preview.png"},"name":"Roy.Tong"},"url":"https://roy-tong.github.io/en/notes/03-verovo-deterministic-replay-with-unknowns/"}</script>
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
            <a class="language-toggle" href="/en/notes/03-verovo-deterministic-replay-with-unknowns/" hreflang="en" lang="en" data-language-switch data-target-language="en" aria-label="切换至中文" title="切换至中文">中文</a>
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

    <main id="main"><p class="translation-note" aria-label="翻译说明">机器辅助翻译。<a href="/en/notes/03-verovo-deterministic-replay-with-unknowns/">阅读英文原文</a>。</p>
      




<article class="post shell reading-shell">
  <header class="post-header">
    <a class="eyebrow back-link" href="/archive/">← 所有写作</a>
    <h1>维罗沃：人工智能指控的决定性重播，未知数完好无损</h1>
    <p class="post-subtitle">十二点算术、计数谷物、内容地址修订、OCR完整性和行级买家处置。</p>
    <div class="post-meta">
      <time datetime="2026-11-24T12:05:00+08:00">2026年11月24日</time>
      <span>10分钟阅读</span>
      
      <a class="post-translation" href="/en/notes/03-verovo-deterministic-replay-with-unknowns/" hreflang="en">Read in English →</a>
      
        <span class="post-tags">
          <a href="/tags/#ai%20agent">#人工智能代理</a>
        </span>
      
    </div>
  </header>

  <div class="prose">
    <p>一个用于claude-hud的公共合成夹具包含200万个一小时缓存写入令牌，用于一个价格为每百万输入令牌3美元的模型。 实施以五分钟乘数定价：</p>

<div class="language-text highlighter-rouge"><div class="highlight"><pre class="highlight"><code>2,000,000 / 1,000,000 × $3 × 1.25 = $7.50
</code></pre></div></div>

<p>适用的一小时乘数是2×：</p>

<div class="language-text highlighter-rouge"><div class="highlight"><pre class="highlight"><code>2,000,000 / 1,000,000 × $3 × 2.00 = $12.00
</code></pre></div></div>

<p>差额为4.50美元，低估了该部分的37.5%。 解析器已经暴露了缓存层拆分；成本路径丢弃了它。 修复被合并为<a href="https://github.com/jarrodwatts/claude-hud/pull/758">克劳德-胡德公关#758</a>.</p>

<p>那个夹具不是客户发票，也不是收回的钱。 它展示了一个更通用的工程问题：人工智能收费是事件身份、计数规则、价格版本、时间窗口和算术的结果。 没有这些输入的总数很难审查。 Verovo的实施是试图使每个都可以重播，同时将交付和买家接受保持在账单判决之外。</p>

<h2 id="start-with-a-complete-small-example">从一个完整的小例子开始</h2>

<p>公共重播夹具包含两个综合事件：</p>

<div class="language-json highlighter-rouge"><div class="highlight"><pre class="highlight"><code><span class="p">{</span><span class="w">
  </span><span class="nl">"transaction_id"</span><span class="p">:</span><span class="w"> </span><span class="s2">"synthetic-tx-001"</span><span class="p">,</span><span class="w">
  </span><span class="nl">"metric_code"</span><span class="p">:</span><span class="w"> </span><span class="s2">"api_call"</span><span class="p">,</span><span class="w">
  </span><span class="nl">"occurred_at"</span><span class="p">:</span><span class="w"> </span><span class="s2">"2026-10-05T10:00:00+00:00"</span><span class="p">,</span><span class="w">
  </span><span class="nl">"ingested_at"</span><span class="p">:</span><span class="w"> </span><span class="s2">"2026-11-02T00:00:00+00:00"</span><span class="p">,</span><span class="w">
  </span><span class="nl">"source_ref"</span><span class="p">:</span><span class="w"> </span><span class="s2">"synthetic-events.jsonl"</span><span class="p">,</span><span class="w">
  </span><span class="nl">"source_hash"</span><span class="p">:</span><span class="w"> </span><span class="s2">"sha256:1111…"</span><span class="p">,</span><span class="w">
  </span><span class="nl">"properties"</span><span class="p">:</span><span class="w"> </span><span class="p">{</span><span class="w">
    </span><span class="nl">"task_id"</span><span class="p">:</span><span class="w"> </span><span class="s2">"synthetic-task-1"</span><span class="p">,</span><span class="w">
    </span><span class="nl">"attempt_id"</span><span class="p">:</span><span class="w"> </span><span class="s2">"synthetic-attempt-1"</span><span class="p">,</span><span class="w">
    </span><span class="nl">"vendor"</span><span class="p">:</span><span class="w"> </span><span class="s2">"example-vendor"</span><span class="p">,</span><span class="w">
    </span><span class="nl">"vendor_record_id"</span><span class="p">:</span><span class="w"> </span><span class="s2">"synthetic-vendor-row-1"</span><span class="w">
  </span><span class="p">}</span><span class="w">
</span><span class="p">}</span><span class="w">
</span></code></pre></div></div>

<p>第二个事件在一分钟后有一个不同的交易和供应商记录ID。 两者都命名相同的任务和尝试。 批准的规则图显示：</p>

<div class="language-json highlighter-rouge"><div class="highlight"><pre class="highlight"><code><span class="p">{</span><span class="w">
  </span><span class="nl">"metric_code"</span><span class="p">:</span><span class="w"> </span><span class="s2">"api_call"</span><span class="p">,</span><span class="w">
  </span><span class="nl">"aggregate"</span><span class="p">:</span><span class="w"> </span><span class="s2">"count"</span><span class="p">,</span><span class="w">
  </span><span class="nl">"unit"</span><span class="p">:</span><span class="w"> </span><span class="s2">"call"</span><span class="p">,</span><span class="w">
  </span><span class="nl">"currency"</span><span class="p">:</span><span class="w"> </span><span class="s2">"USD"</span><span class="p">,</span><span class="w">
  </span><span class="nl">"unit_price"</span><span class="p">:</span><span class="w"> </span><span class="s2">"0.01"</span><span class="p">,</span><span class="w">
  </span><span class="nl">"price_version"</span><span class="p">:</span><span class="w"> </span><span class="s2">"synthetic-price-1"</span><span class="p">,</span><span class="w">
  </span><span class="nl">"valid_from"</span><span class="p">:</span><span class="w"> </span><span class="s2">"2026-10-01"</span><span class="w">
</span><span class="p">}</span><span class="w">
</span></code></pre></div></div>

<p>我构建并验证了捆绑包，然后检查了其清单。 实际结果是：</p>

<div class="language-json highlighter-rouge"><div class="highlight"><pre class="highlight"><code><span class="p">{</span><span class="w">
  </span><span class="nl">"counts"</span><span class="p">:</span><span class="w"> </span><span class="p">{</span><span class="w">
    </span><span class="nl">"received"</span><span class="p">:</span><span class="w"> </span><span class="mi">2</span><span class="p">,</span><span class="w">
    </span><span class="nl">"included"</span><span class="p">:</span><span class="w"> </span><span class="mi">2</span><span class="p">,</span><span class="w">
    </span><span class="nl">"duplicates"</span><span class="p">:</span><span class="w"> </span><span class="mi">0</span><span class="p">,</span><span class="w">
    </span><span class="nl">"conflicts"</span><span class="p">:</span><span class="w"> </span><span class="mi">0</span><span class="p">,</span><span class="w">
    </span><span class="nl">"excluded"</span><span class="p">:</span><span class="w"> </span><span class="mi">0</span><span class="p">,</span><span class="w">
    </span><span class="nl">"late"</span><span class="p">:</span><span class="w"> </span><span class="mi">0</span><span class="w">
  </span><span class="p">},</span><span class="w">
  </span><span class="nl">"metrics"</span><span class="p">:</span><span class="w"> </span><span class="p">[{</span><span class="w">
    </span><span class="nl">"metric_code"</span><span class="p">:</span><span class="w"> </span><span class="s2">"api_call"</span><span class="p">,</span><span class="w">
    </span><span class="nl">"quantity"</span><span class="p">:</span><span class="w"> </span><span class="s2">"2.0000"</span><span class="p">,</span><span class="w">
    </span><span class="nl">"unit"</span><span class="p">:</span><span class="w"> </span><span class="s2">"call"</span><span class="p">,</span><span class="w">
    </span><span class="nl">"currency"</span><span class="p">:</span><span class="w"> </span><span class="s2">"USD"</span><span class="p">,</span><span class="w">
    </span><span class="nl">"amount"</span><span class="p">:</span><span class="w"> </span><span class="s2">"0.0200"</span><span class="p">,</span><span class="w">
    </span><span class="nl">"event_count"</span><span class="p">:</span><span class="w"> </span><span class="mi">2</span><span class="p">,</span><span class="w">
    </span><span class="nl">"price_version"</span><span class="p">:</span><span class="w"> </span><span class="s2">"synthetic-price-1"</span><span class="w">
  </span><span class="p">}],</span><span class="w">
  </span><span class="nl">"charge_verdict"</span><span class="p">:</span><span class="w"> </span><span class="s2">"PASS"</span><span class="p">,</span><span class="w">
  </span><span class="nl">"delivery_state"</span><span class="p">:</span><span class="w"> </span><span class="s2">"UNKNOWN"</span><span class="w">
</span><span class="p">}</span><span class="w">
</span></code></pre></div></div>

<p>重要的细节是一样的<code class="language-plaintext highlighter-rouge">attempt_id</code>在两笔交易中。 夹具可以支持尝试级别的身份覆盖范围，但并不能推断出这两项交易是两项逻辑运算。 尝试、操作和授权是不同的。 运营级别的分组需要额外的证据。</p>

<p>身份报告还显示：</p>

<div class="language-text highlighter-rouge"><div class="highlight"><pre class="highlight"><code>records=2
task_id=2
attempt_id=2
vendor=2
vendor_record_id=2
complete_for_attempt=2
retry_of=0
cache_hit_of=0
</code></pre></div></div>

<p>零重试链接是观察到的字段计数，而不是声称没有发生重试。<code class="language-plaintext highlighter-rouge">external_subject_id</code>保留为账单主题，绝不用作替代<code class="language-plaintext highlighter-rouge">task_id</code>.</p>

<h2 id="replay-is-a-sequence-of-refusals-and-calculations">重播是一系列拒绝和计算</h2>

<p>重播引擎规范化每个事件，应用恒等式和规则映射，发出行级排除，仅汇总包含的行，并计算内容寻址修订。</p>

<h3 id="1-event-identity-and-deduplication">1. 事件识别和重复数据删除</h3>

<p><code class="language-plaintext highlighter-rouge">dedupe_key</code>默认为<code class="language-plaintext highlighter-rouge">transaction_id</code>。 如果同一键再次出现，引擎会比较两者<code class="language-plaintext highlighter-rouge">properties_hash</code>和<code class="language-plaintext highlighter-rouge">source_hash</code>:</p>

<ul>
  <li>相同的密钥和相同的哈希：数一次并记录一个重复的；</li>
  <li>具有不同内容的相同密钥：记录冲突并排除行<code class="language-plaintext highlighter-rouge">DEDUPE_CONFLICT</code>;</li>
  <li>新关键：继续通过定价和聚合。</li>
</ul>

<p>冲突事件不会合并到一个更漂亮的历史中。 规则图中缺少的度量产生<code class="language-plaintext highlighter-rouge">METRIC_NOT_IN_RULE_MAP</code>，数量、价格和金额为空。</p>

<h3 id="2-time-and-rule-eligibility">2. 时间和规则资格</h3>

<p>一个时期是半开放的：<code class="language-plaintext highlighter-rouge">[start, end)</code>。 该窗口外的事件接收<code class="language-plaintext highlighter-rouge">PERIOD_OUT_OF_WINDOW</code>。 价格有自己的有效期和<code class="language-plaintext highlighter-rouge">price_version</code>；过期或尚未生效的价格产生<code class="language-plaintext highlighter-rouge">PRICE_NOT_VALID_FOR_OCCURRED_AT</code>。 缺失的价格会产生<code class="language-plaintext highlighter-rouge">PRICE_MISSING</code>，不是零。</p>

<p>规则映射聚合需要两者<code class="language-plaintext highlighter-rouge">approved_by</code>和<code class="language-plaintext highlighter-rouge">approved_at</code>。 没有它们，聚合状态是<code class="language-plaintext highlighter-rouge">RULE_MAP_NOT_APPROVED</code>。 延迟事件被标记并创建新的重播修订版；它们不会重写之前签名的关闭。</p>

<h3 id="3-aggregation">3. 集合</h3>

<p>发动机支持<code class="language-plaintext highlighter-rouge">count</code>, <code class="language-plaintext highlighter-rouge">sum</code>, <code class="language-plaintext highlighter-rouge">max</code>, <code class="language-plaintext highlighter-rouge">unique_count</code>, <code class="language-plaintext highlighter-rouge">latest</code>，还有<code class="language-plaintext highlighter-rouge">weighted_sum</code>。 每个都有不同的输入要求。 缺少数量块<code class="language-plaintext highlighter-rouge">sum</code>但不是<code class="language-plaintext highlighter-rouge">count</code>或者<code class="language-plaintext highlighter-rouge">unique_count</code>。 缺少权重使加权结果为空<code class="language-plaintext highlighter-rouge">WEIGHT_MISSING</code>。 仅仅<code class="language-plaintext highlighter-rouge">count</code>, <code class="language-plaintext highlighter-rouge">sum</code>, <code class="language-plaintext highlighter-rouge">weighted_sum</code>，还有<code class="language-plaintext highlighter-rouge">unique_count</code>按当前实施情况定价；<code class="language-plaintext highlighter-rouge">max</code>和<code class="language-plaintext highlighter-rouge">latest</code>返回<code class="language-plaintext highlighter-rouge">AGGREGATE_NOT_PRICED</code>.</p>

<p>对于两个事件的例子，<code class="language-plaintext highlighter-rouge">count</code>忽略数量属性的缺失，计算两个调用，并乘以<code class="language-plaintext highlighter-rouge">Decimal("0.01")</code>生产<code class="language-plaintext highlighter-rouge">Decimal("0.0200")</code>.</p>

<h3 id="4-revision-identity">4. 修订身份</h3>

<p>输入指纹哈希包含以下的规范对象：</p>

<div class="language-text highlighter-rouge"><div class="highlight"><pre class="highlight"><code>period + closed_at + complete rule map + normalized events
</code></pre></div></div>

<p>只有解析器的位置<code class="language-plaintext highlighter-rouge">order</code>字段从归一化事件中删除。 修订ID是<code class="language-plaintext highlighter-rouge">ur-</code>加上指纹SHA-256摘要的前十二个十六字符。 这不仅仅是最终金额的哈希：更改规则、身份属性、时间戳或其他输入字段会更改修订版。</p>

<h2 id="verification-checks-more-than-the-final-number">验证检查超过最终数量</h2>

<p>复制捆绑将源输入复制到<code class="language-plaintext highlighter-rouge">inputs/</code>并记录每个文件的SHA-256和字节长度。 验证然后检查：</p>

<div class="language-text highlighter-rouge"><div class="highlight"><pre class="highlight"><code>manifest schema and required fields
→ exact file set
→ every file hash and byte length
→ generator/algorithm version
→ replayed input_fingerprint and revision_id
→ replayed counts and metrics
→ complete semantic replay output
→ independently recomputed identity mapping
→ independently recomputed discrepancy classification
</code></pre></div></div>

<p>不完整的清单或缺失的证据产生<code class="language-plaintext highlighter-rouge">UNPROVEN</code>；完整但失败的验证会产生<code class="language-plaintext highlighter-rouge">FAIL</code>。 构建器写入暂存目录，并在替换现有输出之前进行验证。 失败的构建使之前的捆绑包完好无损。</p>

<p>公共投影是一个单独的操作，有自己的许可规则。 仅合成或明确批准<code class="language-plaintext highlighter-rouge">public-redacted</code>捆绑包可以发布。 公共副本删除私有路径和行级主题。 如果没有私人输入，独立回放是<code class="language-plaintext highlighter-rouge">UNAVAILABLE</code>，不是隐含的成功。</p>

<p>夹具的校样导出正好产生了三个检查：</p>

<div class="language-text highlighter-rouge"><div class="highlight"><pre class="highlight"><code>artifact-integrity   P1  PASS
replay-integrity     P1  PASS
external-result      P4  UNCHECKED
</code></pre></div></div>

<p>用法算术通过。 没有观察到外部接受。 交货仍然存在<code class="language-plaintext highlighter-rouge">UNKNOWN</code>.</p>

<h2 id="canonical-proof-uses-a-different-replay-contract">规范证明使用不同的重播合同</h2>

<p>使用回放和规范金融是独立的引擎。 规范的<code class="language-plaintext highlighter-rouge">verovo proof export</code>命令运行财务模型，记录源哈希值，并写入语义输出指纹。<code class="language-plaintext highlighter-rouge">verovo proof replay</code>然后应用这个决策表：</p>

<table>
  <thead>
    <tr>
      <th>状况</th>
      <th>结果</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>证明结构、投影、模式或预期哈希无效</td>
      <td><code class="language-plaintext highlighter-rouge">INDETERMINATE</code></td>
    </tr>
    <tr>
      <td>必需的输入缺失或其哈希被更改</td>
      <td><code class="language-plaintext highlighter-rouge">EXPIRED</code></td>
    </tr>
    <tr>
      <td>输入匹配，但规范输出不同</td>
      <td><code class="language-plaintext highlighter-rouge">FAIL</code></td>
    </tr>
    <tr>
      <td>输入和规范语义输出匹配</td>
      <td><code class="language-plaintext highlighter-rouge">PASS</code></td>
    </tr>
  </tbody>
</table>

<p>语义指纹仅删除<code class="language-plaintext highlighter-rouge">intake_report.generated_at</code>。 规范结果中的所有其他字段都参与规范JSON哈希。 因此，更改的分配、判决、覆盖字段或与买家相关的产出不能隐藏在不变的顶线金额后面。</p>

<p>规范证明还保留了独立的结论类型：规则重新开具、发票对账、供应商对账、买方验证和交货验收。 它们不会继承彼此的证明水平。 两个供应商控制的出口可以支持供应商对账；它们不会仅仅因为买家下载了两个文件就成为买家控制的证据。</p>

<h2 id="money-has-more-than-one-contract">金钱有不止一份合同</h2>

<p>财务代码倾向于积累小的四舍五入决定，直到两个显示器不一致。 Verovo的货币合同集中了任务经济显示和分配行为：</p>

<ul>
  <li>内部算术使用<code class="language-plaintext highlighter-rouge">Decimal</code>，非有限或无效的严格输入被拒绝；</li>
  <li>外部显示器使用二进制字符串和<code class="language-plaintext highlighter-rouge">ROUND_HALF_UP</code>;</li>
  <li>分配使用最大-remainder方法，因此分配的美分总和与原始总数完全一致；</li>
  <li>零权重任务没有分配。</li>
</ul>

<p>例如，运行当前实现会给出：</p>

<div class="language-text highlighter-rouge"><div class="highlight"><pre class="highlight"><code>display(0.005)                    → 0.01
allocate(0.05, weights a=b=c=1)  → a=0.02, b=0.02, c=0.01
</code></pre></div></div>

<p>最后一个例子是第一个楼层，每个精确分配到<code class="language-plaintext highlighter-rouge">0.01</code>，然后将剩余的两美分分配到剩余部分。 不变量是<code class="language-plaintext highlighter-rouge">sum(allocated) == total</code>；它不会将四舍五入错误分配到假想中的第四项任务中。</p>

<p>还有一个用于传统显示路径的宽大解析器，它将无效输入映射为零。 它被明确排除在会计计算之外。 这种区别与四舍五入规则一样重要：显示回退不能成为财务事实。 买方分类账的零十进制货币公差和预订/分配规则仍然是单独的合同，而不是被二进制显示功能机械地取代。</p>

<h2 id="ocr-approval-is-bound-to-bytes-and-revisions">OCR批准绑定到字节和修订</h2>

<p>OCR引入了两个不同的风险：错误地提取字段，以及在预订另一个文档之前批准一个文档。</p>

<p>每个账单候选人都记录了源文件的SHA-256。 审查和预订重新验证：</p>

<div class="language-text highlighter-rouge"><div class="highlight"><pre class="highlight"><code>raw source hash
+ OCR raw_text_sha256
+ OCR payload schema
+ OCR lines
+ reconstructed OCR text
</code></pre></div></div>

<p>不匹配返回<code class="language-plaintext highlighter-rouge">STALE_SOURCE</code>，并在复制之前立即再次检查来源。 在没有的平台上<code class="language-plaintext highlighter-rouge">fcntl</code>，候选人锁定失败，关闭<code class="language-plaintext highlighter-rouge">UNSUPPORTED_CAPABILITY</code>而不是假装持有跨进程锁。</p>

<p>行算术在审查和预订时重新计算。 数量×单价必须与以下范围内的打印数量相匹配：</p>

<div class="language-text highlighter-rouge"><div class="highlight"><pre class="highlight"><code>max(one smallest printed unit, 1% of |line amount|)
</code></pre></div></div>

<p>无法解析的数量、价格或金额不能被免除到带有审查员备注的已预订发票中。 这避免了旧的零十进制货币故障，即基于规模的公差可能会接受无效的日元或韩元线。</p>

<p>周期投影增加了字节级一致性检查。<code class="language-plaintext highlighter-rouge">CaseRepository</code>快照十个命名状态工件，包括作业、扫描、映射、计算、报告、审查、签收和修订。<code class="language-plaintext highlighter-rouge">PeriodCase.project()</code>检查恢复状态，快照这些字节，构建投影，然后验证每个字节是否保持不变。 中投影写入返回<code class="language-plaintext highlighter-rouge">STALE_SOURCE</code>.</p>

<p>签收绑定同样明确。 当前报告和签收必须就以下方面达成一致：</p>

<ul>
  <li><code class="language-plaintext highlighter-rouge">revision_id</code>;</li>
  <li>报告输出指纹；</li>
  <li>计算指纹；</li>
  <li>规范快照指纹；</li>
  <li>修订元数据和签收记录内容。</li>
</ul>

<p>签收后添加证据会创建新的修订版。 它不会改变已签署的报告，也不会让旧的签名认可新的计算。</p>

<h2 id="the-spend-action-projection-has-a-conservative-order">支出行动预测有一个保守的顺序</h2>

<p>最近的<code class="language-plaintext highlighter-rouge">spend-actions</code>命令将审计案例转化为买家工作，而不是另一个总分。 它的行级决策顺序是：</p>

<table>
  <thead>
    <tr>
      <th>优先顺序的条件</th>
      <th>情节</th>
      <th>默认所有者角色</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>公开发现无法证明，或被归类为缺少证据、货币不匹配或未经验证的结果</td>
      <td><code class="language-plaintext highlighter-rouge">evidence_required</code></td>
      <td>买方操作，或货币不匹配的融资</td>
    </tr>
    <tr>
      <td>任何其他未公开的发现</td>
      <td><code class="language-plaintext highlighter-rouge">review_required</code></td>
      <td>分摊成本分配的采购或融资</td>
    </tr>
    <tr>
      <td>实现了发现，线上没有开放的发现</td>
      <td><code class="language-plaintext highlighter-rouge">settled</code></td>
      <td>买家融资</td>
    </tr>
    <tr>
      <td>清单中明确列出的行<code class="language-plaintext highlighter-rouge">clean_charge_lines</code></td>
      <td><code class="language-plaintext highlighter-rouge">ready_for_payment</code></td>
      <td>应付账款</td>
    </tr>
    <tr>
      <td>没有发现，也没有明确的干净确认</td>
      <td><code class="language-plaintext highlighter-rouge">unreviewed</code></td>
      <td>买家融资</td>
    </tr>
  </tbody>
</table>

<p>最后一行很重要：没有发现不是付款结算。</p>

<p>金额摘要仍然按行动和货币分组，与<code class="language-plaintext highlighter-rouge">known_count</code>, <code class="language-plaintext highlighter-rouge">unknown_count</code>，还有<code class="language-plaintext highlighter-rouge">known_value</code>。 未知数量被计算在内，而不是归零。 该命令永远不会执行或授权付款；买方仍然在其他地方记录实际付款、保留、证据请求或供应商审查。</p>

<p>配套的提供商清单工作流程返回本地<code class="language-plaintext highlighter-rouge">admit</code>, <code class="language-plaintext highlighter-rouge">degrade</code>，或者<code class="language-plaintext highlighter-rouge">refuse</code>从声明的就绪性检查、引擎身份、资源限制、覆盖范围和清理状态。 它不接触发动机。 录取说明了宣布的工程合同，而不是生产整合或采购是安全的。</p>

<h2 id="the-next-period-tests-reuse-without-inheriting-old-passes">下一个时期测试重复使用而不继承旧通行证</h2>

<p>跨期重复使用有明确的资格规则<code class="language-plaintext highlighter-rouge">PeriodCase</code>。 只有当定价规则<code class="language-plaintext highlighter-rouge">valid_from</code>在月经开始或之前，以及它的<code class="language-plaintext highlighter-rouge">valid_to</code>在该期间的最后一天或之后。 每个可重复使用的规则都发出：</p>

<div class="language-json highlighter-rouge"><div class="highlight"><pre class="highlight"><code><span class="p">{</span><span class="w">
  </span><span class="nl">"requires_re_review_next_period"</span><span class="p">:</span><span class="w"> </span><span class="kc">true</span><span class="w">
</span><span class="p">}</span><span class="w">
</span></code></pre></div></div>

<p>上个月的<code class="language-plaintext highlighter-rouge">PASS</code>不包括本月的价格。 有用的资产是有效的字段映射、规则引用、接受标准和比较定义，而不是不可改变的批准。</p>

<p>因此，有意义的第二个时期应该记录哪些映射被重复使用，哪些规则过期，出现了多少个新的开放项目，人类花了多少分钟审查和缺失的证据，以及买家实际做了什么。 重播相同的两个事件建立了决定论。 在这些约束下处理新的周期测试持续价值。</p>

<h2 id="what-the-current-implementation-establishes">目前的实施建立了什么</h2>

<p>Verovo最强大的机制不是通用的“法案是正确的”徽章。 它是更窄的、可检查的不变量的集合：</p>

<ul>
  <li>冲突事件不会无声合并；</li>
  <li>缺少价格、数量、身份和证据仍然无效或未知；</li>
  <li>输入和输出修订是内容解决的；</li>
  <li>货币使用明确的算术和分配合同；</li>
  <li>OCR审查和签收绑定到特定的字节；</li>
  <li>清洁线、未经审查的线和需要证据的线仍然不同；</li>
  <li>重播成功永远不会成为买家的接受。</li>
</ul>

<p>在普遍基准存在之前，这些不变性使系统变得有用。 他们还为第三方提供了具体的攻击：改变一个事件、更改规则、编辑OCR工件、更改签名修订版或删除身份字段。 结果<code class="language-plaintext highlighter-rouge">FAIL</code>, <code class="language-plaintext highlighter-rouge">EXPIRED</code>, <code class="language-plaintext highlighter-rouge">UNPROVEN</code>，或者<code class="language-plaintext highlighter-rouge">INDETERMINATE</code>是产品的一部分，而不是被绿色仪表板隐藏的尴尬。</p>

<h3 id="source-and-verification-links">来源和验证链接</h3>

<ul>
  <li><a href="https://roy-tong.github.io/Verovo/examples/replayable-period.html">可重播期夹具和命令</a></li>
  <li><a href="https://github.com/roy-tong/Verovo/blob/main/buyer-ledger/buyer_ledger/usage_replay.py"><code class="language-plaintext highlighter-rouge">usage_replay.py</code>：事件归一化、定价、聚合和修订</a></li>
  <li><a href="https://github.com/roy-tong/Verovo/blob/main/buyer-ledger/buyer_ledger/reproduce.py"><code class="language-plaintext highlighter-rouge">reproduce.py</code>：捆绑验证和公开投影</a></li>
  <li><a href="https://github.com/roy-tong/Verovo/blob/main/healthcheck/verovo_healthcheck/proof_export.py"><code class="language-plaintext highlighter-rouge">proof_export.py</code>：规范语义指纹和重播判决</a></li>
  <li><a href="https://github.com/roy-tong/Verovo/blob/main/healthcheck/verovo_healthcheck/money.py"><code class="language-plaintext highlighter-rouge">money.py</code>：十進位制显示和最大额分配</a></li>
  <li><a href="https://github.com/roy-tong/Verovo/blob/main/buyer-ledger/buyer_ledger/period_case.py"><code class="language-plaintext highlighter-rouge">period_case.py</code>：快照投影、签收绑定和跨期规则</a></li>
  <li><a href="https://github.com/roy-tong/Verovo/blob/main/healthcheck/verovo_healthcheck/spend_action.py"><code class="language-plaintext highlighter-rouge">spend_action.py</code>：行级买家工作列表</a></li>
  <li><a href="https://github.com/jarrodwatts/claude-hud/pull/758">克劳德-胡德公关#758</a></li>
</ul>


  </div>

  

<aside class="kb-related" aria-label="相关研究材料">
  <h2>相关研究材料</h2>
  <p>在研究图书馆中探索相关报告、数据摘要和笔记。 这些链接显示了主题联系；文章本身引用了直接证据。</p>
  
  <ul>
    
  </ul>
  <ul>
    
      
        <li><a href="/knowledge/agent-measurement/">代理测量</a></li>
      
    
      
        <li><a href="/knowledge/evidence-maintenance/">证据维护</a></li>
      
    
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
