(function () {
  const root = document.documentElement;
  const toggle = document.querySelector('.theme-toggle');
  const saved = localStorage.getItem('theme');
  const preferredDark = window.matchMedia('(prefers-color-scheme: dark)').matches;

  if (saved === 'dark' || (!saved && preferredDark)) {
    root.dataset.theme = 'dark';
  }

  if (toggle) {
    toggle.addEventListener('click', function () {
      const isDark = root.dataset.theme === 'dark';
      root.dataset.theme = isDark ? 'light' : 'dark';
      localStorage.setItem('theme', isDark ? 'light' : 'dark');
    });
  }

  const params = new URLSearchParams(window.location.search);
  const explicitSource = params.get('from') || params.get('utm_source');
  const campaign = params.get('utm_campaign');
  let source = explicitSource ? [explicitSource, campaign].filter(Boolean).join('-') : '';

  if (!source && document.referrer) {
    try {
      const referrerHost = new URL(document.referrer).hostname;
      if (referrerHost.includes('xiaohongshu') || referrerHost.includes('xhslink')) {
        source = 'xhs';
      } else if (referrerHost.includes('weixin') || referrerHost.includes('wechat')) {
        source = 'wechat';
      }
    } catch (error) {
      source = '';
    }
  }

  if (source) {
    localStorage.setItem('book_source', source);
  } else {
    source = localStorage.getItem('book_source') || 'website';
  }

  const cleanSource = source
    .toLowerCase()
    .replace(/[^a-z0-9\u4e00-\u9fff_-]+/g, '-')
    .replace(/^-+|-+$/g, '')
    .slice(0, 24) || 'website';

  document.querySelectorAll('[data-carry-source]').forEach(function (link) {
    try {
      const target = new URL(link.getAttribute('href'), window.location.href);
      if (!target.searchParams.has('from')) {
        target.searchParams.set('from', cleanSource);
      }
      link.setAttribute('href', target.toString());
    } catch (error) {
      // Keep the original link when URL parsing is unavailable.
    }
  });

  const sourceLabel = cleanSource === 'website' ? '官网' : cleanSource;
  const remark = '购书-' + sourceLabel;

  document.querySelectorAll('[data-wechat-remark]').forEach(function (element) {
    element.textContent = remark;
  });

  document.querySelectorAll('[data-copy-text]').forEach(function (button) {
    button.addEventListener('click', async function () {
      const selector = button.getAttribute('data-copy-text');
      const target = selector ? document.querySelector(selector) : null;
      if (!target) return;

      const text = target.textContent.trim();
      const originalText = button.textContent;

      try {
        await navigator.clipboard.writeText(text);
      } catch (error) {
        const textarea = document.createElement('textarea');
        textarea.value = text;
        textarea.setAttribute('readonly', '');
        textarea.style.position = 'fixed';
        textarea.style.opacity = '0';
        document.body.appendChild(textarea);
        textarea.select();
        document.execCommand('copy');
        document.body.removeChild(textarea);
      }

      button.textContent = '已复制';
      window.setTimeout(function () {
        button.textContent = originalText;
      }, 1600);
    });
  });
})();