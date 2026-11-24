---
title: "How AI products go from \"doable\" to \"worth using\": the three thresholds of adoption, delivery and acceptance"
date: "2026-10-10T00:00:00+08:00"
lang: en
permalink: "/en/notes/ai-product-value-loop/"
generated_translation: true
content_id: ai-product-value-loop
knowledge_topic: product-research
knowledge_units: [research-workflows]
translation_of: /notes/ai-product-value-loop/
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




      <link rel="alternate" hreflang="en" href="https://roy-tong.github.io/en/notes/ai-product-value-loop/">
      <link rel="alternate" hreflang="zh-CN" href="https://roy-tong.github.io/notes/ai-product-value-loop/">
      <link rel="alternate" hreflang="x-default" href="https://roy-tong.github.io/notes/ai-product-value-loop/">
    <link type="application/atom+xml" rel="alternate" href="https://roy-tong.github.io/feed.xml" title="Roy.Tong"/>
    <!-- Begin Jekyll SEO tag v2.8.0 -->
<title>How AI products go from &quot;doable&quot; to &quot;worth using&quot;: the three thresholds of adoption, delivery and acceptance | Roy.Tong</title>
<meta name="generator" content="Jekyll v3.9.5"/>
<meta property="og:title" content="How AI products go from &quot;doable&quot; to &quot;worth using&quot;: the three thresholds of adoption, delivery and acceptance">
<meta name="author" content="Roy.Tong"/>
<meta property="og:locale" content="en_US">
<meta name="description" content="Put shooting, end-side AI, creative software and Agent measurement together, distinguish the existence of problems, scheme adoption, complete delivery and verifiable results, and give the next round of experimental methods.">
<meta property="og:description" content="Put shooting, end-side AI, creative software and Agent measurement together, distinguish the existence of problems, scheme adoption, complete delivery and verifiable results, and give the next round of experimental methods.">
<link rel="canonical" href="https://roy-tong.github.io/en/notes/ai-product-value-loop/">
<meta property="og:url" content="https://roy-tong.github.io/en/notes/ai-product-value-loop/">
<meta property="og:site_name" content="Roy.Tong"/>
<meta property="og:image" content="https://roy-tong.github.io/assets/images/social-preview.png"/>
<meta property="og:type" content="article"/>
<meta property="article:published_time" content="2026-10-10T00:00:00+08:00"/>
<meta name="twitter:card" content="summary_large_image"/>
<meta property="twitter:image" content="https://roy-tong.github.io/assets/images/social-preview.png"/>
<meta property="twitter:title" content="How AI products go from &quot;doable&quot; to &quot;worth using&quot;: the three thresholds of adoption, delivery and acceptance">
<script type="application/ld+json">
{"@context":"https://schema.org","@type":"BlogPosting","author":{"@type":"Person","name":"Roy.Tong"},"dateModified":"2026-10-10T00:00:00+08:00","datePublished":"2026-10-10T00:00:00+08:00","description":"把拍摄、端侧 AI、创作软件与 Agent 计量放在一起，区分问题存在、方案采用、完整交付和可验证结果，并给出下一轮实验方法。","headline":"AI 产品怎样从“做得到”走到“值得用”：采用、交付与验收的三道门槛","image":"https://roy-tong.github.io/assets/images/social-preview.png","mainEntityOfPage":{"@type":"WebPage","@id":"https://roy-tong.github.io/notes/ai-product-value-loop/"},"publisher":{"@type":"Organization","logo":{"@type":"ImageObject","url":"https://roy-tong.github.io/assets/images/social-preview.png"},"name":"Roy.Tong"},"url":"https://roy-tong.github.io/notes/ai-product-value-loop/"}</script>
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
            <a class="language-toggle" href="/notes/ai-product-value-loop/" hreflang="zh-CN" lang="zh-CN" data-language-switch data-target-language="zh-CN" aria-label="切换至中文" title="切换至中文">中文</a>
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

    <main id="main"><p class="translation-note" aria-label="Translation note">Machine-assisted translation. <a href="/notes/ai-product-value-loop/">Read the Chinese original</a>.</p>
      




<article class="post shell reading-shell">
  <header class="post-header">
    <a class="eyebrow back-link" href="/en/archive/">← Back to the article</a>
    <h1>How can AI products go from &quot;doable&quot; to &quot;worth using&quot;: the three thresholds of adoption, delivery and acceptance</h1>
    
    <div class="post-meta">
      <time datetime="2026-10-10T00:00:00+08:00">2026-10-10</time>
      
      
      <a class="post-translation" href="/notes/ai-product-value-loop/" hreflang="zh-CN">阅读中文版 →</a>
      
        <span class="post-tags">
          <a href="/en/tags/#ai%E4%BA%A7%E5%93%81">#AI products</a><a href="/en/tags/#%E4%BA%A7%E5%93%81%E7%A0%94%E7%A9%B6">#Product research</a><a href="/en/tags/#agent">#Agent</a><a href="/en/tags/#%E6%99%BA%E8%83%BD%E7%A1%AC%E4%BB%B6">#Smart hardware</a>
        </span>
      
    </div>
  </header>

  <div class="prose">
    <p>Put shooting, end-side AI, creative software and Agent measurement together, distinguish the existence of problems, scheme adoption, complete delivery and verifiable results, and give the next round of experimental methods.</p>

<h2 id="研究问题用户究竟在验收哪一件事">Research question: What exactly is the user accepting?</h2>

<p>A camera can track people, a set of local models can answer questions, and an Agent can call tools continuously. These abilities may be useful, but they have not answered the same question: is it easier for users to do what they originally wanted to do?</p>

<p>I put the research of shooting, end-side AI, home robots, creative software and Agent measurement together, and got a judgment worth continuing to test: product definitions are easy to sk in three places. If a problem is found, it is assumed that the user will adopt a certain scheme; if the local capability is seen, it is assumed that the complete task has been delivered; if the success log is obtained, it is assumed that the result has been used and value has been created.</p>

<p>This report organizes them into three thresholds: adoption, delivery and acceptance. It is a set of cross-project analysis and experimental design framework, not a market scale prediction, nor a completed cross-industry causal experiment. Publicly based on existing research notes, fixed versions of open source projects and official documents checked in this round.</p>

<h2 id="第一道门槛有困难不等于愿意采用你的方案">The first threshold: having difficulties does not mean that you are willing to adopt your plan.</h2>

<p>If users want to shoot good videos, it does not mean that they are willing to add a mobile device; if they want to reduce the cost of AI, it does not mean that they are willing to maintain local servers. Even if a plan solves the old problem, it may also bring new requirements for installation, learning, maintenance or use of the environment.</p>

<p>Research should first record how users complete the task now. Are you putting up with tedious steps, or do you already have a good enough alternative? When will the difficulties occur and who will bear the consequences? What are the conditions for accepting the new plan? These problems need to be explained in the same role and scene. One person&#x27;s complaints, another person&#x27;s purchases and a third person&#x27;s long-term use cannot be put together into a complete user that does not exist.</p>

<p>The SURE method I use distinguishes between scenarios, problems, alternative behaviors, program acceptance and business behaviors. The tool can check the field and evidence threshold, but it cannot prove the real existence of the demand for the researcher. A large number of discussion materials are suitable for helping to find problems to be verified; if there is evidence of prototype acceptance or actual use, continuing to expand the background corpus will not automatically fill in this gap.</p>

<h2 id="第二道门槛衡量完整任务保留被省略的人类工作">The second threshold: measure the complete task and keep the omitted human work</h2>

<p>When evaluating automation, draw the starting and ending points of the task first. Shooting tasks may start from erecting equipment to selecting fragments, modifying and obtaining available content; local AI tasks may include installing models, authorizing data, retrieving, generating, proofreading and saving. Only test the fastest section in the middle, which will hide the labor before and after.</p>

<p>A hypothetical example: it takes a total of eight minutes to prepare and finish the old plan; the new equipment reduces the shooting operation by four minutes, but adds three minutes of pairing and four minutes of film selection. Here, you can&#x27;t claim efficiency improvement just by &quot;shooting four minutes less&quot;. Numbers are just a demonstration to explain the measurement caliber, not the actual measurement of any product.</p>

<p>A more reliable recording method is to keep the preparation time, active operation time, waiting time, rework time, maintenance time and task quality respectively. Waiting can overlap with other tasks, and the user&#x27;s attention cannot be simply added according to the wall clock time. The cost of different roles should also be separated: the buyer is convenient, and the maintainer may bear extra labor.</p>

<h2 id="拍摄和创作短而可靠的承诺也可能有价值">Shooting and creation: short and reliable promises may also be valuable</h2>

<p>From reliable records to interpretations, suggestions and even actions on behalf of users, there is no ladder to automatically add value. For one user, the stable leaving of available fragments has solved the important problem; for another user, it still needs to be sorted out a lot after shooting. The product should first identify which part of the work most hinders the completion of the task, and then decide where to commit.</p>

<p>In the shooting scene, you can compare the fixed camera position, rotating follow and mobile camera position, so that users can choose which clips are worth keeping under the same task. It is necessary to observe whether the movement has increased the content that is really needed, and also record the settings, noise, space occupation and follow-up processing. This design is better not to preset the movement, and not to preset the fixed device is always enough. Before the actual completion of the comparison, it is just a verification plan.</p>

<p>The creative software can be tested with a clear modification request: only change the background and keep the confirmed characters, lines and rhythms. In addition to the successful modification, it should also be recorded whether other parts have been changed unexpectedly. OpenTimelineIO provides an exchange structure of clip information such as fragments, tracks, time and metadata, and does not embed audio and video. This means that the production process can retain the operable structure, but the format itself does not prove that an AI tool can complete the modification stably.</p>

<p>Information:<a href="https://opentimelineio.readthedocs.io/en/latest/">OpenTimelineIO Official Document</a>, 2026-10-10 Check.</p>

<h2 id="端侧-ai先确定必须留在本地的任务">End-side AI: first determine the tasks that must remain locally</h2>

<p>End-side discussion is easy to start with equipment parameters. I&#x27;d rather ask first: which steps must be completed without the network, what data cannot leave the boundary, how often does the task occur, and who will recover after failure? These constraints determine which equipment and software should be compared, not the other way around.</p>

<p>The official instructions of LM Studio confirm that after downloading the model, you can carry out local chat, document processing and local services; functions such as model search, download and update still need to be connected to the Internet. This provides an alternative baseline for the research on existing computers. It cannot prove that the entire Agent link after accessing external tools is also offline, let alone directly prove that users need to purchase additional special equipment.</p>

<p>The Ollama document shows that increasing the context length will increase the memory required for the model to run. Therefore, the comparison cannot only list the model parameters or the peak computing power. Existing computers, dedicated local devices and allowed cloud schemes should be compared under the same tasks, quality requirements and data boundaries, and installation and maintenance, context requirements, failure handling and result availability should be recorded. What is proposed here is the evaluation condition, and it is not claimed that any route has won the total cost.</p>

<p>Information:<a href="https://lmstudio.ai/docs/app/offline">LM Studio offline instructions</a>、<a href="https://docs.ollama.com/context-length">Ollama context description</a>, 2026-10-10 Check.</p>

<h2 id="第三道门槛执行成功之后结果仍需验收">The third threshold: After successful implementation, the result still needs to be accepted.</h2>

<p>The completion of a tool call can prove that the call returns a certain result; it does not necessarily prove that the user&#x27;s goal has been achieved. The generation of the report file does not mean that the content is accurate; the appointment is created does not mean that the time and object meet the user&#x27;s requirements; two retries do not necessarily mean two independent tasks.</p>

<p>Agent measurement research should therefore distinguish between attempts, logical operations, task results, result adoption and business value. Each number must indicate the denominator and observable range. If there is a lack of reliable identification, multiple attempts cannot be classified into the same operation, and the part that cannot be judged will be retained instead of forcibly outputting the accurate success rate.</p>

<p>The fixed version of AgentMeasure README explicitly adopts PASS, FAIL and UNPROVABLE, and separates the execution fact, rule verification and economic settlement. What is quoted here is the design boundary of the project, not the independent verification of the degree of industry adoption, customer income or audit performance. The payment record can prove that the payment has occurred, but it cannot prove the incremental value alone; refunds or concessions should also be recorded separately from the original claim.</p>

<h2 id="把三道门槛变成一个可执行的对照">Turn the three thresholds into an executable comparison.</h2>

<p>The first step is to write down a user, a scenario, a commitment and an existing alternative. For example, &quot;After the fixed indoor activity, get the available footage.&quot; More intelligent&quot; and &quot;more understanding of users&quot; are not specific enough to tell the reviewer what results are passed.</p>

<p>The second step is to define acceptable results, unacceptable side effects and conditions that need to be taken over before testing. Compare the existing plan with the new plan for the same type of task, and try to keep the materials and environment consistent; let the reviewer check the results according to the pre-agreed standards. If the conditions are not consistent, keep the difference, and do not pretend to have completed the strict causal experiment.</p>

<p>The third step is to record the adoption, delivery and acceptance respectively. The adoption depends on whether the user chooses and actually uses it under given conditions; the delivery depends on the qualified completion, operation burden, maintenance and recovery; the acceptance depends on whether the result meets the standards, whether it is adopted, and what evidence is missing. For entertainment and expression tasks, the result standard can be that the user chooses to retain, share or repeat the experience, without forcibly conversion to productivity.</p>

<p>The fourth step is to save the unsuccessful and abandoned tasks, and review the strongest counterexample. If the user likes the result but is unwilling to set up the equipment on a daily basis, first study the deployment burden; if the task is completed but often needs to be rechecked, first study the checkability; if the result is reliable but not selected, return to the importance of the task and the alternative plan. Different breakpoints require different experiments, which cannot be unified because the model is not strong enough.</p>

<h2 id="研究边界这套框架还不能证明什么">Research boundaries: this framework can&#x27;t prove anything yet</h2>

<p>These studies span different products, and cross-field experiments have not been completed using unified samples and tasks. Therefore, the three thresholds are a way to sort out problems, which cannot synthesize a statistically effective industry total score, nor can it predict the success or failure of a company.</p>

<p>It is more suitable for products with clear mission commitments that need to be delivered repeatedly. Entertainment, companionship, identity expression and exploratory creation are also valuable, but the adoption is different from the acceptance method. These motives cannot be deleted because they are difficult to quantify; nor can they claim that a certain hardware, price or business model has been established because of the motive.</p>

<p>The private project budget, cooperation materials, full session or original platform user content were not included in the public report in this round. The size of the existing corpus is not equal to the number of independent users; different snapshots have not been recalculated in a unified way. The next most valuable task is to choose a specific task, compare the old plan with the new plan with the same acceptance conditions, and then revise the judgment with the actual results.</p>

<h2 id="参考资料">Reference material</h2>

<ul>
  <li><a href="https://roy-tong.github.io/knowledge/demand-evidence/">demand</a></li>
  <li><a href="https://roy-tong.github.io/knowledge/local-ai/">local</a></li>
  <li><a href="https://roy-tong.github.io/knowledge/agent-measurement/">agent</a></li>
  <li><a href="https://roy-tong.github.io/knowledge/household-robots/">home</a></li>
  <li><a href="https://roy-tong.github.io/knowledge/video-production/">video</a></li>
  <li><a href="https://opentimelineio.readthedocs.io/en/latest/">otio</a></li>
  <li><a href="https://lmstudio.ai/docs/app/offline">lmstudio</a></li>
  <li><a href="https://docs.ollama.com/context-length">ollama</a></li>
  <li><a href="https://github.com/roy-tong/AgentMeasure/blob/67c276b7d17d5a00dc2fa89681eae97f29eeda06/README.md">agent-code</a></li>
</ul>

  </div>

  

<aside class="kb-related" aria-label="Relevant research materials">
  <h2>Relevant research materials</h2>
  <p>Reports, data and notes are kept in the database and can continue to be consulted. The following is related to the same topic; the evidence directly used in this article shall be subject to the text citation.</p>
  
  <ul><li><a href="/en/knowledge/collections/local-ai/">Local AI and personal computing power · Research files</a></li><li><a href="/en/knowledge/collections/ai-video/">AI Video and Creative Tools · Research Archives</a></li><li><a href="/en/knowledge/collections/agent-systems/">Agent System and Capacity Measurement · Research Archive</a></li><li><a href="/en/knowledge/collections/product-research/">Product Research and Organization Methods · Research Archives</a></li></ul>
  <ul>
    <li><a href="/en/knowledge/demand-evidence/">Demand evidence: What decision can a feedback support?</a></li>
  
    <li><a href="/en/knowledge/local-ai/">Local AI: After the task is established, there is a reason to purchase the equipment.</a></li>
  
    <li><a href="/en/knowledge/agent-measurement/">Agent measurement: execution facts, task results and value</a></li>
  
    <li><a href="/en/knowledge/video-production/">AI video production: keep what has been confirmed and then modify the rest</a></li>
  
    <li><a href="/en/knowledge/household-robots/">Home Robot: Mission Commitment and Failure Recovery</a></li>
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
