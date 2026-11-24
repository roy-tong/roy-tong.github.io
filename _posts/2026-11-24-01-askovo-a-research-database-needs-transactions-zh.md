---
title: "Askovo：研究数据库需要交易语义"
date: "2026-11-24 12:01:00 +0800"
description: "Evidence graphs, immutable decision records, request-scoped snapshots, and a deterministic response to contradiction."
permalink: "/notes/01-askovo-a-research-database-needs-transactions/"
content_id: 01-askovo-a-research-database-needs-transactions
knowledge_topic: product-research
knowledge_units: [demand-evidence, research-workflows]
translation_of: /en/notes/01-askovo-a-research-database-needs-transactions/
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




      <link rel="alternate" hreflang="en" href="https://roy-tong.github.io/en/notes/01-askovo-a-research-database-needs-transactions/">
      <link rel="alternate" hreflang="zh-CN" href="https://roy-tong.github.io/notes/01-askovo-a-research-database-needs-transactions/">
      <link rel="alternate" hreflang="x-default" href="https://roy-tong.github.io/notes/01-askovo-a-research-database-needs-transactions/">
    <link type="application/atom+xml" rel="alternate" href="https://roy-tong.github.io/feed.xml" title="Roy.Tong"/>
    <!-- Begin Jekyll SEO tag v2.8.0 -->
<title>Askovo：研究数据库需要交易语义 | Roy.Tong</title>
<meta name="generator" content="Jekyll v3.9.5"/>
<meta property="og:title" content="Askovo：研究数据库需要交易语义">
<meta name="author" content="Roy.Tong"/>
<meta property="og:locale" content="zh_CN">
<meta name="description" content="Evidence graphs, immutable decision records, request-scoped snapshots, and a deterministic response to contradiction."/>
<meta property="og:description" content="Evidence graphs, immutable decision records, request-scoped snapshots, and a deterministic response to contradiction."/>
<link rel="canonical" href="https://roy-tong.github.io/notes/01-askovo-a-research-database-needs-transactions/">
<meta property="og:url" content="https://roy-tong.github.io/notes/01-askovo-a-research-database-needs-transactions/">
<meta property="og:site_name" content="Roy.Tong"/>
<meta property="og:image" content="https://roy-tong.github.io/assets/images/social-preview.png"/>
<meta property="og:type" content="article"/>
<meta property="article:published_time" content="2026-11-24T12:01:00+08:00"/>
<meta name="twitter:card" content="summary_large_image"/>
<meta property="twitter:image" content="https://roy-tong.github.io/assets/images/social-preview.png"/>
<meta property="twitter:title" content="Askovo：研究数据库需要交易语义">
<script type="application/ld+json">
{"@context":"https://schema.org","@type":"BlogPosting","author":{"@type":"Person","name":"Roy.Tong"},"dateModified":"2026-11-24T12:01:00+08:00","datePublished":"2026-11-24T12:01:00+08:00","description":"Evidence graphs, immutable decision records, request-scoped snapshots, and a deterministic response to contradiction.","headline":"Askovo: a research database needs transaction semantics","image":"https://roy-tong.github.io/assets/images/social-preview.png","mainEntityOfPage":{"@type":"WebPage","@id":"https://roy-tong.github.io/en/notes/01-askovo-a-research-database-needs-transactions/"},"publisher":{"@type":"Organization","logo":{"@type":"ImageObject","url":"https://roy-tong.github.io/assets/images/social-preview.png"},"name":"Roy.Tong"},"url":"https://roy-tong.github.io/en/notes/01-askovo-a-research-database-needs-transactions/"}</script>
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
            <a class="language-toggle" href="/en/notes/01-askovo-a-research-database-needs-transactions/" hreflang="en" lang="en" data-language-switch data-target-language="en" aria-label="切换至中文" title="切换至中文">中文</a>
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

    <main id="main"><p class="translation-note" aria-label="翻译说明">机器辅助翻译。<a href="/en/notes/01-askovo-a-research-database-needs-transactions/">阅读英文原文</a>。</p>
      




<article class="post shell reading-shell">
  <header class="post-header">
    <a class="eyebrow back-link" href="/archive/">← 所有写作</a>
    <h1>Askovo：研究数据库需要交易语义</h1>
    <p class="post-subtitle">证据图、不可变的决策记录、请求范围的快照以及对矛盾的确定性响应。</p>
    <div class="post-meta">
      <time datetime="2026-11-24T12:01:00+08:00">2026年11月24日</time>
      <span>10分钟阅读</span>
      
      <a class="post-translation" href="/en/notes/01-askovo-a-research-database-needs-transactions/" hreflang="en">Read in English →</a>
      
        <span class="post-tags">
          <a href="/tags/#ai%20agent">#人工智能代理</a>
        </span>
      
    </div>
  </header>

  <div class="prose">
    <p>报告生成器可以容忍过时的读取。 决策系统不应该。</p>

<p>假设审计读取研究的版本A。 在渲染最终简报之前，另一个进程会附加反证据并提交版本B。 如果简报将A用于一个部分，B用于另一个部分，则每个单独的输入都可能有效。 由此产生的报告仍然是错误的：从未存在过这样的研究修订。</p>

<p>Askovo 2.22通过提供研究请求快照和交易语义来解决这一类故障。 后续的2.22.1版本填补了两个不太明显的差距：请求快照可能与旧的32个条目解析数据缓存的交互不良，两个进程在获取附加锁之前可能会通过观察身份检查。</p>

<p>这项工作是检查产品的有用视角。 Askovo并没有试图使一个流畅的报告成为真理的单位。 它在证据、推断、决策和随后的观察之间保持了版本化的关系。 数据库层是研究方法的一部分。</p>

<h2 id="the-canonical-objects-are-smaller-than-the-reports">规范对象比报告小</h2>

<p>一项研究有几个文件，故意有不同的责任：</p>

<div class="language-text highlighter-rouge"><div class="highlight"><pre class="highlight"><code>study.json                              # question, owner, scope, method
02-data/evidence.jsonl                  # registered evidence and provenance
04-findings/demand-judgments.json       # demand/commercial evidence judgments
04-findings/product-reasoning.json      # live product/business reasoning
01-sources/observations.jsonl           # product-behavior observations
05-audit/                               # generated audit outputs
06-report/                              # generated projections
</code></pre></div></div>

<p>实时推理脊柱是：</p>

<div class="language-text highlighter-rouge"><div class="highlight"><pre class="highlight"><code>scene → user → pain → need → feature → product → business
</code></pre></div></div>

<p>报告、MRD、PRD、BRD、网页和特定角色的可交付成果是预测<code class="language-plaintext highlighter-rouge">product-reasoning.json</code>，不是独立的结论。 链通过指向需求判断<code class="language-plaintext highlighter-rouge">demand_judgment_id</code>；证据也必须共享链条的<code class="language-plaintext highlighter-rouge">context_key</code>。 这可以防止为一个市场、帐户或研究背景收集的记录成为另一个市场、帐户或研究背景的便捷支持。</p>

<p>分离不仅仅是文件卫生。 它允许Askovo明确拒绝几种不同的故障模式：</p>

<ul>
  <li>节点有证据ID，但证据属于另一个上下文；</li>
  <li>证据记录是真实的，但其类型不能支持所提出的主张；</li>
  <li>业务节点被标记<code class="language-plaintext highlighter-rouge">decided</code>，但交付、观察到的结果和因果状态尚未确定；</li>
  <li>尽管完整的证据门失败，但报告包含一个结论。</li>
</ul>

<p>导入的记录不能简单地宣布自己是E5交易证据。 E4+交易或购买索赔需要交易对手、时间戳、金额、来源参考和证据参考。 缺失的结构在E2上保持记录，并保留推导规则。 标有“交易”的一行文本不会因此成为收据。</p>

<h2 id="product-observations-carry-their-own-scope">产品观察有自己的范围</h2>

<p>Askovo也接受产品行为观察，但他们的模式使过度概括变得尴尬：</p>

<div class="language-json highlighter-rouge"><div class="highlight"><pre class="highlight"><code><span class="p">{</span><span class="w">
  </span><span class="nl">"observation_id"</span><span class="p">:</span><span class="w"> </span><span class="s2">"obs-mobile-001"</span><span class="p">,</span><span class="w">
  </span><span class="nl">"product_version"</span><span class="p">:</span><span class="w"> </span><span class="s2">"2.22.1"</span><span class="p">,</span><span class="w">
  </span><span class="nl">"account_permission"</span><span class="p">:</span><span class="w"> </span><span class="s2">"owner"</span><span class="p">,</span><span class="w">
  </span><span class="nl">"platform"</span><span class="p">:</span><span class="w"> </span><span class="s2">"macos"</span><span class="p">,</span><span class="w">
  </span><span class="nl">"region"</span><span class="p">:</span><span class="w"> </span><span class="s2">"cn"</span><span class="p">,</span><span class="w">
  </span><span class="nl">"tested_at"</span><span class="p">:</span><span class="w"> </span><span class="s2">"2026-11-23T10:00:00Z"</span><span class="p">,</span><span class="w">
  </span><span class="nl">"method"</span><span class="p">:</span><span class="w"> </span><span class="s2">"scripted"</span><span class="p">,</span><span class="w">
  </span><span class="nl">"claims"</span><span class="p">:</span><span class="w"> </span><span class="p">[{</span><span class="w">
    </span><span class="nl">"claim_id"</span><span class="p">:</span><span class="w"> </span><span class="s2">"claim-001"</span><span class="p">,</span><span class="w">
    </span><span class="nl">"observed_facts"</span><span class="p">:</span><span class="w"> </span><span class="p">[</span><span class="s2">"The CLI returned STALE_SOURCE after a source rewrite"</span><span class="p">],</span><span class="w">
    </span><span class="nl">"inferred_rule"</span><span class="p">:</span><span class="w"> </span><span class="s2">"An active request refuses a mixed study revision"</span><span class="p">,</span><span class="w">
    </span><span class="nl">"uncovered_conditions"</span><span class="p">:</span><span class="w"> </span><span class="p">[</span><span class="s2">"Windows file-locking behavior was not exercised"</span><span class="p">],</span><span class="w">
    </span><span class="nl">"generalization"</span><span class="p">:</span><span class="w"> </span><span class="s2">"single_case"</span><span class="p">,</span><span class="w">
    </span><span class="nl">"repeat_count"</span><span class="p">:</span><span class="w"> </span><span class="mi">1</span><span class="p">,</span><span class="w">
    </span><span class="nl">"evidence_level"</span><span class="p">:</span><span class="w"> </span><span class="s2">"E2"</span><span class="p">,</span><span class="w">
    </span><span class="nl">"basis"</span><span class="p">:</span><span class="w"> </span><span class="s2">"product_behavior_observation"</span><span class="w">
  </span><span class="p">}]</span><span class="w">
</span><span class="p">}</span><span class="w">
</span></code></pre></div></div>

<p>三个泛化值具有可执行的定义：</p>

<table>
  <thead>
    <tr>
      <th>公告</th>
      <th>记录中最低限度的证据</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td><code class="language-plaintext highlighter-rouge">single_case</code></td>
      <td>正好一次运行；<code class="language-plaintext highlighter-rouge">not_generalizable=true</code>出口</td>
    </tr>
    <tr>
      <td><code class="language-plaintext highlighter-rouge">repeated</code></td>
      <td>至少两次跑步</td>
    </tr>
    <tr>
      <td><code class="language-plaintext highlighter-rouge">multi_context</code></td>
      <td>至少两次跑步和两次不同的<code class="language-plaintext highlighter-rouge">(product_version, account_permission, platform, region)</code>元组</td>
    </tr>
  </tbody>
</table>

<p>没有<code class="language-plaintext highlighter-rouge">universal</code>价值。 观测到上限为E2，并导出到<code class="language-plaintext highlighter-rouge">01-sources/observations.jsonl</code>不将他们提升到主要证据库中。 仍然需要命名的人类语义审查。</p>

<p>这是数据收集和索赔生成之间的有用区别。 模式保留<code class="language-plaintext highlighter-rouge">observed_facts</code>, <code class="language-plaintext highlighter-rouge">inferred_rule</code>，还有<code class="language-plaintext highlighter-rouge">uncovered_conditions</code>在不同的领域。 收集器不能在不留下可见的验证错误的情况下将“我看过一次”变成“产品总是工作”。</p>

<h2 id="request-snapshots-solve-a-different-problem-from-an-lru-cache">请求快照解决了与LRU缓存不同的问题</h2>

<p>2.22的实施以两个类别为中心：</p>

<ul>
  <li><code class="language-plaintext highlighter-rouge">StudyRepository</code>拥有路径包含、字节读取、原子写入、事务和源版本清单。</li>
  <li><code class="language-plaintext highlighter-rouge">StudyContext</code>拥有一个请求的不可变字节快照和解析数据缓存。</li>
</ul>

<p>清单用SHA-256对每个包含的研究文件进行哈希，不包括生成的<code class="language-plaintext highlighter-rouge">05-audit/</code>和<code class="language-plaintext highlighter-rouge">06-report/</code>产出。 请求激活等同于：</p>

<div class="language-python highlighter-rouge"><div class="highlight"><pre class="highlight"><code><span class="n">manifest</span> <span class="o">=</span> <span class="n">repository</span><span class="p">.</span><span class="n">version_manifest</span><span class="p">()</span>
<span class="n">assert_write_journal_clean</span><span class="p">()</span>

<span class="k">yield</span> <span class="n">context</span>  <span class="c1"># on successful completion of the request body:
</span><span class="n">assert_write_journal_clean</span><span class="p">()</span>
<span class="k">assert</span> <span class="n">repository</span><span class="p">.</span><span class="n">version_manifest</span><span class="p">()</span> <span class="o">==</span> <span class="n">manifest</span>
</code></pre></div></div>

<p>如果另一个进程在请求期间提交多文件更改，则交付失败<code class="language-plaintext highlighter-rouge">STALE_SOURCE</code>。 Askovo不会将新证据合并到一半的输出中，也不会默默地将旧报告返回为当前报告。 下一个法律行动是针对新承诺的修订重新尝试审计和交付。</p>

<p>在请求中，<code class="language-plaintext highlighter-rouge">StudyContext.read_bytes()</code>在请求范围字典中memoize原始字节。 解析的JSON和JSONL读取返回深度副本，因此突变嵌套声明的调用者无法更改另一个投影读取的内容。 JSONL缓存密钥包括解析路径、原始字节的128位BLAKE2b摘要、解析器身份和严格性。</p>

<p>较旧的32个条目LRU仍然具有解析数据的兼容性角色。 这不是请求隔离边界。 在2.22.1中，原始请求快照不再从属于该容量限制。 这种区别很重要：LRU是内存管理优化，而快照是正确性合同。 用另一个替换一个会产生一种错误，这种错误看起来像是偶尔的研究不一致，而不是存储错误。</p>

<p>存储库还拒绝在研究之外解析的路径。 这是与修订稳定性分开的边界：源引用不应将报告生成器变成任意的本地文件阅读器。</p>

<h2 id="observation-export-is-idempotent-by-content-not-by-metadata">观察导出因内容而异，而不是因元数据而异</h2>

<p>观察导出使用身份：</p>

<div class="language-python highlighter-rouge"><div class="highlight"><pre class="highlight"><code><span class="p">(</span><span class="n">observation_id</span><span class="p">,</span> <span class="n">claim_id</span><span class="p">,</span> <span class="n">source_hash</span><span class="p">)</span>
</code></pre></div></div>

<p><code class="language-plaintext highlighter-rouge">source_hash</code>是源观测文件的SHA-256。 出口程序是：</p>

<div class="language-python highlighter-rouge"><div class="highlight"><pre class="highlight"><code><span class="k">with</span> <span class="n">repository</span><span class="p">.</span><span class="n">transaction</span><span class="p">(</span><span class="s">"observation export"</span><span class="p">)</span> <span class="k">as</span> <span class="n">txn</span><span class="p">:</span>
    <span class="n">existing</span> <span class="o">=</span> <span class="n">read_existing_identities</span><span class="p">(</span><span class="n">target</span><span class="p">)</span>
    <span class="n">new_lines</span> <span class="o">=</span> <span class="p">[</span><span class="n">line</span> <span class="k">for</span> <span class="n">line</span> <span class="ow">in</span> <span class="n">projected</span> <span class="k">if</span> <span class="n">identity</span><span class="p">(</span><span class="n">line</span><span class="p">)</span> <span class="ow">not</span> <span class="ow">in</span> <span class="n">existing</span><span class="p">]</span>
    <span class="k">if</span> <span class="n">new_lines</span><span class="p">:</span>
        <span class="n">txn</span><span class="p">.</span><span class="n">add</span><span class="p">(</span><span class="n">target</span><span class="p">,</span> <span class="n">append_jsonl</span><span class="p">(</span><span class="n">new_lines</span><span class="p">),</span> <span class="n">mode</span><span class="o">=</span><span class="s">"append"</span><span class="p">)</span>
        <span class="n">txn</span><span class="p">.</span><span class="n">commit</span><span class="p">()</span>
</code></pre></div></div>

<p>重复导出同一字节返回<code class="language-plaintext highlighter-rouge">added=0</code>。 在保留其ID和元数据的同时编辑观察值会更改哈希值，因此导出成为新的修订版，而不是作为副本消失。 身份检查和附加写入具有相同的研究交易锁，关闭了两个过程窗口，其中两个出口商都可以确定索赔不存在。</p>

<p>这是一个故意狭义的冪等合同。 它没有说两个具有不同哈希值的观察文件在语义上是不同的声明。 它说，系统不会仅仅因为元数据看起来很熟悉就删除源版本。</p>

<p>测试涵盖重复导出、并发导出、更改源哈希、损坏历史记录、中断的附加恢复、无效存储文档以及在事务失败后保留以前的字节。 在准备这篇文章时，我运行了研究上下文和观察套件：29项测试通过。</p>

<h2 id="a-contradiction-triggers-a-state-transition-not-a-new-essay">矛盾引发了国家过渡，而不是新文章</h2>

<p>决策记录是规范链的仅附加快照。 每条记录都有一个版本、父版本、决策者、链指纹、链快照、原始假设、当前候选行动和支持状态。 普通观察不会修改实时建议。</p>

<p>只有在更苛刻的合同下才允许进行对抗性修订：</p>

<ol>
  <li>首字母<code class="language-plaintext highlighter-rouge">DecisionRecord</code>必须存在。</li>
  <li>矛盾ID必须注册在<code class="language-plaintext highlighter-rouge">02-data/evidence.jsonl</code>.</li>
  <li>证据必须共享链条的<code class="language-plaintext highlighter-rouge">context_key</code>.</li>
  <li><code class="language-plaintext highlighter-rouge">evidence_level</code>, <code class="language-plaintext highlighter-rouge">evidence_basis</code>，还有<code class="language-plaintext highlighter-rouge">source_ref</code>必须在场。</li>
  <li>预先录制的<code class="language-plaintext highlighter-rouge">contradicts</code>或反证据关系必须存在于证据立场、连锁计数器列表、链接需求判断或循环映射中。</li>
</ol>

<p>通过这些检查不会调用LLM来写反驳。 该代码应用了一个确定性过渡：</p>

<div class="language-python highlighter-rouge"><div class="highlight"><pre class="highlight"><code><span class="n">confidence_scale</span> <span class="o">=</span> <span class="p">(</span><span class="s">"very-low"</span><span class="p">,</span> <span class="s">"low"</span><span class="p">,</span> <span class="s">"medium"</span><span class="p">,</span> <span class="s">"high"</span><span class="p">)</span>
<span class="n">new_confidence</span> <span class="o">=</span> <span class="n">confidence_scale</span><span class="p">[</span><span class="nb">max</span><span class="p">(</span><span class="mi">0</span><span class="p">,</span> <span class="n">old_index</span> <span class="o">-</span> <span class="mi">1</span><span class="p">)]</span>

<span class="n">chain</span><span class="p">.</span><span class="n">status</span> <span class="o">=</span> <span class="s">"needs-validation"</span>
<span class="n">chain</span><span class="p">.</span><span class="n">nodes</span><span class="p">.</span><span class="n">product</span><span class="p">.</span><span class="n">status</span> <span class="o">=</span> <span class="s">"needs-validation"</span>
<span class="n">chain</span><span class="p">.</span><span class="n">nodes</span><span class="p">.</span><span class="n">business</span><span class="p">.</span><span class="n">status</span> <span class="o">=</span> <span class="s">"needs-validation"</span>
<span class="n">chain</span><span class="p">.</span><span class="n">nodes</span><span class="p">.</span><span class="n">business</span><span class="p">.</span><span class="n">gate</span><span class="p">.</span><span class="n">decision</span> <span class="o">=</span> <span class="s">"hold"</span>  <span class="c1"># unless a human supplies a replacement
</span></code></pre></div></div>

<p>公共合成回归提供了一个具体的前/后：</p>

<div class="language-text highlighter-rouge"><div class="highlight"><pre class="highlight"><code>DecisionRecord version:       1 → 2
recommendation_origin:        deterministic_safe_hold
recommendation_code:          hold
confidence:                   low → very-low
chain/product/business:       needs-validation
candidate_evidence_promoted:  false
demand_judgment_changed:      false
causal_status_changed:        false
full audit:                   PASS
</code></pre></div></div>

<p>两个细节特别重要。 需求判断文件保持字节相同，支持状态保持不变。 系统重新打开决定；它不会重写证据库来证明新状态的合理性。 一个单独的测试提供了没有记录的矛盾映射的证据ID。 命令退出2，并保持规范推理字节未触及。</p>

<p>人类可以提供明确的替换建议。 那产生<code class="language-plaintext highlighter-rouge">recommendation_origin=decision_maker_override</code>，不是CLI的假装语义推理。</p>

<p>决策命令是：</p>

<div class="language-bash highlighter-rouge"><div class="highlight"><pre class="highlight"><code>askovo decision record STUDY <span class="nt">--chain</span> PR01 <span class="nt">--by</span> <span class="s2">"Product owner"</span>
askovo decision record STUDY <span class="nt">--chain</span> PR01 <span class="nt">--by</span> <span class="s2">"Product owner"</span> <span class="se">\</span>
  <span class="nt">--contradiction</span> EVIDENCE_ID
askovo decision replay STUDY <span class="nt">--chain</span> PR01 <span class="nt">--json</span>
</code></pre></div></div>

<p>这个<a href="https://roy-tong.github.io/Askovo/en/examples/decision-replay.html">公共决策重播页面</a>链接到实际回归。 我为了这篇文章再次运行了它；它通过了。</p>

<h2 id="proof-export-deliberately-produces-an-incomplete-proof">证明出口故意产生不完整的证明</h2>

<p>Askovo可以将研究投射到OVO的共享证明包格式中：</p>

<div class="language-bash highlighter-rouge"><div class="highlight"><pre class="highlight"><code>askovo proof <span class="nb">export </span>STUDY <span class="nt">--out</span> NEW_DIR <span class="nt">--by</span> NAME
</code></pre></div></div>

<p>导出器首先重建或阅读决策简报，删除摘录，并在安全投影中用证据ID替换直接来源位置，对规范输入进行散发，然后写入暂存目录。 输出必须在源研究之外，并且现有的输出永远不会被覆盖。</p>

<p>它的检查是故意不对称的：</p>

<table>
  <thead>
    <tr>
      <th>支票</th>
      <th>度</th>
      <th>正常状态</th>
      <th>原因</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td><code class="language-plaintext highlighter-rouge">artifact-readable</code></td>
      <td>P1</td>
      <td><code class="language-plaintext highlighter-rouge">PASS</code>，或者<code class="language-plaintext highlighter-rouge">EXPIRED</code>如果简报陈旧了</td>
      <td>该简报是已确定的输入的可读投影</td>
    </tr>
    <tr>
      <td><code class="language-plaintext highlighter-rouge">independent-semantic-review</code></td>
      <td>P3</td>
      <td><code class="language-plaintext highlighter-rouge">UNCHECKED</code></td>
      <td>出口商不能批准研究语义</td>
    </tr>
    <tr>
      <td><code class="language-plaintext highlighter-rouge">external-decision-adoption</code></td>
      <td>P4</td>
      <td><code class="language-plaintext highlighter-rouge">UNCHECKED</code></td>
      <td>没有所有者处置自动捆绑</td>
    </tr>
    <tr>
      <td><code class="language-plaintext highlighter-rouge">replay-readiness</code></td>
      <td>P1</td>
      <td><code class="language-plaintext highlighter-rouge">INDETERMINATE</code></td>
      <td>私人规范输入和收集历史记录不会被复制</td>
    </tr>
  </tbody>
</table>

<p>因此，正常的出口有<code class="language-plaintext highlighter-rouge">proof_status=BLOCKED</code>。 那不是出口商的失败。 这是将“我们生成了一个有效的简报”与“独立审查员接受了推理”和“所有者实际使用它”分开的预期后果。</p>

<p>Askovo确实有一个单独的收养命令，但它记录了指定所有者的声明和提供的收据文本。 它不会验证所有者的身份或推断商业成功。 声明是有用的证据；它不是神奇的独立观察。</p>

<p>隐私和重播在这里向相反的方向拉动。 复制每个规范输入将使第三方重播更容易，并泄露研究。 出口商选择更安全的默认值：保持证明在结构上可审查，并在提供授权输入之前标记完全重播不可用。</p>

<h2 id="what-the-second-use-should-measure">第二次使用应该衡量什么</h2>

<p>一项Askovo内部研究分析了24个月内来自八个社区的109,429条重复评论。 由此产生的建议将高尔夫设备序列从专用相机硬件更改为首先验证软件和导出工作流程。 该样本是方便样本，因此它不能支持市场流行率估计。 有益的结果是改变了产品努力的拟议分配。</p>

<p>等效的软件测试不是是否可以生成另一份报告。 这是第二次决定审查是否保留了原始决定，在不破坏旧基础的情况下导入新证据，并减少不必要的返工，同时暴露其人工记录。</p>

<p>因此，有用的二次使用记录包括：</p>

<ul>
  <li>在新证据之前记录的原始倾斜和替代方案；</li>
  <li>新证据哈希及其与先前索赔的关系；</li>
  <li>所有者的实际处置：维持、更改、推迟或收集证据；</li>
  <li>审查和更正会议记录；</li>
  <li>仍未检查的支票；</li>
  <li>独立审查，如果有的话。</li>
</ul>

<p>重复两次相同的夹具是一种确定性测试。 第二种用途是新的决定修订或具有自身背景的独立决定。</p>

<h2 id="the-tradeoffs-are-visible-in-the-implementation">在实施中可以看到权衡</h2>

<p>Askovo的方法是有代价的。 整个研究清单要求在请求边界上读取源文件；该项目并不声称这是非常大型研究的最快设计。 JSON和JSONL使研究可检查和版本控制友好，但它们需要明确的交易纪律，否则数据库会提供帮助。 快照隔离有利于连贯的报告，而不是立即纳入新到的证据。</p>

<p>确定性安全持有同样是一种产品选择。 它无法决定矛盾在语义上是否有效、具有代表性或重要。 它只能保证当前的建议机制不能忽视记录的、相同背景的、映射的矛盾。 人类评论仍然对意义负责。</p>

<p>这些约束比总是产生答案的系统更可取。 研究工具应该能够返回<code class="language-plaintext highlighter-rouge">STALE_SOURCE</code>，拒绝未经证实的证据等级，保留未知，或重新打开决定。 否则，它的一致性只是排版。</p>

<h3 id="source-and-verification-links">来源和验证链接</h3>

<ul>
  <li><a href="https://github.com/roy-tong/Askovo/blob/main/skills/askovo/scripts/study_context.py"><code class="language-plaintext highlighter-rouge">study_context.py</code>：存储库、快照、清单和请求激活</a></li>
  <li><a href="https://github.com/roy-tong/Askovo/blob/main/skills/askovo/scripts/observation.py"><code class="language-plaintext highlighter-rouge">observation.py</code>：观察模式和交易导出</a></li>
  <li><a href="https://github.com/roy-tong/Askovo/blob/main/skills/askovo/scripts/decision_review.py"><code class="language-plaintext highlighter-rouge">decision_review.py</code>：矛盾验证和确定性安全持有</a></li>
  <li><a href="https://github.com/roy-tong/Askovo/blob/main/skills/askovo/scripts/proof_export.py"><code class="language-plaintext highlighter-rouge">proof_export.py</code>：P1/P3/P4检查和重播边界</a></li>
  <li><a href="https://roy-tong.github.io/Askovo/en/examples/decision-replay.html">决策重播示例和可运行回归</a></li>
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
