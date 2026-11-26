const library = document.querySelector('.video-section');
const topics = library.querySelector('.video-topics');
const episodes = Array.from(library.querySelectorAll('[data-episode]'));
const player = library.querySelector('.video-dialog');
const video = player.querySelector('video');
const transcript = player.querySelector('.video-dialog-transcript');

topics.addEventListener('click', event => {
  const button = event.target.closest('[data-topic]');
  if (!button) return;
  const topic = button.dataset.topic;
  topics.querySelectorAll('[data-topic]').forEach(tab => {
    tab.setAttribute('aria-pressed', String(tab === button));
  });
  episodes.forEach(episode => {
    episode.hidden = topic !== 'todos' && episode.dataset.episode !== topic;
  });
});
topics.hidden = false;

if (typeof player.showModal === 'function') {
  let opener;

  function playEpisode(episode, trigger) {
    const cover = episode.querySelector('.video-cover');
    opener = trigger;
    player.querySelector('h3').textContent = episode.querySelector('h3').textContent;
    transcript.open = false;
    transcript.lastElementChild.replaceChildren(episode.querySelector('.video-transcript ol').cloneNode(true));
    video.poster = cover.querySelector('img').src;
    video.src = cover.href;
    player.showModal();
    video.play().catch(() => {
      // The native Play control remains available when autoplay is blocked.
    });
  }

  episodes.forEach(episode => {
    const cover = episode.querySelector('.video-cover');
    cover.addEventListener('click', event => {
      if (event.metaKey || event.ctrlKey || event.shiftKey || event.altKey) return;
      event.preventDefault();
      playEpisode(episode, cover);
    });
  });

  player.addEventListener('close', () => {
    video.pause();
    video.removeAttribute('src');
    video.load();
    opener?.focus();
  });

}
