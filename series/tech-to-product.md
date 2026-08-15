---
layout: default
title: 系列 · 技术 → 产品翻译
permalink: /series/tech-to-product/
description: 把技术机会翻译成产品与商业决策的判断方法：市场角色、竞品分析、需求证据、AI Native 产品形态。
lang_switch_url: /en/
---

<section class="page-intro shell">
  <p class="eyebrow">SERIES A</p>
  <h1>技术 → 产品翻译</h1>
  <p class="page-deck">新技术出现时，最难的不是理解技术，而是判断它应该变成什么产品、先服务谁、凭什么成立。这个系列把"技术机会 → 产品定义 → 商业决策"的翻译过程拆成可复用的判断方法。</p>
</section>

<section class="archive shell">
  <div class="archive-year">
    <h2>为什么读这个系列</h2>
    <div class="archive-items">
      <article class="archive-item">
        <div>
          <p>如果你在做 AI、硬件或 Agent 相关的产品决策，这个系列回答的是同一类问题：面对一个看起来很大的机会，什么证据能证明它值得做，什么信号说明该停。</p>
        </div>
      </article>
    </div>
  </div>

  <div class="archive-year">
    <h2>系列文章</h2>
    <div class="archive-items">
      {% assign series_posts = site.posts | where_exp: "post", "post.tags contains '市场进入' or post.tags contains '产品策略' or post.tags contains '商业化' or post.tags contains '竞品分析' or post.tags contains '用户研究' or post.tags contains 'AI Native'" %}
      {% for post in site.posts %}
        {% if post.path contains 'market-roles-remove-uncertainty' or post.path contains 'competitive-analysis-software-hardware' or post.path contains 'scene-user-demand-evidence-research' or post.path contains 'ai-native-basic-unit' or post.path contains 'waic-from-models-to-systems' %}
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
          <p>从 <a href="{{ '/notes/market-roles-remove-uncertainty/' | relative_url }}">Geek、Professional、B、C</a> 开始——它定义了整套方法的总纲：先找最大的未知，再选能暴露它的市场。之后按你的当前问题选择：<a href="{{ '/notes/competitive-analysis-software-hardware/' | relative_url }}">竞品分析</a>（怎么比较对手）、<a href="{{ '/notes/scene-user-demand-evidence-research/' | relative_url }}">需求证据</a>（怎么验证用户）、<a href="{{ '/notes/ai-native-basic-unit/' | relative_url }}">AI Native 产品形态</a>（怎么定义产品）。</p>
        </div>
      </article>
    </div>
  </div>
</section>
