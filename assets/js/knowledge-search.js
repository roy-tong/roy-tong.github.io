(function () {
  'use strict';
  const root = document.querySelector('[data-library]');
  if (!root) return;
  const form = root.querySelector('[data-library-form]');
  const query = form.querySelector('[name="q"]');
  const sort = root.querySelector('[name="sort"]');
  const status = root.querySelector('[data-library-status]');
  const list = root.querySelector('[data-material-list]');
  const heading = root.querySelector('[data-list-heading]');
  const context = root.querySelector('[data-collection-context]');
  const empty = root.querySelector('[data-library-empty]');
  const more = root.querySelector('[data-library-more]');
  const exit = root.querySelector('[data-collection-exit]');
  const exitLink = root.querySelector('[data-collection-page-link]');
  const collectionLinks = Array.from(root.querySelectorAll('[data-collection]'));
  const typeButtons = Array.from(root.querySelectorAll('[data-type]'));
  const normalize = value => String(value || '').normalize('NFKC').toLocaleLowerCase().replace(/\s+/g, ' ').trim();
  const typeOrder = { report: 0, data: 1, note: 2, reference: 3 };
  const typeNames = Object.fromEntries(typeButtons.map(button => [button.dataset.type, button.childNodes[0].textContent.trim()]));
  const collections = new Map(collectionLinks.filter(link => link.dataset.collection).map(link => [
    link.dataset.collection, { title: link.querySelector('span').textContent, url: link.getAttribute('href'), coverage: '' }
  ]));
  const records = Array.from(list.querySelectorAll('[data-material]')).map((element, index) => ({
    element, id: element.dataset.id, kind: element.dataset.kind,
    collections: element.dataset.collections.split(/\s+/).filter(Boolean),
    updated: element.dataset.updated, index,
    title: normalize(element.querySelector('h3').textContent),
    summary: normalize(element.querySelector('.kb-material-copy > p').textContent),
    search: normalize(element.textContent)
  }));
  let fullTextReady = false;
  let indexFailed = false;
  let selectedCollection = '';
  let selectedType = '';
  let limit = 12;
  let lastMatches = [];

  function readState() {
    const params = new URLSearchParams(window.location.hash.slice(1));
    query.value = (params.get('q') || '').slice(0, 200);
    const requestedCollection = params.get('collection') || '';
    selectedCollection = collections.has(requestedCollection) ? requestedCollection : '';
    const requestedType = params.get('type') || (params.get('kind') === 'knowledge' ? 'note' : '');
    selectedType = Object.hasOwn(typeOrder, requestedType) ? requestedType : '';
    const requestedSort = params.get('sort') || 'type';
    sort.value = ['type', 'updated', 'title'].includes(requestedSort) ? requestedSort : 'type';
    limit = 12;
  }

  function saveState(push) {
    const params = new URLSearchParams();
    if (selectedCollection) params.set('collection', selectedCollection);
    if (selectedType) params.set('type', selectedType);
    if (query.value.trim()) params.set('q', query.value.trim());
    if (sort.value !== 'type') params.set('sort', sort.value);
    const hash = params.toString();
    const target = window.location.pathname + window.location.search + (hash ? '#' + hash : '');
    if (target !== window.location.pathname + window.location.search + window.location.hash) {
      // URL fragments are not sent with HTTP requests; queries stay on the device.
      window.history[push ? 'pushState' : 'replaceState'](null, '', target);
    }
  }

  function render() {
    const terms = normalize(query.value).split(' ').filter(Boolean);
    const scoped = records.filter(row =>
      (!selectedCollection || row.collections.includes(selectedCollection)) &&
      terms.every(term => row.search.includes(term))
    );
    const matches = scoped.filter(row => !selectedType || row.kind === selectedType);
    const score = row => terms.reduce((total, term) => total +
      (row.title.includes(term) ? 10 : 0) + (row.summary.includes(term) ? 3 : 0), 0);
    matches.sort((a, b) => {
      if (sort.value === 'updated') return b.updated.localeCompare(a.updated) || a.index - b.index;
      if (sort.value === 'title') return a.title.localeCompare(b.title, 'zh-CN') || a.index - b.index;
      return (terms.length ? score(b) - score(a) : 0) ||
        typeOrder[a.kind] - typeOrder[b.kind] || a.index - b.index;
    });
    lastMatches = matches;
    records.forEach(row => { row.element.hidden = true; });
    const fragment = document.createDocumentFragment();
    matches.forEach((row, index) => {
      row.element.hidden = index >= limit;
      fragment.append(row.element);
    });
    // Keep all pre-rendered rows; hiding and ordering never rewrites their links.
    records.filter(row => !matches.includes(row)).forEach(row => fragment.append(row.element));
    list.append(fragment);
    typeButtons.forEach(button => {
      const type = button.dataset.type;
      button.setAttribute('aria-pressed', String(type === selectedType));
      button.querySelector('span').textContent = scoped.filter(row => !type || row.kind === type).length;
    });
    collectionLinks.forEach(link => {
      if (link.dataset.collection === selectedCollection) link.setAttribute('aria-current', 'true');
      else link.removeAttribute('aria-current');
    });
    const collection = collections.get(selectedCollection);
    heading.textContent = collection ? collection.title : '全部资料';
    context.textContent = collection ? collection.coverage : '';
    context.hidden = !context.textContent;
    exit.hidden = !collection;
    if (collection) exitLink.setAttribute('href', collection.url);
    const active = terms.length || selectedCollection || selectedType;
    const visible = Math.min(matches.length, limit);
    let message = (active ? '找到 ' : '共 ') + matches.length + ' 份公开资料';
    if (selectedType) message += ' · ' + typeNames[selectedType];
    if (visible < matches.length) message += ' · 显示前 ' + visible + ' 份';
    message += fullTextReady ? ' · 已包含公开正文检索。' :
      (indexFailed ? ' · 正文索引暂不可用，仍可搜索标题与简介。' : ' · 标题与简介可搜索，正在载入公开正文。');
    status.textContent = message;
    empty.hidden = matches.length !== 0;
    more.hidden = matches.length <= limit;
    more.textContent = '显示更多资料（还有 ' + Math.max(0, matches.length - visible) + ' 份）';
  }

  function update(push) { limit = 12; saveState(push); render(); }
  function clearAll() {
    query.value = '';
    selectedCollection = '';
    selectedType = '';
    sort.value = 'type';
    update(true);
    query.focus();
  }
  form.addEventListener('submit', event => { event.preventDefault(); update(false); });
  form.addEventListener('reset', event => { event.preventDefault(); clearAll(); });
  query.addEventListener('input', event => { if (!event.isComposing) update(false); });
  query.addEventListener('compositionend', () => update(false));
  sort.addEventListener('change', () => update(true));
  typeButtons.forEach(button => button.addEventListener('click', () => {
    selectedType = button.dataset.type;
    update(true);
  }));
  collectionLinks.forEach(link => link.addEventListener('click', event => {
    if (event.button !== 0 || event.metaKey || event.ctrlKey || event.shiftKey || event.altKey) return;
    event.preventDefault();
    selectedCollection = link.dataset.collection;
    update(true);
  }));
  more.addEventListener('click', () => {
    const previousLimit = limit;
    limit += 12;
    render();
    const next = lastMatches[previousLimit];
    if (next) next.element.querySelector('h3 a').focus();
  });
  root.querySelector('[data-clear-filters]').addEventListener('click', clearAll);
  window.addEventListener('popstate', () => { readState(); render(); });
  window.addEventListener('hashchange', () => { readState(); render(); });

  readState();
  form.hidden = false;
  root.querySelector('[data-type-filters]').hidden = false;
  root.querySelector('[data-library-sort]').hidden = false;
  render();

  const controller = new AbortController();
  const timeout = window.setTimeout(() => controller.abort(), 10000);
  fetch(root.dataset.indexUrl, { signal: controller.signal, credentials: 'omit' })
    .then(response => { if (!response.ok) throw new Error('Index unavailable'); return response.json(); })
    .then(data => {
      if (!Array.isArray(data.records) || !Array.isArray(data.collections)) throw new Error('Invalid index');
      const indexed = new Map(data.records.map(row => [row.id, row]));
      if (indexed.size !== data.records.length || indexed.size !== records.length ||
          records.some(row => !indexed.has(row.id) || typeof indexed.get(row.id).text !== 'string')) {
        throw new Error('Index and page do not describe the same material set');
      }
      records.forEach(row => {
        const entry = indexed.get(row.id);
        row.search = normalize([row.title, row.summary, entry.text, entry.version, entry.access].join(' '));
      });
      data.collections.forEach(entry => {
        const collection = collections.get(entry.id);
        if (collection && typeof entry.coverage === 'string') collection.coverage = entry.coverage;
      });
      fullTextReady = true;
      render();
    })
    .catch(() => { indexFailed = true; render(); })
    .finally(() => window.clearTimeout(timeout));
})();
