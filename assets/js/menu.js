// Menu do celular: recolhe a navegação atrás do botão "Menu".
(() => {
  const topo = document.querySelector('.topo');
  if (!topo) return;

  const botao = topo.querySelector('.menu-botao');
  const menu = topo.querySelector('.menu');

  topo.classList.add('menu-recolhivel');

  function alternar(abrir) {
    botao.setAttribute('aria-expanded', String(abrir));
    topo.classList.toggle('menu-aberto', abrir);
  }

  botao.addEventListener('click', () => {
    alternar(botao.getAttribute('aria-expanded') !== 'true');
  });

  // Fecha ao escolher um item, ao apertar Esc ou ao clicar fora do menu.
  menu.addEventListener('click', (event) => {
    if (event.target.closest('a')) alternar(false);
  });

  document.addEventListener('keydown', (event) => {
    if (event.key === 'Escape' && topo.classList.contains('menu-aberto')) {
      alternar(false);
      botao.focus();
    }
  });

  document.addEventListener('click', (event) => {
    if (!topo.contains(event.target)) alternar(false);
  });
})();
