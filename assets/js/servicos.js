// Vídeo explicativo dentro do card do serviço, sem sair da página.
// Sem JavaScript, o botão leva à pergunta correspondente em duvidas.html.
(() => {
  const botoes = document.querySelectorAll('[data-video-inline]');

  botoes.forEach((botao) => {
    botao.addEventListener('click', (event) => {
      if (event.metaKey || event.ctrlKey || event.shiftKey) return;
      event.preventDefault();

      const bloco = botao.closest('.servico-card, .servico');
      const area = bloco.querySelector('.servico-video');

      if (!area.firstElementChild) {
        const video = document.createElement('video');
        video.controls = true;
        video.playsInline = true;
        video.poster = botao.dataset.poster;
        video.src = botao.dataset.videoInline;
        area.append(video);
      }

      area.hidden = false;
      botao.hidden = true;
      area.firstElementChild.play().catch(() => {});
    });
  });

  // Pausa o vídeo quando o card é fechado.
  document.querySelectorAll('.servico-card').forEach((card) => {
    card.addEventListener('toggle', () => {
      if (!card.open) card.querySelector('.servico-video video')?.pause();
    });
  });
})();
