// Central de dúvidas em vídeo.
// Computador: lista à esquerda e vídeo à direita. Celular: o vídeo abre dentro da pergunta.
(() => {
  const section = document.querySelector('.qa-section');
  if (!section) return;

  const items = Array.from(section.querySelectorAll('details.qa'));
  const topics = section.querySelector('.qa-topics');
  const stage = section.querySelector('.qa-stage');
  const player = stage.querySelector('.qa-player');
  const copy = stage.querySelector('.qa-stage-copy');
  const video = player.querySelector('video');
  const wide = window.matchMedia('(min-width: 900px)');
  let current;

  section.classList.add('qa-js');
  topics.hidden = false;

  function fillStage(item) {
    const title = document.createElement('h3');
    title.textContent = item.querySelector('.qa-q').textContent;
    const body = item.querySelector('.qa-body').cloneNode(true);
    body.querySelectorAll('[id]').forEach(el => el.removeAttribute('id'));
    copy.replaceChildren(title, ...body.childNodes);
  }

  function layout() {
    if (!current) return;
    if (wide.matches) {
      stage.hidden = false;
      stage.prepend(player);
      fillStage(current);
      items.forEach(item => { item.open = false; });
    } else {
      stage.hidden = true;
      items.forEach(item => { item.open = item === current; });
      current.querySelector('.qa-body').prepend(player);
    }
  }

  function select(item, play) {
    const changed = item !== current;
    current = item;
    items.forEach(other => {
      other.classList.toggle('is-active', other === item);
      other.querySelector('summary').setAttribute('aria-current', String(other === item));
    });
    if (changed) {
      video.pause();
      video.poster = item.dataset.poster;
      video.src = item.dataset.video;
    }
    layout();
    if (play) video.play().catch(() => {});
  }

  function collapse() {
    video.pause();
    current.open = false;
    current.classList.remove('is-active');
    current = undefined;
  }

  items.forEach(item => {
    item.querySelector(':scope > summary').addEventListener('click', event => {
      event.preventDefault();
      if (!wide.matches && item === current && item.open) {
        collapse();
        return;
      }
      select(item, true);
      if (!wide.matches) {
        item.scrollIntoView({ block: 'start', behavior: window.matchMedia('(prefers-reduced-motion: reduce)').matches ? 'auto' : 'smooth' });
      }
    });
  });

  topics.addEventListener('click', event => {
    const button = event.target.closest('[data-topic]');
    if (!button) return;
    const topic = button.dataset.topic;
    topics.querySelectorAll('[data-topic]').forEach(b => b.setAttribute('aria-pressed', String(b === button)));
    items.forEach(item => { item.hidden = topic !== 'todos' && item.dataset.topic !== topic; });
    if (current && current.hidden) {
      const first = items.find(item => !item.hidden);
      if (wide.matches) select(first, false);
      else collapse();
    }
  });

  const onChange = () => {
    if (wide.matches && !current) select(items.find(item => !item.hidden), false);
    else layout();
  };
  if (typeof wide.addEventListener === 'function') wide.addEventListener('change', onChange);
  else wide.addListener(onChange);

  // Abre direto a pergunta indicada no endereço (ex.: #bpc)
  const fromHash = items.find(item => `#${item.id}` === window.location.hash);
  if (fromHash) select(fromHash, false);
  else if (wide.matches) select(items[0], false);
})();
