---
layout: default
title: 系列 · 技术 → 产品翻译
permalink: /series/tech-to-product/
description: 把技术机会翻译成产品与商业决策的判断方法：市场角色、竞品分析、需求证据、AI Native 产品形态。
lang_switch_url: /en/
---

<section class="series-hero shell">
  <p class="eyebrow">系列 A · 判断方法</p>
  <h1>技术 → 产品翻译</h1>
  <p class="series-deck">新技术不缺解读，缺翻译。把一个技术机会变成什么产品、先服务谁、凭什么成立——这个系列把翻译过程拆成可复用的判断方法。</p>
</section>

<section class="series-block shell" aria-labelledby="theses-title">
  <header class="series-block-heading">
    <h2 id="theses-title">这个系列的核心判断</h2>
  </header>
  <ol class="series-thesis-list">
    <li>
      <span class="series-thesis-num">01</span>
      <div>
        <h3>市场不是阶梯，是证据环境</h3>
        <p>Geek、Professional、领域 B 端与大众消费者不是成熟度等级，而是四种证据环境，各自消灭不同的未知。选择下一站，先选最合适的证据场，而不是最大的市场。</p>
      </div>
    </li>
    <li>
      <span class="series-thesis-num">02</span>
      <div>
        <h3>竞品比较工作流，不比较参数表</h3>
        <p>软件比工作流、迁移与持续变化；硬件还要比物理系统、量产可靠性与服务。参数表没有洞察，只有坐标。</p>
      </div>
    </li>
    <li>
      <span class="series-thesis-num">03</span>
      <div>
        <h3>样本量不等于证据</h3>
        <p>20 万条用户反馈可能全是噪音。需求判断需要证据分级、场景还原与反例检验——先定义什么算证据，再谈样本。</p>
      </div>
    </li>
    <li>
      <span class="series-thesis-num">04</span>
      <div>
        <h3>AI Native 之后，产品的基本单位变了</h3>
        <p>页面与文件不会消失，但会退化为同一份语义与任务状态的不同视图。产品定义要从对象模型开始，而不是从界面开始。</p>
      </div>
    </li>
  </ol>
</section>

<section class="series-block shell" aria-labelledby="articles-title">
  <header class="series-block-heading">
    <h2 id="articles-title">系列文章</h2>
  </header>

  {% assign entry_slug = 'market-roles-remove-uncertainty' %}
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
      {% if post.lang == 'en' %}{% continue %}{% endif %}
      {% if post.path contains 'market-roles-remove-uncertainty' or post.path contains 'competitive-analysis-software-hardware' or post.path contains 'scene-user-demand-evidence-research' or post.path contains 'ai-native-basic-unit' or post.path contains 'waic-from-models-to-systems' %}
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
    <li><span>1</span><p>先读入口文章，建立总纲：先找最大的未知，再选能暴露它的市场。</p></li>
    <li><span>2</span><p>按你当前的问题选读：<a href="{{ '/notes/competitive-analysis-software-hardware/' | relative_url }}">怎么比较对手</a>、<a href="{{ '/notes/scene-user-demand-evidence-research/' | relative_url }}">怎么验证用户</a>。</p></li>
    <li><span>3</span><p>用 <a href="{{ '/notes/ai-native-basic-unit/' | relative_url }}">AI Native 产品形态</a> 收束：把判断落回产品定义。</p></li>
  </ol>
</section>

<nav class="series-nav shell" aria-label="其他系列">
  <a class="series-nav-link" href="{{ '/series/agent-and-terminals/' | relative_url }}">
    <span>下一个系列</span>
    <strong>Agent 与 AI 终端 <span aria-hidden="true">→</span></strong>
  </a>
  <a class="series-nav-link" href="{{ '/series/software-to-hardware-pm/' | relative_url }}">
    <span>另一个角度</span>
    <strong>从软件到硬件的产品管理 <span aria-hidden="true">→</span></strong>
  </a>
</nav>
