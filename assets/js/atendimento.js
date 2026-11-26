// Mostra no rodapé se o escritório está aberto agora (horário de Rondônia).
(() => {
  const el = document.querySelector('[data-open-status]');
  if (!el || typeof Intl === 'undefined') return;

  const ABRE = 8;
  const FECHA = 18;
  const DIAS = ['Sun', 'Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat'];
  const NOMES = ['domingo', 'segunda', 'terça', 'quarta', 'quinta', 'sexta', 'sábado'];

  function agora() {
    const parts = new Intl.DateTimeFormat('en-US', {
      timeZone: 'America/Porto_Velho',
      weekday: 'short',
      hour: 'numeric',
      minute: 'numeric',
      hourCycle: 'h23',
    }).formatToParts(new Date());
    const get = (type) => parts.find((p) => p.type === type).value;
    return {
      dia: DIAS.indexOf(get('weekday')),
      hora: Number(get('hour')) + Number(get('minute')) / 60,
    };
  }

  const util = (dia) => dia >= 1 && dia <= 5;

  function atualizar() {
    const { dia, hora } = agora();
    let texto;
    let aberto = false;
    if (util(dia) && hora >= ABRE && hora < FECHA) {
      aberto = true;
      texto = 'Aberto agora · até as 18h';
    } else if (util(dia) && hora < ABRE) {
      texto = 'Fechado agora · abre hoje às 8h';
    } else {
      let proximo = (dia + 1) % 7;
      while (!util(proximo)) proximo = (proximo + 1) % 7;
      const quando = proximo === (dia + 1) % 7 ? 'amanhã' : NOMES[proximo];
      texto = `Fechado agora · abre ${quando} às 8h`;
    }
    el.textContent = texto;
    el.classList.toggle('is-open', aberto);
    el.hidden = false;
  }

  atualizar();
  window.setInterval(atualizar, 60000);
})();
