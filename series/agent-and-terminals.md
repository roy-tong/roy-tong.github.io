---
layout: default
title: 系列 · Agent 与 AI 终端
permalink: /series/agent-and-terminals/
description: 信息空间与物理世界里的新产品形态：Agent 运行时、具身智能、机器人、AI 可穿戴与空间计算。
lang_switch_url: /en/
---

<section class="page-intro shell">
  <p class="eyebrow">SERIES B</p>
  <h1>Agent 与 AI 终端</h1>
  <p class="page-deck">AI 同时走向两个方向：在信息空间里变成 Agent，在物理世界里变成新的终端和身体。这个系列研究这两条路的产品形态、交互范式与经济结构。</p>
</section>

<section class="archive shell">
  <div class="archive-year">
    <h2>为什么读这个系列</h2>
    <div class="archive-items">
      <article class="archive-item">
        <div>
          <p>如果你在观察或参与 Agent、机器人、AI 硬件赛道，这个系列提供的是判断坐标：Agent 的下一步是上下文编排，终端的胜负手是交互范式，机器人给人增加的是能力而不是替代关系。</p>
        </div>
      </article>
    </div>
  </div>

  <div class="archive-year">
    <h2>系列文章</h2>
    <div class="archive-items">
      {% for post in site.posts %}
        {% if post.path contains 'agent-context-recommendation-after-rag' or post.path contains 'agent-left-embodied-right' or post.path contains 'robots-give-people-new-bodies' or post.path contains 'ai-wearable-modalities-body-comfort' or post.path contains 'spatial-computing-touch-moment' %}
          <article class="archive-item">
            <time datetime="{{ post.date | date_to_xmlschema }}">{{ post.date | date: '%m 月 %d 日' }}</time>
            <div>
              <h3><a href="{{ post.url | relative_url }}">{{ post.title }}</a></h3>
              {% if post.subtitle %}<p>{{ post.subtitle }}</p>{% endif %}
            </div>
            <a class="post-arrow" href="{{ post.url | relative_url }}" aria-label="阅读《{{ post.title }}》">↗</a>
          </article>
        {% endif %}
      {% endfor %}
    </div>
  </div>

  <div class="archive-year">
    <h2>建议阅读顺序</h2>
    <div class="archive-items">
      <article class="archive-item">
        <div>
          <p>从 <a href="{{ '/notes/agent-left-embodied-right/' | relative_url }}">Agent 向左，具身向右</a> 开始——它划定了两条路线的分界。信息空间继续读 <a href="{{ '/notes/agent-context-recommendation-after-rag/' | relative_url }}">Context Recommendation</a>；物理世界继续读 <a href="{{ '/notes/robots-give-people-new-bodies/' | relative_url }}">机器人给人新身体</a>，终端形态看 <a href="{{ '/notes/ai-wearable-modalities-body-comfort/' | relative_url }}">AI Wearable</a> 与 <a href="{{ '/notes/spatial-computing-touch-moment/' | relative_url }}">空间计算触控时刻</a>。</p>
        </div>
      </article>
    </div>
  </div>
</section>
