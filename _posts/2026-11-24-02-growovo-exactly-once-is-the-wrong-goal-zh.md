---
title: "Growovo：一次执行是错误的目标"
date: "2026-11-24 12:03:00 +0800"
description: "Approval fingerprints, capability derivation, attempt leases, durable ingress, and independent readback for authorized execution."
permalink: "/notes/02-growovo-exactly-once-is-the-wrong-goal/"
content_id: 02-growovo-exactly-once-is-the-wrong-goal
knowledge_topic: agent-systems
knowledge_units: [agent-measurement, evidence-maintenance]
translation_of: /en/notes/02-growovo-exactly-once-is-the-wrong-goal/
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




      <link rel="alternate" hreflang="en" href="https://roy-tong.github.io/en/notes/02-growovo-exactly-once-is-the-wrong-goal/">
      <link rel="alternate" hreflang="zh-CN" href="https://roy-tong.github.io/notes/02-growovo-exactly-once-is-the-wrong-goal/">
      <link rel="alternate" hreflang="x-default" href="https://roy-tong.github.io/notes/02-growovo-exactly-once-is-the-wrong-goal/">
    <link type="application/atom+xml" rel="alternate" href="https://roy-tong.github.io/feed.xml" title="Roy.Tong"/>
    <!-- Begin Jekyll SEO tag v2.8.0 -->
<title>Growovo：一次执行是错误的目标 | Roy.Tong</title>
<meta name="generator" content="Jekyll v3.9.5"/>
<meta property="og:title" content="Growovo：一次执行是错误的目标">
<meta name="author" content="Roy.Tong"/>
<meta property="og:locale" content="zh_CN">
<meta name="description" content="Approval fingerprints, capability derivation, attempt leases, durable ingress, and independent readback for authorized execution."/>
<meta property="og:description" content="Approval fingerprints, capability derivation, attempt leases, durable ingress, and independent readback for authorized execution."/>
<link rel="canonical" href="https://roy-tong.github.io/notes/02-growovo-exactly-once-is-the-wrong-goal/">
<meta property="og:url" content="https://roy-tong.github.io/notes/02-growovo-exactly-once-is-the-wrong-goal/">
<meta property="og:site_name" content="Roy.Tong"/>
<meta property="og:image" content="https://roy-tong.github.io/assets/images/social-preview.png"/>
<meta property="og:type" content="article"/>
<meta property="article:published_time" content="2026-11-24T12:03:00+08:00"/>
<meta name="twitter:card" content="summary_large_image"/>
<meta property="twitter:image" content="https://roy-tong.github.io/assets/images/social-preview.png"/>
<meta property="twitter:title" content="Growovo：一次执行是错误的目标">
<script type="application/ld+json">
{"@context":"https://schema.org","@type":"BlogPosting","author":{"@type":"Person","name":"Roy.Tong"},"dateModified":"2026-11-24T12:03:00+08:00","datePublished":"2026-11-24T12:03:00+08:00","description":"Approval fingerprints, capability derivation, attempt leases, durable ingress, and independent readback for authorized execution.","headline":"Growovo: exactly-once execution is the wrong goal","image":"https://roy-tong.github.io/assets/images/social-preview.png","mainEntityOfPage":{"@type":"WebPage","@id":"https://roy-tong.github.io/en/notes/02-growovo-exactly-once-is-the-wrong-goal/"},"publisher":{"@type":"Organization","logo":{"@type":"ImageObject","url":"https://roy-tong.github.io/assets/images/social-preview.png"},"name":"Roy.Tong"},"url":"https://roy-tong.github.io/en/notes/02-growovo-exactly-once-is-the-wrong-goal/"}</script>
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
            <a class="language-toggle" href="/en/notes/02-growovo-exactly-once-is-the-wrong-goal/" hreflang="en" lang="en" data-language-switch data-target-language="en" aria-label="切换至中文" title="切换至中文">中文</a>
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

    <main id="main"><p class="translation-note" aria-label="翻译说明">机器辅助翻译。<a href="/en/notes/02-growovo-exactly-once-is-the-wrong-goal/">阅读英文原文</a>。</p>
      




<article class="post shell reading-shell">
  <header class="post-header">
    <a class="eyebrow back-link" href="/archive/">← 所有写作</a>
    <h1>Growovo：完全执行一次是错误的目标</h1>
    <p class="post-subtitle">批准指纹、能力推导、尝试租赁、持久入口和授权执行的独立回读。</p>
    <div class="post-meta">
      <time datetime="2026-11-24T12:03:00+08:00">2026年11月24日</time>
      <span>10分钟阅读</span>
      
      <a class="post-translation" href="/en/notes/02-growovo-exactly-once-is-the-wrong-goal/" hreflang="en">Read in English →</a>
      
        <span class="post-tags">
          <a href="/tags/#ai%20agent">#人工智能代理</a>
        </span>
      
    </div>
  </header>

  <div class="prose">
    <blockquote>
  <p>实施边界：本文涵盖了通过0.20.0发布的Growovo核心和2026年11月24日的内部开发树。 下面描述的SQLite增长运行时、GitHub应用程序运算符、Gmail双向同步和结构化功能模型在该开发树中实现和离线测试；它们没有在编号版本中或公开<code class="language-plaintext highlighter-rouge">main</code>在撰写本文时，真正的GitHub应用程序和Gmail写金丝雀尚未完成。</p>
</blockquote>

<p>在服务器创建了注释后，POST超时。 工人接下来应该做什么？</p>

<p>重试可能会创建重复项。 将操作标记为失败可能会记录一些不再真实的东西。 报告成功将朝着不同的方向乐观。 网络无法告诉工人超时的哪一方赢得了比赛，任何本地交易日志记录都不会改变这一点。</p>

<p>这就是为什么“精确一次执行”对于写入外部系统的代理来说是错误的目标。 有用的目标更加具体：</p>

<ul>
  <li>不要执行已批准的意图已经改变的工作；</li>
  <li>当第一次结果未知时，不要发出第二次尝试；</li>
  <li>即使重复交付，也使入站处理冪等；</li>
  <li>通过独立读取验证外部状态；</li>
  <li>保留未解决的结果，直到一个人或只读和解可以决定它。</li>
</ul>

<p>Growovo最近的工作是围绕这些目标组织的。 与自主增长守护程序相比，该设计不那么迷人。 从可靠性工程的角度来看，这也更有趣。</p>

<h2 id="approval-covers-bytes-identity-and-location">批准涵盖字节、身份和位置</h2>

<p>A<code class="language-plaintext highlighter-rouge">human_approved=true</code>旗帜没有说明批准的内容。 Growovo用四个输入的执行指纹取代了这种模糊性：</p>

<div class="language-python highlighter-rouge"><div class="highlight"><pre class="highlight"><code><span class="n">payload</span> <span class="o">=</span> <span class="p">{</span>
    <span class="s">"plan"</span><span class="p">:</span> <span class="p">{</span><span class="n">k</span><span class="p">:</span> <span class="n">v</span> <span class="k">for</span> <span class="n">k</span><span class="p">,</span> <span class="n">v</span> <span class="ow">in</span> <span class="n">plan</span><span class="p">.</span><span class="n">items</span><span class="p">()</span> <span class="k">if</span> <span class="n">k</span> <span class="o">!=</span> <span class="s">"review"</span><span class="p">},</span>
    <span class="s">"queues"</span><span class="p">:</span> <span class="n">resolved_queues_with_sorted_items</span><span class="p">,</span>
    <span class="s">"workspace"</span><span class="p">:</span> <span class="n">resolved_workspace</span><span class="p">,</span>
    <span class="s">"account"</span><span class="p">:</span> <span class="n">resolved_account</span><span class="p">,</span>
<span class="p">}</span>
<span class="n">fingerprint</span> <span class="o">=</span> <span class="n">sha256</span><span class="p">(</span><span class="n">canonical_json</span><span class="p">(</span><span class="n">payload</span><span class="p">))</span>
</code></pre></div></div>

<p>规范形式是Python JSON序列化，带有排序键和紧凑的分隔符。 队列项目在哈希之前进行排序，并包括已解决的队列路径。 因此，目标、身体、行动、平台、帐户和工作区都会影响指纹。</p>

<p>批准不仅仅是对这个有效载荷的签名。 在写之前，<code class="language-plaintext highlighter-rouge">approve_plan</code>运行：</p>

<div class="language-text highlighter-rouge"><div class="highlight"><pre class="highlight"><code>lint_plan
→ load every declared queue (a missing queue is an error)
→ lint_queue for each bound queue
→ campaign.preflight for content and target gates
→ compute execution fingerprint
→ write plan.review
→ save an approval snapshot
→ append an event to approvals.jsonl
</code></pre></div></div>

<p>结果记录包括<code class="language-plaintext highlighter-rouge">approved_by</code>, <code class="language-plaintext highlighter-rouge">approved_at</code>，可选到期，<code class="language-plaintext highlighter-rouge">fingerprint_scope=plan+queue+account+workspace</code>，以及一个快照路径。 执行重新计算指纹。 编辑正文、替换收件人、更改帐户或移动工作区会使旧的批准无效。</p>

<p>有一个明确的兼容性例外：传统计划与<code class="language-plaintext highlighter-rouge">human_approved=true</code>但没有指纹可以运行并被标记<code class="language-plaintext highlighter-rouge">legacy</code>。 该例外情况对安全审查很重要。 它保留了旧的工作区，但并不等同于更强的指纹保证。</p>

<h2 id="capability-is-a-derived-view-not-a-boolean">能力是一个派生视图，而不是布尔值</h2>

<p>开发树在意图和执行之间增加了另一层。 能力记录由以下方式输入：</p>

<div class="language-text highlighter-rouge"><div class="highlight"><pre class="highlight"><code>(account, platform, action, route)
</code></pre></div></div>

<p>对于每条路线，<code class="language-plaintext highlighter-rouge">read</code>, <code class="language-plaintext highlighter-rouge">write</code>，还有<code class="language-plaintext highlighter-rouge">verify</code>是独立的操作。 唱片店分开<code class="language-plaintext highlighter-rouge">implemented</code>, <code class="language-plaintext highlighter-rouge">available</code>，还有<code class="language-plaintext highlighter-rouge">verified</code>数组，有两个子集不变量：</p>

<div class="language-text highlighter-rouge"><div class="highlight"><pre class="highlight"><code>verified ⊆ implemented
available ⊆ implemented
</code></pre></div></div>

<p>每个经过验证的操作都需要验证证据参考和<code class="language-plaintext highlighter-rouge">last_verified_at</code>。 授权必须是<code class="language-plaintext highlighter-rouge">active</code>，有一个非空的范围，并且没有过期。 凭据从能力记录中递归拒绝。</p>

<p>每个视图都得出了准备：</p>

<div class="language-python highlighter-rouge"><div class="highlight"><pre class="highlight"><code><span class="n">missing</span> <span class="o">=</span> <span class="p">[]</span>
<span class="k">for</span> <span class="n">operation</span> <span class="ow">in</span> <span class="n">required</span><span class="p">:</span>
    <span class="k">if</span> <span class="ow">not</span> <span class="n">implemented</span><span class="p">(</span><span class="n">operation</span><span class="p">):</span> <span class="n">missing</span><span class="p">.</span><span class="n">append</span><span class="p">(</span><span class="sa">f</span><span class="s">"</span><span class="si">{</span><span class="n">operation</span><span class="si">}</span><span class="s">_not_implemented"</span><span class="p">)</span>
    <span class="k">elif</span> <span class="ow">not</span> <span class="n">available</span><span class="p">(</span><span class="n">operation</span><span class="p">):</span> <span class="n">missing</span><span class="p">.</span><span class="n">append</span><span class="p">(</span><span class="sa">f</span><span class="s">"</span><span class="si">{</span><span class="n">operation</span><span class="si">}</span><span class="s">_unavailable"</span><span class="p">)</span>
    <span class="k">if</span> <span class="ow">not</span> <span class="n">verified</span><span class="p">(</span><span class="n">operation</span><span class="p">):</span>    <span class="n">missing</span><span class="p">.</span><span class="n">append</span><span class="p">(</span><span class="sa">f</span><span class="s">"</span><span class="si">{</span><span class="n">operation</span><span class="si">}</span><span class="s">_not_verified"</span><span class="p">)</span>

<span class="n">executable</span> <span class="o">=</span> <span class="n">authorized_now</span> <span class="ow">and</span> <span class="ow">not</span> <span class="n">paused_reason</span> <span class="ow">and</span> <span class="ow">not</span> <span class="n">missing</span>
</code></pre></div></div>

<p>这是故意比<code class="language-plaintext highlighter-rouge">available=true</code>。 可以实现GitHub应用程序，其令牌可能工作，其写入路径可能已通过金丝雀，而独立回读仍然未经验证。 当...时，该路线不可执行<code class="language-plaintext highlighter-rouge">verify</code>是必需的。 暂停的帐户可以阻止自己的路由，而不会禁用不相关的健康帐户。</p>

<p>行动解析器行走<code class="language-plaintext highlighter-rouge">preferred_transports</code>按顺序。 使用结构化功能集，它返回第一个匹配路由，其衍生<code class="language-plaintext highlighter-rouge">executable</code>是真的。 否则，它会返回累积的缺失原因，然后要么是手动工作包，要么是<code class="language-plaintext highlighter-rouge">LIVE_BLOCKED</code>，取决于行动的回退政策。 它不会默默地将请求的现场动作变成试运行。 预览是明确的执行意图。</p>

<p>MCP可以读取这些能力记录，但不能提出自己的验证声明。 否则，代理只需更自信地描述它，就可以改善其权限。</p>

<h2 id="the-durable-unit-is-an-attempt-not-a-queue-row">耐用单元是尝试，而不是排队行</h2>

<p>当前运行时使用SQLite作为其权威存储。 它的中央表格揭示了预期的故障模型：</p>

<div class="language-sql highlighter-rouge"><div class="highlight"><pre class="highlight"><code><span class="n">attempts</span><span class="p">(</span>
  <span class="n">attempt_id</span> <span class="nb">TEXT</span> <span class="k">PRIMARY</span> <span class="k">KEY</span><span class="p">,</span>
  <span class="n">service_id</span> <span class="nb">TEXT</span><span class="p">,</span>
  <span class="n">action_id</span> <span class="nb">TEXT</span><span class="p">,</span>
  <span class="n">worker</span> <span class="nb">TEXT</span><span class="p">,</span>
  <span class="n">intent_sha256</span> <span class="nb">TEXT</span><span class="p">,</span>
  <span class="n">status</span> <span class="nb">TEXT</span><span class="p">,</span>
  <span class="n">lease_expires_at</span> <span class="nb">INTEGER</span><span class="p">,</span>
  <span class="k">external</span> <span class="nb">INTEGER</span><span class="p">,</span>
  <span class="n">evidence_json</span> <span class="nb">TEXT</span><span class="p">,</span>
  <span class="p">...</span>
<span class="p">)</span>

<span class="n">source_events</span><span class="p">(</span>
  <span class="k">source</span> <span class="nb">TEXT</span><span class="p">,</span>
  <span class="n">source_event_id</span> <span class="nb">TEXT</span><span class="p">,</span>
  <span class="n">service_id</span> <span class="nb">TEXT</span><span class="p">,</span>
  <span class="n">event_type</span> <span class="nb">TEXT</span><span class="p">,</span>
  <span class="n">payload_json</span> <span class="nb">TEXT</span><span class="p">,</span>
  <span class="n">processed</span> <span class="nb">INTEGER</span><span class="p">,</span>
  <span class="p">...</span>
  <span class="k">PRIMARY</span> <span class="k">KEY</span><span class="p">(</span><span class="k">source</span><span class="p">,</span> <span class="n">source_event_id</span><span class="p">,</span> <span class="n">service_id</span><span class="p">)</span>
<span class="p">)</span>

<span class="n">scheduled_jobs</span><span class="p">(</span>
  <span class="n">job_id</span> <span class="nb">TEXT</span><span class="p">,</span>
  <span class="n">intent_sha256</span> <span class="nb">TEXT</span><span class="p">,</span>
  <span class="n">status</span> <span class="nb">TEXT</span><span class="p">,</span>
  <span class="n">result_json</span> <span class="nb">TEXT</span><span class="p">,</span>
  <span class="k">external</span> <span class="nb">INTEGER</span><span class="p">,</span>
  <span class="p">...</span>
  <span class="k">PRIMARY</span> <span class="k">KEY</span><span class="p">(</span><span class="n">job_id</span><span class="p">,</span> <span class="n">intent_sha256</span><span class="p">)</span>
<span class="p">)</span>
</code></pre></div></div>

<p>服务有一个版本号。 更新运行在<code class="language-plaintext highlighter-rouge">BEGIN IMMEDIATE</code>，并且只有在开始读取的版本仍然匹配时，更新才会成功：</p>

<div class="language-sql highlighter-rouge"><div class="highlight"><pre class="highlight"><code><span class="k">UPDATE</span> <span class="n">services</span>
<span class="k">SET</span> <span class="n">service_json</span> <span class="o">=</span> <span class="o">?</span><span class="p">,</span> <span class="k">version</span> <span class="o">=</span> <span class="k">version</span> <span class="o">+</span> <span class="mi">1</span><span class="p">,</span> <span class="n">updated_at</span> <span class="o">=</span> <span class="o">?</span>
<span class="k">WHERE</span> <span class="n">service_id</span> <span class="o">=</span> <span class="o">?</span> <span class="k">AND</span> <span class="k">version</span> <span class="o">=</span> <span class="o">?</span><span class="p">;</span>
</code></pre></div></div>

<p>零行更新是版本冲突，而不是最后作者获胜的合并。</p>

<p>现有的JSON和JSONL文件仍然是兼容性预测。 SQLite和文件系统不是神奇的一个原子存储系统；相反，该设计使SQLite具有权威性，投影可重建。 计划作业在写入遗留状态文件之前记录其最终结果，因此投影写入失败不会导致成功的外部作业再次执行。</p>

<h2 id="expiry-has-different-semantics-for-local-and-external-work">到期对本地和外部工作有不同的语义</h2>

<p>声明操作会使用UUID、工人身份、有效负载哈希和租赁创建尝试。 第二个索赔人看到了主动尝试，而不是创建另一个尝试；如果其有效负载哈希不同，结果会携带<code class="language-plaintext highlighter-rouge">intent_mismatch</code>.</p>

<p>动作状态机器大约是：</p>

<div class="language-text highlighter-rouge"><div class="highlight"><pre class="highlight"><code>pending ──claim──&gt; in_progress ──accepted evidence──&gt; completed
                     │
                     ├──────────────────────────────&gt; waiting_manual
                     │
                     ├─local attempt expired────────&gt; pending
                     │
                     └─external attempt expired─────&gt; waiting_verification
                                                        │
                                                        ├─one verified match──&gt; completed
                                                        ├─zero matches────────&gt; unresolved
                                                        └─multiple matches────&gt; manual review
</code></pre></div></div>

<p>尝试表区分了<code class="language-plaintext highlighter-rouge">expired_retryable</code>来自<code class="language-plaintext highlighter-rouge">expired_unknown</code>。 本地无副作用的工作可以回到<code class="language-plaintext highlighter-rouge">pending</code>。 外部工作变成了<code class="language-plaintext highlighter-rouge">waiting_verification</code>并且保持不可运行。 调度员不会再次要求已完成的、手动等待或等待验证的操作。</p>

<p>这是对一次幻想的实用替代品：<strong>一个主动声明、显式不确定性和只读恢复。</strong></p>

<p>同样的规则也适用于具有外部影响的预定作业。 如果之前的索赔仍未解决，下一个排班标记将返回<code class="language-plaintext highlighter-rouge">needs_reconciliation</code>而不是执行副本。</p>

<h2 id="inbound-events-can-be-at-least-once-projection-must-be-idempotent">入站事件至少可以是一次；投影必须是冪等的</h2>

<p>GitHub应用程序进入从HMAC-SHA256签名验证开始，使用<code class="language-plaintext highlighter-rouge">hmac.compare_digest</code>。 HTTP服务器最多接受1 MiB，并默认绑定到回环。 支持的事件仅限于已打开的问题、已创建的问题评论、已创建的讨论和已创建的讨论评论。</p>

<p>处理是一个两步持久性协议：</p>

<ol>
  <li><code class="language-plaintext highlighter-rouge">INSERT OR IGNORE</code>原始有效载荷进入<code class="language-plaintext highlighter-rouge">source_events</code>使用<code class="language-plaintext highlighter-rouge">(source, source_event_id, service_id)</code>作为钥匙。</li>
  <li>在交易中，将存储的有效负载投射到对话模型中，并将源事件标记为已处理。</li>
</ol>

<p>因此，重复交付是数据库重复，而不是新的对话或操作。 如果投影失败，原始事件仍处于待定状态，可以重播。 对话键保留了问题和讨论之间的区别：</p>

<div class="language-text highlighter-rouge"><div class="highlight"><pre class="highlight"><code>owner/repo#7                  # Issue and all of its comments
owner/repo/discussion#12      # Discussion and all of its comments
</code></pre></div></div>

<p>每个互动 ID 都会被保留。 外部文本被标记<code class="language-plaintext highlighter-rouge">untrusted_external_content</code>；接收webhook并不能使其主体成为对代理的指令。</p>

<p>Gmail使用具有相同冪等目标的不同光标机制。 初始同步列举收件箱消息并记录最大值<code class="language-plaintext highlighter-rouge">historyId</code>。 增量同步随之而来<code class="language-plaintext highlighter-rouge">history.list</code>，在运行中重复消息ID。 过期历史记录光标的404会触发完全重新同步，而不是空的“成功”。 光标仅在消息被摄取并待处理事件重播后才会前进。 Pub/Sub通知只有在相应的同步成功后才会被确认；通知被视为同步的提示，而不是消息本身。</p>

<p>这些机制接受重复的输入，因此系统不会丢失输入。 持久的身份和交易预测可以防止这种选择成为重复的业务工作。</p>

<h2 id="outbound-success-requires-an-independent-read">出站成功需要独立阅读</h2>

<p>写入API的返回值是执行者观察到的收据。 它是有用的，但它不是独立的最终状态证据。</p>

<p>因此，GitHub运算符跟随一个带有独立GET的回复。 验证检查评论ID或URL、正文、作者和目标问题。 讨论回复通过GraphQL遵循相同的模式：<code class="language-plaintext highlighter-rouge">addDiscussionComment</code>必须返回完整的评论收据，然后<code class="language-plaintext highlighter-rouge">node(id: ...)</code>独立查询。 Gmail回复通过单独的线程/消息读取线程、收件人和正文进行检查。</p>

<p>和解永远不会再发送。 它搜索外部系统：</p>

<ul>
  <li>一个匹配的对象完成了最初的尝试；</li>
  <li>零匹配让结果未解决；</li>
  <li>多个匹配需要人工审核。</li>
</ul>

<p>该规则还防止模棱两可的阅读成为另一个写作的借口。</p>

<h2 id="proof-export-keeps-execution-final-state-and-business-events-apart">证明导出将执行、最终状态和业务事件分开</h2>

<p>Growovo的只读证明导出器将这些证据类型映射到不同的级别。</p>

<p>对于每个操作，P0检查都会记录执行者观察到的结果：</p>

<ul>
  <li><code class="language-plaintext highlighter-rouge">committed</code> → <code class="language-plaintext highlighter-rouge">PASS</code>;</li>
  <li><code class="language-plaintext highlighter-rouge">failed</code> → <code class="language-plaintext highlighter-rouge">FAIL</code>;</li>
  <li><code class="language-plaintext highlighter-rouge">indeterminate</code> → <code class="language-plaintext highlighter-rouge">INDETERMINATE</code>;</li>
  <li>试运行、被拒绝和其他未执行的状态→<code class="language-plaintext highlighter-rouge">UNCHECKED</code>.</li>
</ul>

<p>P2最终状态检查要严格得多。 电流<code class="language-plaintext highlighter-rouge">readback_ok</code>谓词需要经过验证的回读绑定到相同的操作、渠道、操作、目标、完整内容哈希、收据身份、帐户、完成时间和回读源。 缺少或不匹配的证据离开P2<code class="language-plaintext highlighter-rouge">UNCHECKED</code>；执行人的承诺行不能提升自己。</p>

<p>外部产品事件成为P4检查。 经过验证的事件可以通过；未经验证的事件是<code class="language-plaintext highlighter-rouge">INDETERMINATE</code>。 没有事件产生P4<code class="language-plaintext highlighter-rouge">UNCHECKED</code>覆盖范围检查。 捆绑包显式设置<code class="language-plaintext highlighter-rouge">causality=not_claimed</code>.</p>

<p>离线演示使这一点变得具体。 我在临时工作区运行它并检查了<code class="language-plaintext highlighter-rouge">checks.json</code>:</p>

<div class="language-text highlighter-rouge"><div class="highlight"><pre class="highlight"><code>summary-readable                 P1  PASS
execution:&lt;committed operation&gt;  P0  PASS
final-state:&lt;same operation&gt;     P2  UNCHECKED
execution:&lt;dry-run operation&gt;    P0  UNCHECKED
execution:&lt;rejected operation&gt;   P0  UNCHECKED
execution:&lt;failed operation&gt;     P0  FAIL
external-business-events         P4  UNCHECKED
replay.status                        UNAVAILABLE
replay.missing                     operations.jsonl
</code></pre></div></div>

<p>提交的沙盒操作不会接收P2，因为内存内演示收据不是独立的外部最终状态。 一个故意失败的夹具使整体证明<code class="language-plaintext highlighter-rouge">FAIL</code>。 这是一个比统一绿色演示更有用的测试：它行使聚合、负状态以及可读证据和商业结果之间的差异。</p>

<p>您可以使用以下方式重现演示：</p>

<div class="language-bash highlighter-rouge"><div class="highlight"><pre class="highlight"><code>pipx <span class="nb">install </span>growovo
mkt demo
</code></pre></div></div>

<p>或者检查<a href="https://roy-tong.github.io/Growovo/examples/controlled-run.en.html">受控运行页面</a>.</p>

<h2 id="business-observations-need-matching-pairs">业务观察需要匹配对</h2>

<p>执行证据只有一层。 Growovo 0.20.0区分<code class="language-plaintext highlighter-rouge">owner_declared</code>, <code class="language-plaintext highlighter-rouge">observed</code>，还有<code class="language-plaintext highlighter-rouge">independently_verified</code>商业观察。 更强有力的观察需要哈希约束的证据、主题身份和度量定义版本。 独立验证还需要独立的控制域、权威、验证结果和审查收据。</p>

<p>前后比较需要相同的观察对、主题和定义，基线时间在最终时间之前。 后来的基线使旧对无效，而不是追溯性地改进故事。 有效的delta仍然没有因果关系。</p>

<p>这种区别来自于操作课程。 一次内部交接记录了X、GitHub和Discord的12波503个承诺操作，同时三个OVO存储库的零星增长，没有可读的外部用户计数。 这不是一个受控实验，但它使一个测量错误站不住钒：将执行者产生的卷视为用户价值。</p>

<p>因此，第二批是一个单独的证据事件。 它应该测试抑制、身份、未解决的收据、能力状态和指标定义是否在新的授权输入集中幸存下来。 重复相同的夹具证明了决定性，而不是持续的有用性。</p>

<h2 id="what-the-implementation-proves-so-far">到目前为止，实施证明了什么</h2>

<p>在供应商执行、配额保留或提交分类账附加之前，发布的0.18.1边界拒绝所有脚本化的非API X浏览器写入。 本地运营商授权和登录的浏览器不被视为平台权限。 只读集合、显式预览、草稿和人工操作仍然分开。</p>

<p>在这篇文章中，我还运行了开发树功能、并发域、签名的GitHub黄金链和Gmail测试：13次通过。 它们涵盖了独立的读/写/验证要求、过期和帐户隔离、没有兼容性JSON的SQLite权限、重复签名的webhook提交、独立的Gmail回读、历史-404恢复以及成功同步后的Pub/Sub确认。</p>

<p>这些测试使用临时目录、模拟平台传输和本地HTTP/SQLite流。 他们没有建立真正的GitHub应用程序或Gmail写入金丝雀、用户激活或收入。 下一个工程里程碑相应地狭窄：针对授权目标运行这些金丝雀，并将其外部回读与已存储的尝试进行比较。 可靠性索赔应该以与证据相同的速度增长。</p>

<h3 id="source-and-verification-links">来源和验证链接</h3>

<ul>
  <li><a href="https://github.com/roy-tong/Growovo/blob/main/core/approval.py"><code class="language-plaintext highlighter-rouge">approval.py</code>：执行指纹和批准快照</a></li>
  <li><a href="https://github.com/roy-tong/Growovo/blob/main/core/proof_export.py"><code class="language-plaintext highlighter-rouge">proof_export.py</code>：P0/P2/P4映射和回读谓词</a></li>
  <li><a href="https://github.com/roy-tong/Growovo/blob/main/core/business_observations.py"><code class="language-plaintext highlighter-rouge">business_observations.py</code>：观察等级和比较对</a></li>
  <li><a href="https://github.com/roy-tong/Growovo/blob/main/docs/feature-status.md">Growovo实施状态，包括开发树边界</a></li>
  <li><a href="https://roy-tong.github.io/Growovo/examples/controlled-run.en.html">受控运行示例</a></li>
  <li><a href="https://github.com/roy-tong/Growovo/blob/main/CHANGELOG.md">Growovo更改日志</a></li>
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
