document.addEventListener('keydown', (e) => {
  if (e.target.tagName === 'INPUT' || e.target.tagName === 'TEXTAREA') return;
  if (e.key === 'j') window.scrollBy(0, 100);
  if (e.key === 'k') window.scrollBy(0, -100);
});
