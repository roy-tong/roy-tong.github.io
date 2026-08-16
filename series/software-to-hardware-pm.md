---
layout: default
title: 系列 · 从软件到硬件的产品管理
permalink: /series/software-to-hardware-pm/
description: 跨软硬件做产品与组织时真正不同的变量：变更经济性、组织阶段、阶段门与系统 Owner。
lang_switch_url: /en/
---

<section class="series-hero shell">
  <p class="eyebrow">系列 C · 组织与管理</p>
  <h1>从软件到硬件的产品管理</h1>
  <p class="series-deck">软件迭代以天计，硬件变更以阶段门计。当产品同时包含两者，难点不是各自的方法，而是把它们放进同一套系统。这个系列记录我从软件走向软硬一体的判断、组织方法与管理复盘。</p>
</section>

<section class="series-block shell" aria-labelledby="theses-title">
  <header class="series-block-heading">
    <h2 id="theses-title">这个系列的核心判断</h2>
  </header>
  <ol class="series-thesis-list">
    <li>
      <span class="series-thesis-num">01</span>
      <div>
        <h3>智能硬件是三种节奏的叠加</h3>
        <p>硬件阶段门 + 软件持续交付 + 系统工程。管理难点来自变更经济性的差异：改一行代码和改一个模具不是同一种成本。</p>
      </div>
    </li>
    <li>
      <span class="series-thesis-num">02</span>
      <div>
        <h3>组织按三类风险配人</h3>
        <p>价值风险、技术/系统风险、交付/商业风险。早期 6-10 个关键角色，可以兼任，但 Owner 不能模糊。</p>
      </div>
    </li>
    <li>
      <span class="series-thesis-num">03</span>
      <div>
        <h3>头衔不等于合法性</h3>
        <p>头衔提供决策权，共同解决问题的记录才形成组织合法性。空降管理者的第一任务是稳定并诊断，而不是证明自己。</p>
      </div>
    </li>
    <li>
      <span class="series-thesis-num">04</span>
      <div>
        <h3>家庭不是一个场景</h3>
        <p>变化环境、多人关系、多任务长尾与多支付机制叠加，让技术更难、经济可能更丰富——单任务 ROI 不高不等于经济性差。</p>
      </div>
    </li>
  </ol>
</section>

<section class="series-block shell" aria-labelledby="articles-title">
  <header class="series-block-heading">
    <h2 id="articles-title">系列文章</h2>
  </header>

  {% assign entry_slug = 'from-ai-software-to-physical-world' %}
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
      {% if post.lang != 'en' and (post.path contains 'from-ai-software-to-physical-world' or post.path contains 'hardware-innovation-organization-management' or post.path contains 'appointed-manager-organizational-legitimacy' or post.path contains 'home-robots-harder-richer') %}
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
    <li><span>1</span><p>先读入口文章：为什么从软件转向物理世界产品，这决定了后面所有判断的出发点。</p></li>
    <li><span>2</span><p>再读 <a href="{{ '/notes/hardware-innovation-organization-management/' | relative_url }}">组织与管理方法</a>，建立系统框架：三类风险、组织阶段、阶段门与 System Owner。</p></li>
    <li><span>3</span><p>最后是两个场景案例：<a href="{{ '/notes/appointed-manager-organizational-legitimacy/' | relative_url }}">空降管理者</a>（个人视角）与 <a href="{{ '/notes/home-robots-harder-richer/' | relative_url }}">家庭机器人</a>（场景判断）。</p></li>
  </ol>
</section>

<nav class="series-nav shell" aria-label="其他系列">
  <a class="series-nav-link" href="{{ '/series/agent-and-terminals/' | relative_url }}">
    <span>上一个系列</span>
    <strong>Agent 与 AI 终端 <span aria-hidden="true">→</span></strong>
  </a>
  <a class="series-nav-link" href="{{ '/series/tech-to-product/' | relative_url }}">
    <span>回到起点</span>
    <strong>技术 → 产品翻译 <span aria-hidden="true">→</span></strong>
  </a>
</nav>
