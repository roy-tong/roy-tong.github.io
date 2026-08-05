(function () {
  const root = document.documentElement;
  const themeToggle = document.querySelector('.theme-toggle');
  const themeColor = document.querySelector('meta[name="theme-color"]');
  const menuToggle = document.querySelector('.menu-toggle');
  const navigation = document.querySelector('.nav');
  const saved = localStorage.getItem('theme');
  const preferredDark = window.matchMedia('(prefers-color-scheme: dark)').matches;

  function applyTheme(theme) {
    root.dataset.theme = theme;
    const isDark = theme === 'dark';

    if (themeToggle) {
      const label = isDark ? '切换至浅色模式' : '切换至深色模式';
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
      localStorage.setItem('theme', nextTheme);
    });
  }

  function closeNavigation() {
    if (!menuToggle || !navigation) return;
    navigation.classList.remove('is-open');
    menuToggle.setAttribute('aria-expanded', 'false');
    menuToggle.setAttribute('aria-label', '打开导航');
    document.body.classList.remove('nav-open');
  }

  if (menuToggle && navigation) {
    menuToggle.addEventListener('click', function () {
      const shouldOpen = menuToggle.getAttribute('aria-expanded') !== 'true';
      navigation.classList.toggle('is-open', shouldOpen);
      menuToggle.setAttribute('aria-expanded', String(shouldOpen));
      menuToggle.setAttribute('aria-label', shouldOpen ? '关闭导航' : '打开导航');
      document.body.classList.toggle('nav-open', shouldOpen);
    });

    navigation.querySelectorAll('a').forEach(function (link) {
      link.addEventListener('click', closeNavigation);
    });

    document.addEventListener('keydown', function (event) {
      if (event.key === 'Escape') closeNavigation();
    });

    window.matchMedia('(min-width: 681px)').addEventListener('change', function (event) {
      if (event.matches) closeNavigation();
    });
  }

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
