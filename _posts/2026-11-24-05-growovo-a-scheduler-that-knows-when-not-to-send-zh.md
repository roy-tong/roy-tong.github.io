---
title: "Growovo：一个知道何时不发送的调度器"
date: "2026-11-24 12:04:00 +0800"
description: "Eligibility filters, stable action identity, UTC budgets, stale-draft pruning, adaptive ordering, and channel recovery."
permalink: "/notes/05-growovo-a-scheduler-that-knows-when-not-to-send/"
content_id: 05-growovo-a-scheduler-that-knows-when-not-to-send
knowledge_topic: agent-systems
knowledge_units: [agent-measurement, evidence-maintenance]
translation_of: /en/notes/05-growovo-a-scheduler-that-knows-when-not-to-send/
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




      <link rel="alternate" hreflang="en" href="https://roy-tong.github.io/en/notes/05-growovo-a-scheduler-that-knows-when-not-to-send/">
      <link rel="alternate" hreflang="zh-CN" href="https://roy-tong.github.io/notes/05-growovo-a-scheduler-that-knows-when-not-to-send/">
      <link rel="alternate" hreflang="x-default" href="https://roy-tong.github.io/notes/05-growovo-a-scheduler-that-knows-when-not-to-send/">
    <link type="application/atom+xml" rel="alternate" href="https://roy-tong.github.io/feed.xml" title="Roy.Tong"/>
    <!-- Begin Jekyll SEO tag v2.8.0 -->
<title>Growovo：一个知道何时不发送的调度器 | Roy.Tong</title>
<meta name="generator" content="Jekyll v3.9.5"/>
<meta property="og:title" content="Growovo：一个知道何时不发送的调度器">
<meta name="author" content="Roy.Tong"/>
<meta property="og:locale" content="zh_CN">
<meta name="description" content="Eligibility filters, stable action identity, UTC budgets, stale-draft pruning, adaptive ordering, and channel recovery."/>
<meta property="og:description" content="Eligibility filters, stable action identity, UTC budgets, stale-draft pruning, adaptive ordering, and channel recovery."/>
<link rel="canonical" href="https://roy-tong.github.io/notes/05-growovo-a-scheduler-that-knows-when-not-to-send/">
<meta property="og:url" content="https://roy-tong.github.io/notes/05-growovo-a-scheduler-that-knows-when-not-to-send/">
<meta property="og:site_name" content="Roy.Tong"/>
<meta property="og:image" content="https://roy-tong.github.io/assets/images/social-preview.png"/>
<meta property="og:type" content="article"/>
<meta property="article:published_time" content="2026-11-24T12:04:00+08:00"/>
<meta name="twitter:card" content="summary_large_image"/>
<meta property="twitter:image" content="https://roy-tong.github.io/assets/images/social-preview.png"/>
<meta property="twitter:title" content="Growovo：一个知道何时不发送的调度器">
<script type="application/ld+json">
{"@context":"https://schema.org","@type":"BlogPosting","author":{"@type":"Person","name":"Roy.Tong"},"dateModified":"2026-11-24T12:04:00+08:00","datePublished":"2026-11-24T12:04:00+08:00","description":"Eligibility filters, stable action identity, UTC budgets, stale-draft pruning, adaptive ordering, and channel recovery.","headline":"Growovo: a scheduler that knows when not to send","image":"https://roy-tong.github.io/assets/images/social-preview.png","mainEntityOfPage":{"@type":"WebPage","@id":"https://roy-tong.github.io/en/notes/05-growovo-a-scheduler-that-knows-when-not-to-send/"},"publisher":{"@type":"Organization","logo":{"@type":"ImageObject","url":"https://roy-tong.github.io/assets/images/social-preview.png"},"name":"Roy.Tong"},"url":"https://roy-tong.github.io/en/notes/05-growovo-a-scheduler-that-knows-when-not-to-send/"}</script>
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
            <a class="language-toggle" href="/en/notes/05-growovo-a-scheduler-that-knows-when-not-to-send/" hreflang="en" lang="en" data-language-switch data-target-language="en" aria-label="切换至中文" title="切换至中文">中文</a>
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

    <main id="main"><p class="translation-note" aria-label="翻译说明">机器辅助翻译。<a href="/en/notes/05-growovo-a-scheduler-that-knows-when-not-to-send/">阅读英文原文</a>。</p>
      




<article class="post shell reading-shell">
  <header class="post-header">
    <a class="eyebrow back-link" href="/archive/">← 所有写作</a>
    <h1>Growovo：一个知道何时不发送的调度器</h1>
    <p class="post-subtitle">资格过滤器、稳定行动身份、UTC预算、陈旧的草稿修剪、自适应订购和渠道恢复。</p>
    <div class="post-meta">
      <time datetime="2026-11-24T12:04:00+08:00">2026年11月24日</time>
      <span>7分钟阅读</span>
      
      <a class="post-translation" href="/en/notes/05-growovo-a-scheduler-that-knows-when-not-to-send/" hreflang="en">Read in English →</a>
      
        <span class="post-tags">
          <a href="/tags/#ai%20agent">#人工智能代理</a>
        </span>
      
    </div>
  </header>

  <div class="prose">
    <p>调度器信息量最大的输出通常是带有确切原因的跳过行。</p>

<p><code class="language-plaintext highlighter-rouge">already_done</code>表示目标分类账显示此回复已经存在。<code class="language-plaintext highlighter-rouge">target_isolated</code>意味着早期的事件使目标不安全。<code class="language-plaintext highlighter-rouge">stale_row</code>意味着批准的时刻已经过去。<code class="language-plaintext highlighter-rouge">daily_quota_exhausted</code>意味着安排行只会在以后失败。 这些不是隐藏在进度条后面的错误字符串。 它们是控制平面。</p>

<p>Growovo的参与周期在考虑任何浏览器操作之前，将规划视为确定性资格计算。 只有在计算之后，自适应执行器才会决定接下来运行哪个符合条件的行。 这种分离使两种错误可以区分：一个不应该符合条件的行，以及一个符合条件的行，其实时顺序效率低下。</p>

<h2 id="action-identity-must-survive-editing">行动身份必须在编辑中幸存下来</h2>

<p>在过滤之前，队列行被归一化为一个共同的形状：通道、操作、目标、文本、行为者和源。 回复身份基于渠道、行动和目标；原始帖子身份还包括文本的前60个字符。</p>

<p>稳定队列ID是：</p>

<div class="language-python highlighter-rouge"><div class="highlight"><pre class="highlight"><code><span class="n">text_part</span> <span class="o">=</span> <span class="s">""</span> <span class="k">if</span> <span class="n">action</span> <span class="o">==</span> <span class="s">"reply"</span> <span class="k">else</span> <span class="n">text</span><span class="p">[:</span><span class="mi">60</span><span class="p">]</span>
<span class="n">raw</span> <span class="o">=</span> <span class="sa">f</span><span class="s">"</span><span class="si">{</span><span class="n">channel</span><span class="si">}</span><span class="s">|</span><span class="si">{</span><span class="n">action</span><span class="si">}</span><span class="s">|</span><span class="si">{</span><span class="n">target</span><span class="si">}</span><span class="s">|</span><span class="si">{</span><span class="n">text_part</span><span class="si">}</span><span class="s">"</span>
<span class="n">stable_id</span> <span class="o">=</span> <span class="s">"q:"</span> <span class="o">+</span> <span class="n">sha1</span><span class="p">(</span><span class="n">raw</span><span class="p">)[:</span><span class="mi">12</span><span class="p">]</span>
</code></pre></div></div>

<p>回复可以重写，而不会成为新的业务操作。 这对于操作日志和重复数据删除很重要：填写空的收件箱草稿或改进其措辞不得产生两个独立的尝试来回答同一线程。 原始帖子需要不同的处理，因为同一帐户可能会故意向同一目的地发布不同的内容。</p>

<p>重复数据删除使用相同的语义。 一个目标的两个回复行是重复的，即使它们的文本不同。 然后，分类账检查回答了一个单独的问题：是否已经观察到该目标的已提交回复？ 队列重复和外部执行历史是相关的，但不能互换。</p>

<h2 id="planning-is-a-pipeline-of-refusals">计划是一条拒绝的管道</h2>

<p>规划者读取已承诺的分类账历史、当前政策、队列内容和本地预算。 它的过滤器顺序使故障模式可以检查：</p>

<table>
  <thead>
    <tr>
      <th>时期</th>
      <th>代表拒绝</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>频道保留</td>
      <td><code class="language-plaintext highlighter-rouge">channel_hold</code></td>
    </tr>
    <tr>
      <td>征兵年龄</td>
      <td><code class="language-plaintext highlighter-rouge">stale_row</code></td>
    </tr>
    <tr>
      <td>支持的行动</td>
      <td><code class="language-plaintext highlighter-rouge">unsupported</code></td>
    </tr>
    <tr>
      <td>内容呈现和允许</td>
      <td><code class="language-plaintext highlighter-rouge">text_empty</code>，内容规则原因</td>
    </tr>
    <tr>
      <td>目标合同</td>
      <td><code class="language-plaintext highlighter-rouge">target_required</code>, <code class="language-plaintext highlighter-rouge">channel_not_allowed</code></td>
    </tr>
    <tr>
      <td>队列和目标身份</td>
      <td><code class="language-plaintext highlighter-rouge">duplicate_in_queue</code>, <code class="language-plaintext highlighter-rouge">target_isolated</code>, <code class="language-plaintext highlighter-rouge">already_done</code></td>
    </tr>
    <tr>
      <td>配置的预算</td>
      <td><code class="language-plaintext highlighter-rouge">night_quota_exhausted</code>, <code class="language-plaintext highlighter-rouge">hour_quota_exhausted</code>, <code class="language-plaintext highlighter-rouge">daily_quota_exhausted</code></td>
    </tr>
    <tr>
      <td>独立的安全帽</td>
      <td><code class="language-plaintext highlighter-rouge">safety_cap_missing</code>, <code class="language-plaintext highlighter-rouge">safety_cap_exhausted</code></td>
    </tr>
    <tr>
      <td>波浪组成</td>
      <td><code class="language-plaintext highlighter-rouge">wave_target_met</code>, <code class="language-plaintext highlighter-rouge">actor_cap</code>, <code class="language-plaintext highlighter-rouge">wave_cap</code></td>
    </tr>
    <tr>
      <td>时间预算</td>
      <td><code class="language-plaintext highlighter-rouge">wave_budget</code></td>
    </tr>
  </tbody>
</table>

<p>每个被拒绝的行都会返回通道、操作、目标和原因。 计划本身没有副作用。</p>

<p>仅提交行<code class="language-plaintext highlighter-rouge">transport=browser-attach</code>或者传统的空白传输会消耗夜间和每小时的使用量。 失败的操作不会消耗相同的计数器。 每人上限适用于回复，而不是原始帖子；否则，作为所有者发布三个原始帖子将耗尽所谓的“每晚两个外部人员”的预算。</p>

<p>两个预算层是故意独立的。 背景<code class="language-plaintext highlighter-rouge">quota.enforce=false</code>禁用已配置的夜间/每小时配额拒绝，但不会禁用独立的安全上限层。 旨在减少意外调度摩擦的策略更改不能默默地删除最终停止条件。</p>

<h2 id="budget-days-are-an-accounting-decision">预算日是一个会计决策</h2>

<p>每晚从19:00到07:00的窗口跨越当地午夜。 按本地日历日期划分使用情况会产生两个不好的结果：傍晚时分继承了当天早晨的使用情况，而午夜似乎提供了新的每日津贴。</p>

<p>因此，默认预算边界是上海的UTC午夜08:00，因此整个晚上共享一个预算日。 与UTC窗口重叠的遗留本地日期文件是保守添加的，而不是在迁移期间被忽略。 来电者可以明确选择<code class="language-plaintext highlighter-rouge">day_boundary=local</code>；状态文件名发生变化，这样两个会计系统就不会混淆。</p>

<p>每次运行的切片是机械的：</p>

<div class="language-python highlighter-rouge"><div class="highlight"><pre class="highlight"><code><span class="n">Throttle</span><span class="p">(...).</span><span class="n">slice_batches</span><span class="p">(</span><span class="s">"email"</span><span class="p">,</span> <span class="s">"message"</span><span class="p">,</span> <span class="mi">120</span><span class="p">)</span>
<span class="c1"># cap = 50 → [range(0, 50), range(50, 100), range(100, 120)]
</span></code></pre></div></div>

<p>实际长度是<code class="language-plaintext highlighter-rouge">[50, 50, 20]</code>。 这与...不同<code class="language-plaintext highlighter-rouge">check_run</code>，它拒绝盖子上方的整个批次。 切片允许调用者继续使用推迟的行，而不是将容量视为全有或全无故障。</p>

<p>保留发生在跨进程锁定下的外部写入之前。 如果写入失败或变得未知，保留仍然被消耗。 这是故意保守的：未知的外部结果不能被视为未使用的容量并立即再次花费。</p>

<p>这些是当地的运营预算，而不是关于平台官方限制的声明。 该代码为官方限制保留了单独的参考值，并使用自己的较低预算进行规划。</p>

<h2 id="stale-drafts-expire-conversations-do-not">过时的草稿过期；对话不会</h2>

<p>默认的非收件箱草稿有效期为12小时。 年龄来自<code class="language-plaintext highlighter-rouge">queued_at</code>；遗留行可以倒退到午夜<code class="language-plaintext highlighter-rouge">night-YYYYMMDD</code>竞选活动。 既没有时间戳的行将被视为新行，而不是在没有证据的情况下被丢弃。</p>

<p>通过此规则，收件箱回复永远不会过期。 旧的入站问题仍然是需要处理的对话，尽管其内容和平台状态仍然需要审查。 这避免了一个常见的自动化错误：修剪回答的人，同时保留一批新的冷促销副本。</p>

<p>干运行报告陈旧行，无需更改队列。 真正的运行会修剪陈旧的非收件箱行，而推迟的行仍然可以用于以后的波。 因此，“过期内容”和“暂时无法运行的内容”之间的区别保留在存储中。</p>

<h2 id="the-static-plan-is-not-the-live-order">静态计划不是实时订单</h2>

<p>一旦行符合条件，<code class="language-plaintext highlighter-rouge">choose_next</code>每次操作后重新计算准备情况：</p>

<div class="language-python highlighter-rouge"><div class="highlight"><pre class="highlight"><code><span class="n">channel_ready</span> <span class="o">=</span> <span class="n">last_channel</span><span class="p">[</span><span class="n">channel</span><span class="p">]</span> <span class="o">+</span> <span class="n">channel_gap</span>
<span class="n">global_ready</span> <span class="o">=</span> <span class="n">last_any</span> <span class="o">+</span> <span class="n">global_gap</span>
<span class="n">ready</span> <span class="o">=</span> <span class="nb">max</span><span class="p">(</span><span class="n">channel_ready</span><span class="p">,</span> <span class="n">global_ready</span><span class="p">)</span>
</code></pre></div></div>

<p>获胜者是根据三个有序规则选出的：</p>

<ol>
  <li>最早的<code class="language-plaintext highlighter-rouge">ready</code>时间戳；</li>
  <li>收件箱行赢得平局；</li>
  <li>观察时间最短的行赢得剩余的平局。</li>
</ol>

<p>持续时间估计使用指数移动平均线：</p>

<div class="language-python highlighter-rouge"><div class="highlight"><pre class="highlight"><code><span class="n">new_average</span> <span class="o">=</span> <span class="n">old_average</span> <span class="o">*</span> <span class="mf">0.75</span> <span class="o">+</span> <span class="n">observed_seconds</span> <span class="o">*</span> <span class="mf">0.25</span>
</code></pre></div></div>

<p>没有持续时间观察的行不会发明快速估计。 正的测量持续时间只对未知或更长的持续时间获胜。</p>

<p>我用两个等量准备行直接调用了选择器。 实际的决定是：</p>

<div class="language-text highlighter-rouge"><div class="highlight"><pre class="highlight"><code>queue row + inbox row at the same ready time
→ x / inbox_first

30.0-second GitHub row + 12.5-second X row at the same ready time
→ x / 12.5 seconds / shortest_observed_duration
</code></pre></div></div>

<p>这就是为什么试运行计划是最初的保留，而不是最终执行订单的承诺。 推迟的通道从实时待定集合中删除，允许另一个通道在不减少配置的冷却时间的情况下使用间隙。 每个自适应决策及其定时输入都记录在波摘要中。</p>

<p>后台供应预取也受到类似的限制。 当需要新的候选时，只读发现可以在执行旁边运行，但X搜索被标记为<code class="language-plaintext highlighter-rouge">shared_browser_tab</code>并且不与发送选项卡同时运行。 预取失败不会重写操作结果。</p>

<h2 id="a-channel-needs-a-circuit-breaker-not-a-retry-loop">通道需要断路器，而不是重试循环</h2>

<p>停止状态有三个值：</p>

<div class="language-text highlighter-rouge"><div class="highlight"><pre class="highlight"><code>closed     no stop file; normal scheduling allowed
open       cooling, unresolved, or unreadable timestamp; no sends
half_open  cooldown elapsed; at most one probe action this wave
</code></pre></div></div>

<p>没有可读时间戳的停止文件<code class="language-plaintext highlighter-rouge">open</code>：系统无法证明冷却已经完成。 如果外部结果是<code class="language-plaintext highlighter-rouge">indeterminate</code>，停止记录携带<code class="language-plaintext highlighter-rouge">requires_human_resolution</code>和一个未解决的参考资料。 虽然原始分类账行仍然是不确定的，但后面的波浪仍然开放。</p>

<p>冷却后，波只保留一个探针用于通道，并将其余探针推迟到<code class="language-plaintext highlighter-rouge">stop_probe_pending</code>。 提交的探针清除了停止文件。 任何其他结果都会保留它。 系统不会通过其他渠道重定向相同的内容，以使故障不那么明显。</p>

<p>基础设施的缺席与平台停止是故意不同的。 缺失或隐藏的浏览器选项卡会推迟该通道，而不创建停止文件或收取操作费用。 其他渠道继续。 相比之下，未知的外部结果在命名解决方案之前停止受影响的频道。</p>

<h2 id="a-second-batch-tests-the-reasons-not-just-the-count">第二批测试原因，而不仅仅是计数</h2>

<p>下一个授权批次只有在保留这些区别时才有用。 它应该显示重写的回复是否保留了其身份，抑制和目标隔离是否仍然胜过新内容，未解决的结果是否阻止了另一次尝试，以及新的一天是否继承了正确的遗留用法。</p>

<p>有用的第二批证据包括：</p>

<ul>
  <li>跳过的行及其原因代码，而不仅仅是提交的计数；</li>
  <li>草稿编辑前后的队列ID；</li>
  <li>保留与实际观察到的行动；</li>
  <li>存储中的陈旧和推迟的行；</li>
  <li>适应性调度决策；</li>
  <li>在任何探测前后停止状态；</li>
  <li>人类和解会议记录。</li>
</ul>

<p>我为这篇文章运行了参与周期套件：69次测试通过。 它们涵盖了重写后的回复身份、已回复的目标、演员上限、陈旧修剪、每日和每小时预算、缺失的标签、未知结果停止、单探针恢复、队列锁定、自适应定时和第二波行为。 传输和帐户是模拟的；这些测试建立调度行为，而不是平台有效性或增长结果。</p>

<p>设计的权衡是，Growovo波可能选择做的很少。 空的发送计数可能意味着缺少资格、证据不足、封闭预算或故意停止。 一个好的调度器使这些状态更显眼，而不是将它们视为必须填补的配额。</p>

<h3 id="source-and-verification-links">来源和验证链接</h3>

<ul>
  <li><a href="https://github.com/roy-tong/Growovo/blob/main/core/engagement_cycle.py"><code class="language-plaintext highlighter-rouge">engagement_cycle.py</code>：资格、身份、自适应排序和停止恢复</a></li>
  <li><a href="https://github.com/roy-tong/Growovo/blob/main/core/throttle.py"><code class="language-plaintext highlighter-rouge">throttle.py</code>：UTC预算核算、切片和保留</a></li>
  <li><a href="https://github.com/roy-tong/Growovo/blob/main/core/inbox_replies.py"><code class="language-plaintext highlighter-rouge">inbox_replies.py</code>：入站回复收集</a></li>
  <li><a href="https://github.com/roy-tong/Growovo/blob/main/core/supply_prefetch.py"><code class="language-plaintext highlighter-rouge">supply_prefetch.py</code>：受限的提前阅读</a></li>
  <li><a href="https://github.com/roy-tong/Growovo/blob/main/tests/test_engagement_cycle.py">参与周期测试</a></li>
  <li><a href="https://github.com/roy-tong/Growovo/blob/main/docs/feature-status.md">Growovo实施状态</a></li>
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
