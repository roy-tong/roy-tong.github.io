---
title: "After the App, do you need a \"world canvas\" for space computing?"
date: "2026-10-02T18:20:00+08:00"
description: "同一台机器的设计、维修和操作记录，常被不同应用分别保存。世界画布要让对象身份、状态与权限跨工具延续。"
permalink: "/en/notes/world-canvas/"
content_id: world-canvas
knowledge_topic: ai-devices
knowledge_units: [spatial-computing, agent-context]
translation_of: /notes/world-canvas/
lang: en
generated_translation: true
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




      <link rel="alternate" hreflang="en" href="https://roy-tong.github.io/en/notes/world-canvas/">
      <link rel="alternate" hreflang="zh-CN" href="https://roy-tong.github.io/notes/world-canvas/">
      <link rel="alternate" hreflang="x-default" href="https://roy-tong.github.io/notes/world-canvas/">
    <link type="application/atom+xml" rel="alternate" href="https://roy-tong.github.io/feed.xml" title="Roy.Tong"/>
    <!-- Begin Jekyll SEO tag v2.8.0 -->
<title>After the App, do you need a &quot;world canvas&quot; for space computing? |Roy.Tong</title>
<meta name="generator" content="Jekyll v3.9.5"/>
<meta property="og:title" content="App 之后，空间计算需要一张“世界画布”吗？"/>
<meta name="author" content="Roy.Tong"/>
<meta property="og:locale" content="en_US">
<meta name="description" content="同一台机器的设计、维修和操作记录，常被不同应用分别保存。世界画布要让对象身份、状态与权限跨工具延续。"/>
<meta property="og:description" content="同一台机器的设计、维修和操作记录，常被不同应用分别保存。世界画布要让对象身份、状态与权限跨工具延续。"/>
<link rel="canonical" href="https://roy-tong.github.io/en/notes/world-canvas/">
<meta property="og:url" content="https://roy-tong.github.io/en/notes/world-canvas/">
<meta property="og:site_name" content="Roy.Tong"/>
<meta property="og:image" content="https://roy-tong.github.io/assets/images/social-preview.png"/>
<meta property="og:type" content="article"/>
<meta property="article:published_time" content="2026-10-02T18:20:00+08:00"/>
<meta name="twitter:card" content="summary_large_image"/>
<meta property="twitter:image" content="https://roy-tong.github.io/assets/images/social-preview.png"/>
<meta property="twitter:title" content="App 之后，空间计算需要一张“世界画布”吗？"/>
<script type="application/ld+json">
{"@context":"https://schema.org","@type":"BlogPosting","author":{"@type":"Person","name":"Roy.Tong"},"dateModified":"2026-10-02T18:20:00+08:00","datePublished":"2026-10-02T18:20:00+08:00","description":"同一台机器的设计、维修和操作记录，常被不同应用分别保存。世界画布要让对象身份、状态与权限跨工具延续。","headline":"App 之后，空间计算需要一张“世界画布”吗？","image":"https://roy-tong.github.io/assets/images/social-preview.png","mainEntityOfPage":{"@type":"WebPage","@id":"https://roy-tong.github.io/notes/world-canvas/"},"publisher":{"@type":"Organization","logo":{"@type":"ImageObject","url":"https://roy-tong.github.io/assets/images/social-preview.png"},"name":"Roy.Tong"},"url":"https://roy-tong.github.io/notes/world-canvas/"}</script>
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
            <a class="language-toggle" href="/notes/world-canvas/" hreflang="zh-CN" lang="zh-CN" data-language-switch data-target-language="zh-CN" aria-label="View in English" title="View in English">EN</a>
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

    <main id="main"><p class="translation-note" aria-label="Translation note">Machine-assisted translation. <a href="/notes/world-canvas/">Read the Chinese original</a>.</p>
      




<article class="post shell reading-shell">
  <header class="post-header">
    <a class="eyebrow back-link" href="/en/archive/">← Back to the article</a>
    <h1>After the App, do you need a &quot;world canvas&quot; for space computing?</h1>
    <p class="post-subtitle">Information hangs in the world, not in the application. The public version has hidden the specific platform, company and product name.</p>
    <div class="post-meta">
      <time datetime="2026-10-02T18:20:00+08:00">2026-10-02</time>
      <span>5 minutes to read</span>
      
      <a class="post-translation" href="/notes/world-canvas/" hreflang="zh-CN">阅读中文版 →</a>
      
        <span class="post-tags">
          <a href="/en/tags/#%E7%A9%BA%E9%97%B4%E8%AE%A1%E7%AE%97">#Space calculation</a><a href="/en/tags/#ai%20%E7%A1%AC%E4%BB%B6">#AI hardware</a><a href="/en/tags/#%E4%BA%A7%E5%93%81%E8%AE%BE%E6%83%B3">#Product idea</a>
        </span>
      
    </div>
  </header>

  <div class="prose">
    <p>Talking about space calculation, there is a premise that is rarely asked: where is the information hanging?</p>

<p>Most of today&#x27;s software is still organized by applications. Open the image software for retouching, open the map for navigation, and the space device also follows this structure: open an application and put the window into the room.</p>

<p>The information hangs in the application, which is the answer left by the desktop era. The problem is that only using application windows to organize information may not be suitable for spatial tasks that require cross-tool continuity.</p>

<h2 id="真实空间不是一组窗口">Real space is not a group of windows.</h2>

<p>A chair has a position, orientation and belonging to; a machine has a structure, state, history and authority. The same object will be used by design tools, repair tools and family agents at the same time.</p>

<p>Applications don&#x27;t know each other. The retouching software does not know the person of the chair, and the maintenance tool does not know what the design tool has changed. In the desktop world, this is bearable, and files are copied; in the space world, there is only one object, but there are many applications. &quot;Who is the truth&quot; becomes a question to be answered every day.</p>

<h2 id="从窗口到画布">From the window to the canvas</h2>

<p>If spatial computing continues to develop, a &quot;world canvas&quot; can be added outside the application: real objects and digital objects together form an understandable, operable and authorized whole.</p>

<p>What the user expresses is no longer a menu command, but &quot;what do you want this part of the world to become&quot;: tell me why the water is leaking here; move the table to a position that does not block the door; freeze the current layout and try another rule, and restore it if the effect is not good.</p>

<p>For users, the canvas changes the interaction from &quot;action&quot; to &quot;status&quot;. Today, what users do in the application is verbs: new, drag, save; what the user expresses on the canvas is the goal, and the system is responsible for translating the goal into action.</p>

<p>For developers, the competition has changed from &quot;occupying an entrance application&quot; to &quot;providing capabilities on a shared canvas&quot;. Repair tools do not need their own rooms, they only need to hang their own services and records on the machine object. The moat at the entrance becomes thinner, but the identity and authority of the object become thicker.</p>

<h2 id="四件基础设施">Four pieces of infrastructure</h2>

<p>To make it valid, the platform must at least provide:</p>

<ol>
  <li><strong>Stabilize the identity of the object</strong>: The same chair has been replaced three times, and after a month, it is still &quot;that one&quot;;</li>
  <li><strong>Spatial relationship and state</strong>: Position, orientation, layout rules;</li>
  <li><strong>Cross-application access</strong>: Design, maintenance and family Agent share the same object;</li>
  <li><strong>The authority of people and Agent</strong>: Who can see, who can change, and who can only make suggestions.</li>
</ol>

<p>This is much more difficult than putting a few more windows in the room, and it is closer to the real difference between spatial computing and desktop computing.</p>

<h2 id="画布改写了后悔">The canvas rewrote &quot;regret&quot;</h2>

<p>The desktop era depends on the in-app cancellation and version. In the era of canvas, the object has its own history, which can be frozen and arranged, try another rule, and the effect is not easy to restore.</p>

<p>However, the digital layout and analog state can be returned, and the movement, wear or damage of real objects cannot be restored by the undo button. When real equipment is involved, there must be a separate safe stop, takeover and recovery actions; the digital version record is only one of them.</p>

<h2 id="操作画布的系统分布在全身">The system of operating the canvas is distributed throughout the body.</h2>

<p>Information hangs in the world, and the system that operates it is spread on the body. Glasses are responsible for first-person perspective and display, headphones are responsible for private audio, rings or wristbands are responsible for silent confirmation, and mobile phones are responsible for high-density management.</p>

<p>First-time settings, complex editing, permissions and abnormal recovery are still the most suitable for mobile phones. At this time, the analysis of competitive products can not only compare with the host, but also with the whole interaction chain composed of pairing, connection, charging, state synchronization and abnormal recovery.</p>

<h2 id="从窄场景长出来">Grow out of the narrow scene</h2>

<p>Today, most space products are still far from this canvas: applications are modeled separately and do not communicate with each other, and the object identity stops within a single application. To judge whether a platform has canvas ambition, it depends on whether the object can be recognized after leaving a single application.</p>

<p>The canvas will not be laid overnight. It is more likely to grow out of a narrow scene: first a machine with its own maintenance history, then a room with layout rules, and finally the whole world.</p>

<p>Until then, &quot;putting the window into the room&quot; is still a safe default, just don&#x27;t take it as the end.</p>

<hr/>

<p><strong>Public explanation</strong>: This article removes specific platform, product, character and source links, and only retains the product concept of &quot;object-status-permission&quot;. It is not a fact of the industry that has been completed.</p>

  </div>

  

<aside class="kb-related" aria-label="Relevant research materials">
  <h2>Relevant research materials</h2>
  <p>Reports, data and notes are kept in the database and can continue to be consulted. The following is related to the same topic; the evidence directly used in this article shall be subject to the text citation.</p>
  
  <ul>
    
      
      <li><a href="/en/knowledge/collections/product-research/">Product Research and Organization Methods · Research Archives</a></li>
    
  </ul>
  <ul>
    
      
        <li><a href="/en/knowledge/spatial-computing/">Spatial interaction: the object pointed to needs to be operated continuously.</a></li>
      
    
      
        <li><a href="/en/knowledge/agent-context/">Agent Runtime: Context, Status and Permissions</a></li>
      
    
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
