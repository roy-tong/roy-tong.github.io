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
})();

