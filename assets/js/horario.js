// Recursos que dependem do horário de Rondônia (America/Porto_Velho):
// o aviso "aberto/fechado" do rodapé e o tema claro/escuro do mapa.
(() => {
  if (typeof Intl === 'undefined') return;

  const ABRE = 8;
  const FECHA = 18;
  const AMANHECER = 6;
  const ANOITECER = 18;
  const DIAS = ['Sun', 'Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat'];
  const NOMES = ['domingo', 'segunda', 'terça', 'quarta', 'quinta', 'sexta', 'sábado'];

  const status = document.querySelector('[data-open-status]');
  const mapas = document.querySelectorAll('[data-mapa]');

  function agora() {
    const partes = new Intl.DateTimeFormat('en-US', {
      timeZone: 'America/Porto_Velho',
      weekday: 'short',
      hour: 'numeric',
      minute: 'numeric',
      hourCycle: 'h23',
    }).formatToParts(new Date());
    const valor = (tipo) => partes.find((parte) => parte.type === tipo).value;
    return {
      dia: DIAS.indexOf(valor('weekday')),
      hora: Number(valor('hour')) + Number(valor('minute')) / 60,
    };
  }

  const diaUtil = (dia) => dia >= 1 && dia <= 5;

  function textoDoStatus({ dia, hora }) {
    if (diaUtil(dia) && hora >= ABRE && hora < FECHA) return 'Aberto agora · até as 18h';
    if (diaUtil(dia) && hora < ABRE) return 'Fechado agora · abre hoje às 8h';

    let proximo = (dia + 1) % 7;
    while (!diaUtil(proximo)) proximo = (proximo + 1) % 7;
    const quando = proximo === (dia + 1) % 7 ? 'amanhã' : NOMES[proximo];
    return `Fechado agora · abre ${quando} às 8h`;
  }

  function atualizar() {
    const momento = agora();

    if (status) {
      status.textContent = textoDoStatus(momento);
      status.classList.toggle('is-open', status.textContent.startsWith('Aberto'));
      status.hidden = false;
    }

    const noite = momento.hora < AMANHECER || momento.hora >= ANOITECER;
    mapas.forEach((mapa) => mapa.classList.toggle('mapa-noite', noite));
  }

  atualizar();
  window.setInterval(atualizar, 60000);
})();
