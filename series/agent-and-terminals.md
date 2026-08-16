---
layout: default
title: 系列 · Agent 与 AI 终端
permalink: /series/agent-and-terminals/
description: 信息空间与物理世界里的新产品形态：Agent 运行时、具身智能、机器人、AI 可穿戴与空间计算。
lang_switch_url: /en/
---

<section class="series-hero shell">
  <p class="eyebrow">系列 B · 产品形态</p>
  <h1>Agent 与 AI 终端</h1>
  <p class="series-deck">AI 同时走向两个方向：在信息空间里变成 Agent，在物理世界里变成新的终端与身体。这个系列研究两条路的产品形态、交互范式与经济结构。</p>
</section>

<section class="series-block shell" aria-labelledby="theses-title">
  <header class="series-block-heading">
    <h2 id="theses-title">这个系列的核心判断</h2>
  </header>
  <ol class="series-thesis-list">
    <li>
      <span class="series-thesis-num">01</span>
      <div>
        <h3>RAG 之后，Agent 需要 Context Recommendation</h3>
        <p>复杂 Agent 要解决的，是每一轮该注入什么上下文、工具、状态与权限——这是独立于检索的系统能力。</p>
      </div>
    </li>
    <li>
      <span class="series-thesis-num">02</span>
      <div>
        <h3>Agent 向左，具身向右</h3>
        <p>共享模型能力的两条路线，在失败成本、评测、安全、部署与商业化上逐步分岔。它们会越来越不像同一个行业。</p>
      </div>
    </li>
    <li>
      <span class="series-thesis-num">03</span>
      <div>
        <h3>机器人不是替代人，是给人新的身体</h3>
        <p>视野、在场、动作与身体属性——能力增益是比替代率更接近用户价值的坐标。</p>
      </div>
    </li>
    <li>
      <span class="series-thesis-num">04</span>
      <div>
        <h3>AI 可穿戴的竞争，不是眼镜对耳机</h3>
        <p>真正要比较的是模态、控制、身体位置与长期佩戴成本组成的整套系统。</p>
      </div>
    </li>
    <li>
      <span class="series-thesis-num">05</span>
      <div>
        <h3>空间计算需要自己的触控时刻</h3>
        <p>缺的不是更多手势，是跨应用稳定、可组合、可撤销的公共交互语法。</p>
      </div>
    </li>
  </ol>
</section>

<section class="series-block shell" aria-labelledby="articles-title">
  <header class="series-block-heading">
    <h2 id="articles-title">系列文章</h2>
  </header>

  {% assign entry_slug = 'agent-left-embodied-right' %}
  {% for post in site.posts %}
    {% if post.lang != 'en' and post.path contains entry_slug %}
      <a class="series-entry" href="{{ post.url | relative_url }}">
        <div>
          <span class="series-entry-tag">入口文章</span>
          <h3>{{ post.title }}</h3>
          {% if post.subtitle %}<p>{{ post.subtitle }}</p>{% endif %}
        </div>
        <span class="series-entry-arrow" aria-hidden="true">↗</span>
      </a>
    {% endif %}
  {% endfor %}

  <div class="series-article-list">
    {% for post in site.posts %}
      {% if post.lang != 'en' and (post.path contains 'agent-context-recommendation-after-rag' or post.path contains 'agent-left-embodied-right' or post.path contains 'robots-give-people-new-bodies' or post.path contains 'ai-wearable-modalities-body-comfort' or post.path contains 'spatial-computing-touch-moment') %}
        {% if post.path contains entry_slug %}{% continue %}{% endif %}
        <a class="series-article-row" href="{{ post.url | relative_url }}">
          <time datetime="{{ post.date | date_to_xmlschema }}">{{ post.date | date: '%m.%d' }}</time>
          <div>
            <h3>{{ post.title }}</h3>
            {% if post.subtitle %}<p>{{ post.subtitle }}</p>{% endif %}
          </div>
          <span aria-hidden="true">↗</span>
        </a>
      {% endif %}
    {% endfor %}
  </div>
</section>

<section class="series-block series-path-block shell" aria-labelledby="path-title">
  <header class="series-block-heading">
    <h2 id="path-title">怎么读这个系列</h2>
  </header>
  <ol class="series-path-list">
    <li><span>1</span><p>先读入口文章，看清两条路线的分界与各自约束。</p></li>
    <li><span>2</span><p>信息空间线：<a href="{{ '/notes/agent-context-recommendation-after-rag/' | relative_url }}">Context Recommendation</a>；物理世界线：<a href="{{ '/notes/robots-give-people-new-bodies/' | relative_url }}">机器人给人新身体</a>。</p></li>
    <li><span>3</span><p>终端形态看 <a href="{{ '/notes/ai-wearable-modalities-body-comfort/' | relative_url }}">AI Wearable</a> 与 <a href="{{ '/notes/spatial-computing-touch-moment/' | relative_url }}">空间计算</a>，比较不同形态的交互入口。</p></li>
  </ol>
</section>

<nav class="series-nav shell" aria-label="其他系列">
  <a class="series-nav-link" href="{{ '/series/tech-to-product/' | relative_url }}">
    <span>上一个系列</span>
    <strong>技术 → 产品翻译 <span aria-hidden="true">→</span></strong>
  </a>
  <a class="series-nav-link" href="{{ '/series/software-to-hardware-pm/' | relative_url }}">
    <span>下一个系列</span>
    <strong>从软件到硬件的产品管理 <span aria-hidden="true">→</span></strong>
  </a>
</nav>
