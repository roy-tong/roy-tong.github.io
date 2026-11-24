(function () {
  const root = document.documentElement;
  const themeToggle = document.querySelector('.theme-toggle');
  const themeColor = document.querySelector('meta[name="theme-color"]');
  const menuToggle = document.querySelector('.menu-toggle');
  const navigation = document.querySelector('.nav');
  const languageToggle = document.querySelector('[data-language-switch]');
  const preferredDark = window.matchMedia('(prefers-color-scheme: dark)').matches;
  const isEnglish = root.lang.toLowerCase().startsWith('en');
  const labels = isEnglish ? {
    darkMode: 'Switch to dark mode',
    lightMode: 'Switch to light mode',
    openNavigation: 'Open navigation',
    closeNavigation: 'Close navigation',
    copied: 'Copied'
  } : {
    darkMode: '切换至深色模式',
    lightMode: '切换至浅色模式',
    openNavigation: '打开导航',
    closeNavigation: '关闭导航',
    copied: '已复制'
  };

  function readPreference(key) {
    try {
      return localStorage.getItem(key);
    } catch (error) {
      return null;
    }
  }

  function savePreference(key, value) {
    try {
      localStorage.setItem(key, value);
    } catch (error) {
      /* Controls remain functional when storage is unavailable. */
    }
  }

  const saved = readPreference('theme');

  function applyTheme(theme) {
    root.dataset.theme = theme;
    const isDark = theme === 'dark';

    if (themeToggle) {
      const label = isDark ? labels.lightMode : labels.darkMode;
      themeToggle.setAttribute('aria-pressed', String(isDark));
      themeToggle.setAttribute('aria-label', label);
      themeToggle.setAttribute('title', label);
    }

    if (themeColor) {
      themeColor.setAttribute('content', isDark ? '#121513' : '#f4f5f2');
    }
  }

  applyTheme(saved === 'dark' || (!saved && preferredDark) ? 'dark' : 'light');

  if (themeToggle) {
    themeToggle.addEventListener('click', function () {
      const isDark = root.dataset.theme === 'dark';
      const nextTheme = isDark ? 'light' : 'dark';
      applyTheme(nextTheme);
      savePreference('theme', nextTheme);
    });
  }

  if (languageToggle) {
    languageToggle.addEventListener('click', function () {
      savePreference('site-language', languageToggle.dataset.targetLanguage || 'zh-CN');
    });
  }

  function closeNavigation() {
    if (!menuToggle || !navigation) return;
    navigation.classList.remove('is-open');
    menuToggle.setAttribute('aria-expanded', 'false');
    menuToggle.setAttribute('aria-label', labels.openNavigation);
    document.body.classList.remove('nav-open');
  }

  if (menuToggle && navigation) {
    menuToggle.addEventListener('click', function () {
      const shouldOpen = menuToggle.getAttribute('aria-expanded') !== 'true';
      navigation.classList.toggle('is-open', shouldOpen);
      menuToggle.setAttribute('aria-expanded', String(shouldOpen));
      menuToggle.setAttribute('aria-label', shouldOpen ? labels.closeNavigation : labels.openNavigation);
      document.body.classList.toggle('nav-open', shouldOpen);
    });

    navigation.querySelectorAll('a').forEach(function (link) {
      link.addEventListener('click', closeNavigation);
    });

    document.addEventListener('keydown', function (event) {
      if (event.key === 'Escape' && menuToggle.getAttribute('aria-expanded') === 'true') {
        closeNavigation();
        menuToggle.focus();
      }
    });

    window.matchMedia('(min-width: 681px)').addEventListener('change', function (event) {
      if (event.matches) closeNavigation();
    });
  }

  document.querySelectorAll('[data-archive]').forEach(function (archive) {
    const input = archive.querySelector('[data-archive-search]');
    const count = archive.querySelector('[data-archive-count]');
    const empty = archive.querySelector('[data-archive-empty]');
    const items = Array.from(archive.querySelectorAll('[data-archive-item]'));
    const years = Array.from(archive.querySelectorAll('.archive-year'));
    if (!input || !items.length) return;

    const totalLabel = count ? count.textContent : '';
    let announceTimer;

    function filterArchive() {
      const query = input.value.trim().toLocaleLowerCase();
      let visibleCount = 0;

      items.forEach(function (item) {
        const matches = !query || (item.dataset.search || '').toLocaleLowerCase().includes(query);
        item.hidden = !matches;
        if (matches) visibleCount += 1;
      });

      years.forEach(function (year) {
        const visibleItems = year.querySelectorAll('[data-archive-item]:not([hidden])');
        year.hidden = visibleItems.length === 0;
      });

      if (empty) empty.hidden = visibleCount !== 0;
      if (!count) return;

      window.clearTimeout(announceTimer);
      announceTimer = window.setTimeout(function () {
        count.textContent = query
          ? (isEnglish ? visibleCount + ' of ' + items.length + ' essays' : '找到 ' + visibleCount + ' 篇，共 ' + items.length + ' 篇')
          : totalLabel;
      }, 200);
    }

    input.addEventListener('input', filterArchive);
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

      button.textContent = labels.copied;
      window.setTimeout(function () {
        button.textContent = originalText;
      }, 1600);
    });
  });
})();
