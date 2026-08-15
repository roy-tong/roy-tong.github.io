---
layout: default
title: 系列 · 从软件到硬件的产品管理
permalink: /series/software-to-hardware-pm/
description: 跨软硬件做产品与组织时真正不同的变量：变更经济性、组织阶段、阶段门与系统 Owner。
lang_switch_url: /en/
---

<section class="page-intro shell">
  <p class="eyebrow">SERIES C</p>
  <h1>从软件到硬件的产品管理</h1>
  <p class="page-deck">软件迭代以天计，硬件变更以阶段门计。当产品同时包含两者，管理的难点不是各自的方法，而是把它们放进同一套系统。这个系列记录我从软件产品走向软硬一体的判断、组织方法与管理复盘。</p>
</section>

<section class="archive shell">
  <div class="archive-year">
    <h2>为什么读这个系列</h2>
    <div class="archive-items">
      <article class="archive-item">
        <div>
          <p>如果你是从软件/AI 转向硬件产品，或在管理软硬一体的团队，这个系列回答的是同一类问题：组织上为什么做不出来、阶段门怎么设、负责人权责怎么划、机器人与家庭场景为什么难。</p>
        </div>
      </article>
    </div>
  </div>

  <div class="archive-year">
    <h2>系列文章</h2>
    <div class="archive-items">
      {% for post in site.posts %}
        {% if post.lang != 'en' and (post.path contains 'from-ai-software-to-physical-world' or post.path contains 'hardware-innovation-organization-management' or post.path contains 'appointed-manager-organizational-legitimacy' or post.path contains 'home-robots-harder-richer') %}
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
          <p>从 <a href="{{ '/notes/from-ai-software-to-physical-world/' | relative_url }}">从 AI 应用到真实世界</a> 开始（我为什么转向），再到 <a href="{{ '/notes/hardware-innovation-organization-management/' | relative_url }}">硬件组织的管理方法</a>（系统框架），然后是 <a href="{{ '/notes/appointed-manager-organizational-legitimacy/' | relative_url }}">空降管理者</a>（个人视角）和 <a href="{{ '/notes/home-robots-harder-richer/' | relative_url }}">家庭机器人</a>（场景判断）。</p>
        </div>
      </article>
    </div>
  </div>
</section>
