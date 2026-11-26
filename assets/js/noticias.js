// Carrossel de artigos no celular e no tablet: destaca o card que está no centro.
// No computador os cards ficam em grade e o destaque é feito pelo CSS (:hover).
(() => {
  const carrosseis = document.querySelectorAll('.post-grid-carrossel');

  carrosseis.forEach((carrossel) => {
    const cards = Array.from(carrossel.querySelectorAll('.post-card'));
    let agendado = false;

    function destacarCentral() {
      agendado = false;
      const limites = carrossel.getBoundingClientRect();
      const centro = limites.left + limites.width / 2;
      let maisProximo;
      let menorDistancia = Infinity;

      cards.forEach((card) => {
        const caixa = card.getBoundingClientRect();
        const distancia = Math.abs(caixa.left + caixa.width / 2 - centro);
        if (distancia < menorDistancia) {
          menorDistancia = distancia;
          maisProximo = card;
        }
      });

      cards.forEach((card) => card.classList.toggle('em-foco', card === maisProximo));
    }

    function agendar() {
      if (agendado) return;
      agendado = true;
      window.requestAnimationFrame(destacarCentral);
    }

    carrossel.addEventListener('scroll', agendar, { passive: true });
    window.addEventListener('resize', agendar);
    destacarCentral();
  });
})();
