document.addEventListener('keydown', (e) => {
  if (e.target.tagName === 'INPUT' || e.target.tagName === 'TEXTAREA') return;
  const behavior = e.repeat ? 'instant' : 'smooth';
  if (e.key === 'j') window.scrollBy({ top: 100, behavior });
  if (e.key === 'k') window.scrollBy({ top: -100, behavior });
  if (e.key === 'Escape') {
    e.preventDefault();
    window.location.href = '/articles/';
  }
});
