(function () {
  'use strict';
  const form = document.querySelector('[data-kb-search]');
  if (!form) return;
  const query = form.querySelector('[name="q"]');
  const topic = form.querySelector('[name="topic"]');
  const kind = form.querySelector('[name="kind"]');
  const status = document.querySelector('[data-kb-status]');
  const results = document.querySelector('[data-kb-results]');
  const list = document.querySelector('[data-kb-result-list]');
  const names = { knowledge: '知识单元', article: '文章', project: '项目' };
  let records = [];
  let topics = {};
  let ready = false;
  const normalize = value => String(value || '').normalize('NFKC').toLocaleLowerCase();
  function readHash() {
    const params = new URLSearchParams(window.location.hash.slice(1));
    query.value = (params.get('q') || '').slice(0, 200);
    topic.value = params.get('topic') || '';
    kind.value = params.get('kind') || '';
  }
  function saveHash() {
    const params = new URLSearchParams();
    if (query.value.trim()) params.set('q', query.value.trim());
    if (topic.value) params.set('topic', topic.value);
    if (kind.value) params.set('kind', kind.value);
    const fragment = params.toString();
    // Fragments stay in the browser; search terms are not sent to the server.
    window.history.replaceState(null, '', window.location.pathname + window.location.search + (fragment ? '#' + fragment : ''));
  }
  function safeUrl(value) {
    try {
      const url = new URL(value, window.location.origin);
      return url.origin === window.location.origin || (url.protocol === 'https:' && url.hostname === 'github.com') ? url.href : null;
    } catch (error) { return null; }
  }
  function render() {
    if (!ready) return;
    const terms = normalize(query.value.trim()).split(/\s+/).filter(Boolean);
    const active = terms.length || topic.value || kind.value;
    list.replaceChildren();
    results.hidden = !active;
    if (!active) {
      status.textContent = '可检索 ' + records.length + ' 个公开条目（含英文译文）。也可以直接浏览下方主题。';
      return;
    }
    const matches = records.filter(row => (!topic.value || row.topic === topic.value) &&
      (!kind.value || row.kind === kind.value) && terms.every(term => row.search.includes(term)));
    matches.sort((a, b) => {
      const score = row => terms.reduce((sum, term) => sum + (normalize(row.title).includes(term) ? 10 : 0) + (normalize(row.summary).includes(term) ? 3 : 0), 0);
      return score(b) - score(a) || (a.kind === 'knowledge' ? -1 : 0) - (b.kind === 'knowledge' ? -1 : 0);
    });
    status.textContent = matches.length ? '找到 ' + matches.length + ' 个条目。英文译文不代表独立证据。' : '没有匹配结果。试试更短的关键词，或清空主题和类型限制。';
    const fragment = document.createDocumentFragment();
    matches.forEach(row => {
      const li = document.createElement('li');
      const meta = document.createElement('span');
      meta.className = 'kb-result-meta';
      meta.textContent = (names[row.kind] || '内容') + ' · ' + (topics[row.topic] || '') + (row.lang === 'en' ? ' · EN 译文' : '');
      const heading = document.createElement('h3');
      const link = document.createElement('a');
      link.href = row.safeUrl;
      link.textContent = row.title;
      heading.append(link);
      const summary = document.createElement('p');
      summary.textContent = row.summary || '';
      li.append(meta, heading, summary);
      fragment.append(li);
    });
    list.append(fragment);
  }
  function update() { saveHash(); render(); }
  form.addEventListener('submit', event => { event.preventDefault(); update(); });
  query.addEventListener('input', event => { if (!event.isComposing) update(); });
  query.addEventListener('compositionend', update);
  topic.addEventListener('change', update);
  kind.addEventListener('change', update);
  form.addEventListener('reset', () => { window.setTimeout(() => { update(); query.focus(); }, 0); });
  window.addEventListener('hashchange', () => { readHash(); render(); });
  readHash();
  status.textContent = '正在读取公开检索索引…';
  const controller = new AbortController();
  const timeout = window.setTimeout(() => controller.abort(), 15000);
  fetch(form.dataset.indexUrl, { signal: controller.signal, credentials: 'omit' })
    .then(response => { if (!response.ok) throw new Error('Index unavailable'); return response.json(); })
    .then(data => {
      if (!Array.isArray(data.records) || !Array.isArray(data.topics)) throw new Error('Invalid index');
      topics = Object.fromEntries(data.topics.map(item => [item.id, item.title]));
      records = data.records.filter(row => typeof row.title === 'string' && names[row.kind] && safeUrl(row.url)).map(row => ({
        ...row, safeUrl: safeUrl(row.url), search: normalize([row.title, row.summary, row.text].join(' '))
      }));
      ready = true;
      form.hidden = false;
      render();
    })
    .catch(() => {
      form.hidden = true;
      results.hidden = true;
      status.textContent = '全文索引暂时无法载入。下方主题、项目和完整文章目录仍可使用。';
    })
    .finally(() => window.clearTimeout(timeout));
})();
