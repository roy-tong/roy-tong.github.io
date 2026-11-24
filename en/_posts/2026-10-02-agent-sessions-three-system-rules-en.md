---
title: "After running hundreds of Agent sessions, I left three system rules"
date: "2026-10-02T11:00:00+08:00"
lang: en
permalink: "/en/notes/agent-sessions-three-system-rules/"
generated_translation: true
content_id: agent-sessions-three-system-rules
knowledge_topic: agent-systems
knowledge_units: [research-workflows, agent-context]
translation_of: /notes/agent-sessions-three-system-rules/
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




      <link rel="alternate" hreflang="en" href="https://roy-tong.github.io/en/notes/agent-sessions-three-system-rules/">
      <link rel="alternate" hreflang="zh-CN" href="https://roy-tong.github.io/notes/agent-sessions-three-system-rules/">
      <link rel="alternate" hreflang="x-default" href="https://roy-tong.github.io/notes/agent-sessions-three-system-rules/">
    <link type="application/atom+xml" rel="alternate" href="https://roy-tong.github.io/feed.xml" title="Roy.Tong"/>
    <!-- Begin Jekyll SEO tag v2.8.0 -->
<title>After running hundreds of Agent sessions, I left three system rules | Roy.Tong</title>
<meta name="generator" content="Jekyll v3.9.5"/>
<meta property="og:title" content="After running hundreds of Agent sessions, I left three system rules">
<meta name="author" content="Roy.Tong"/>
<meta property="og:locale" content="en_US">
<meta name="description" content="One day in early September, I asked the self-built DeepSeek harness (hereinafter referred to as DSH) to run a round of competitive information scanning. Dozens of sub-agents were grabbing data, and one of them suddenly found that the built-in search tool began to return to HTTP 402 - the quota was used up. It didn&#x27;t stop...">
<meta property="og:description" content="One day in early September, I asked the self-built DeepSeek harness (hereinafter referred to as DSH) to run a round of competitive information scanning. Dozens of sub-agents were grabbing data, and one of them suddenly found that the built-in search tool began to return to HTTP 402 - the quota was used up. It didn&#x27;t stop...">
<link rel="canonical" href="https://roy-tong.github.io/en/notes/agent-sessions-three-system-rules/">
<meta property="og:url" content="https://roy-tong.github.io/en/notes/agent-sessions-three-system-rules/">
<meta property="og:site_name" content="Roy.Tong"/>
<meta property="og:image" content="https://roy-tong.github.io/assets/images/social-preview.png"/>
<meta property="og:type" content="article"/>
<meta property="article:published_time" content="2026-10-02T11:00:00+08:00"/>
<meta name="twitter:card" content="summary_large_image"/>
<meta property="twitter:image" content="https://roy-tong.github.io/assets/images/social-preview.png"/>
<meta property="twitter:title" content="After running hundreds of Agent sessions, I left three system rules">
<script type="application/ld+json">
{"@context":"https://schema.org","@type":"BlogPosting","author":{"@type":"Person","name":"Roy.Tong"},"dateModified":"2026-10-02T11:00:00+08:00","datePublished":"2026-10-02T11:00:00+08:00","description":"九月上旬某天，我让自建的 DeepSeek harness（下称 DSH）跑一轮竞品信息扫描，几十个子代理正在各自抓资料，其中一个突然发现内置搜索工具开始返回 HTTP 402——配额用完了。它没有停…","headline":"跑了几百个 Agent 会话后，我留下了三条系统规则","image":"https://roy-tong.github.io/assets/images/social-preview.png","mainEntityOfPage":{"@type":"WebPage","@id":"https://roy-tong.github.io/notes/agent-sessions-three-system-rules/"},"publisher":{"@type":"Organization","logo":{"@type":"ImageObject","url":"https://roy-tong.github.io/assets/images/social-preview.png"},"name":"Roy.Tong"},"url":"https://roy-tong.github.io/notes/agent-sessions-three-system-rules/"}</script>
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
            <a class="language-toggle" href="/notes/agent-sessions-three-system-rules/" hreflang="zh-CN" lang="zh-CN" data-language-switch data-target-language="zh-CN" aria-label="切换至中文" title="切换至中文">中文</a>
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

    <main id="main"><p class="translation-note" aria-label="Translation note">Machine-assisted translation. <a href="/notes/agent-sessions-three-system-rules/">Read the Chinese original</a>.</p>
      




<article class="post shell reading-shell">
  <header class="post-header">
    <a class="eyebrow back-link" href="/en/archive/">← Back to the article</a>
    <h1>After running hundreds of Agent sessions, I left three system rules.</h1>
    <p class="post-subtitle">It can be parallel, but the task must be narrow; it can fail, but it must be downgraded; judgment and action need determinism access control.</p>
    <div class="post-meta">
      <time datetime="2026-10-02T11:00:00+08:00">2026-10-02</time>
      <span>5 minutes to read</span>
      
      <a class="post-translation" href="/notes/agent-sessions-three-system-rules/" hreflang="zh-CN">阅读中文版 →</a>
      
        <span class="post-tags">
          <a href="/en/tags/#agent">#Agent</a><a href="/en/tags/#%E8%87%AA%E5%8A%A8%E5%8C%96">#Automation</a><a href="/en/tags/#%E5%B7%A5%E7%A8%8B%E5%AE%9E%E8%B7%B5">#Engineering practice</a>
        </span>
      
    </div>
  </header>

  <div class="prose">
    <p>One day in early September, I asked the self-built DeepSeek harness (hereinafter referred to as DSH) to run a round of competitive information scanning. Dozens of sub-agents were grabbing data, and one of them suddenly found that the built-in search tool began to return to HTTP 402 - the quota was used up. It didn&#x27;t stop and wait for me. It flipped through the old scripts in the workspace, found two free search paths, and then completed its part of the task.</p>

<p>Let&#x27;s explain the background first. DSH is a set of research pipelines in the resident background. The model is deepseek-v4.1-flash. The main usage is to fan out: a main agent disassembles the research task and sends sub-agents with role settings to work in parallel; each session is recorded in an event-by-event log. Who did what, which tool was adjusted, and which step failed can be reconciled later. From mid-August to now, there are 336 session catalogs. In these hundreds of sessions, quota exhaustion, review hallucinations, and 449 empty mail accidents have all been hit once, leaving three rules in the end. They do not bind DeepSeek, and any self-built agent system is still established.</p>

<h2 id="规则一能并行但任务必须窄">Rule 1: It can be parallel, but the task must be narrow.</h2>

<p>I grouped the number of sub-agents by day from the conversation record: 108 on September 8, 71 on September 24, and 53 on September 19. The division of labor can be seen in the naming - demand-validation researcher, primary-source documentation researcher. A round of competitive product scanning was removed, and a split body only took care of a company&#x27;s public records on a source. After checking, he handed in the structured field and left. The narrow task also brings a by-product: failure becomes cheaper. A split body is checked and smashed, and a rerun is an API call. There is no need for people to clean up on the spot, and it does not pollute the output of other split bodies.</p>

<p>When is it worth opening to three digits? My judgment criteria are that three can be established at the same time: the task can be neatly cut into a narrow problem that does not depend on each other (one company, one source and one role); it doesn&#x27;t matter if a single sub-task fails, and the cost of starting is close to zero; the result can be mechanically combined, and the main agent only summarizes. The three standards correspond to three costs: cutting cost, retry cost, and consolidation cost. Which one can&#x27;t be paid, the fan out will be stuck at any level. If any of the three articles is not valid, fanning out is amplifying the chaos: when the task boundary is not cut cleanly, multiple split bodies will overlap the same object, and the conflict fields in the merging stage will need to be manually adjudicated. At this time, it is faster to open a few fewer. The economic account fanned out is not in the number of split bodies, and the task of each split body is so narrow that there is no need to judge.</p>

<p>The practice that can be taken away: cut the task first, and then talk about parallel. Cut each sub-task to the extent that the executor does not need to judge - the object is fixed, the source is fixed, and the output field is fixed; the task that can&#x27;t be cut is left to a single session to do slowly, and opening a hundred splits can&#x27;t save it.</p>

<h2 id="规则二能失败但必须降级">Rule 2: You can fail, but you must be downgraded.</h2>

<p>Back to the 402 at the beginning. The built-in web_search is a quota system, and it is normal to run out during large-scale scanning. The self-help path of the sub-agent is the working area.<code class="language-plaintext highlighter-rouge">.research/</code>Two scripts in the directory: esearch.sh adjusts the search API of Oriental Fortune to parse the date, title, media name, link and summary; brss.sh requests Bing&#x27;s RSS interface to parse the title, link and description. The quality of the source is worse than that of the full-volume web page search, but there is no quota. Financial information and Chinese web pages each occupy one, and the output format follows the needs of the sub-agent, so as not to waste the context window that is originally tight.</p>

<p>I added a hard discipline to this path: for any material obtained by downgrade retrieval, the output report must have a &quot;retrieval restriction statement&quot;, stating which downgrade path is used and what coverage is missing. The credibility of the conclusions supported by the downgrade search has been discounted, and people who read the report (often a week apart) have the right to know this discount. The cost of honest marking is a paragraph, and the cost of not marking is to treat local sources as full evidence.</p>

<p>This rule only cares about one kind of problem: external dependence is gone, and whether the task can continue. In the early days of the system, it was luck that the system could survive by turning over the old scripts by itself. The 402 that time, it happened to rely on the fact that there were two old scripts lying in the work area, and turning &quot;just in&quot; into &quot;inevitable&quot; was what this rule should do. But not all failures depend on failure - in one kind of accident, the tools are all good, and the bad thing is that the action itself has no access control, which is the third rule.</p>

<p>What can be taken away: preset the downgrade path for each type of task (which backup link is hung by the main tool, and how to mark the discount on the downgrade material). The survivability of the system is not how smooth the normal path is, but whether the downgrade path exists in advance.</p>

<h2 id="规则三判断和动作都需要确定性门禁">Rule 3: Judgment and action need definite access control.</h2>

<p>Another assembly line of DSH is three-stage: ChatGPT comes out, DeepSeek lands, and ChatGPT reviews. In the third paragraph, I made an agreement--<strong>The review opinions must be verified mechanically before implementation.</strong>。</p>

<p>The source is the actual test record of 2026-08-16. The two consecutive rounds of review of the sample2 task reported &quot;badge Markdown grammar damage&quot;, and the mechanical verification gave 4/4: the badge format all matched the standard style, the brackets matched and balanced, and the damage pattern claimed by the review appeared 0 times in the product. Judged as a false report, rejected, and the product did not move. In the same batch of tests, the first round of review of sample1 caught a real bug - the abstract generator skipped the subdirectory file, resulting in the lack of source code of the abstract. After the repair, the second round of review passed.</p>

<p>The same review model can not only catch real bugs, but also create problems that do not exist at all. If you take all the review opinions as instructions, you will change the code for illusions; if you take it as a wind, you will miss the real bug. The reliable dividing line is mechanical verification: if the reviewer says that it is bad, it will use regulars, tests and practice to verify that the bad method does not exist. If it exists, it will be repaired according to priority, and if it does not exist, it will be rejected.</p>

<p>The lesson of the judgment side comes from the illusion of judging, and the lesson of the action side comes from 449 empty emails. On August 22, a sub-agent carried out the task of sending letters for the external project, sending 449 empty body emails. In hindistance, this is not a downgrade failure: the SMTP channel is good, and the sending action is also &quot;successful&quot;, but the bad one is that there is no gate control to stop it. &quot;The text is empty, why is it still sent&quot;? The conversation records of the next two days were all accident recovery: the SMTP channel was verified 323/323 one by one, and reissued according to the grade the next day (3 apologies, 10 explanations, and 310 text reissues), and then the text non-empty verification and evidence ledger were added to the letter-sending tasks. This kind of accident has the same origin as the evaluation illusion: the agent&#x27;s self-narration will be wrong, the agent&#x27;s action will also be wrong, and once the action is external, the error will directly fall into the other person&#x27;s inbox. The downgrade saved the tools, and the action could not be saved without defense.</p>

<p>Therefore, access control should be samelized on each type of judgment and action. I fixedly run four ways: mechanical verification before the review opinion enters the execution queue (regular, test, actual run); preflight before sending an email into the sending queue (the text is not empty, the number of recipients is expected, the preview is kept in the file); the data is written before schema verification, and the field is not complete and refuses to write; the external action is dry-run first and then done. The common point of the four is that it is checked with deterministic code, not to send another agent to take a look. The verification itself is not expensive, a regular rule plus a test run; the expensive version is the version without access control - change the code for the illusion once, miss a real bug online, or send an empty email to 449 people.</p>

<p>Practice that can be taken away: the judgment and action are first entered into the access control queue, and then entered the execution queue. The access control is written as a check that can run automatically (regular rule, test, diff comparison, schema verification, preflight). Don&#x27;t rely on the human eye to check it - the human eye check it again, which is equivalent to introducing another reviewer who will make mistakes.</p>

<h2 id="边界">Border</h2>

<p>The three rules control the three types of risks of parallelization, downgrade, judgment and action, and cannot control &quot;what to study&quot;. 1M The context window sounds big. What is really difficult in a two-week study is the continuity of judgment. At present, I still do it myself. The downgrade path solves the survival problem of quotas, and the deterministic access control solves the credibility problem of review and action, but the machine has not answered the topic selection for me. This is also the reason why I wrote three rules at the system level - the model is changed every half a year, and the skeleton of the system will be used for many years. The operation and maintenance layer has also paid the tuition fee (macOS permission locked the log, the service failed to pull up repeatedly with the exit code 78, and the data was moved out of ~/Documents and eradicated), but it was a one-time pit, which was gone after repair, and it was not worthy of the rules.</p>

<p>These three rules are all system-level: if you change DeepSeek, it will still work. If you only change the model and don&#x27;t make rules, the bills of quotas, illusions and empty mail will come again.</p>

  </div>

  

<aside class="kb-related" aria-label="Relevant research materials">
  <h2>Relevant research materials</h2>
  <p>Reports, data and notes are kept in the database and can continue to be consulted. The following is related to the same topic; the evidence directly used in this article shall be subject to the text citation.</p>
  
  <ul></ul>
  <ul>
    <li><a href="/en/knowledge/research-workflows/">Connect the research workflow to the inspectable product.</a></li>
  
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
