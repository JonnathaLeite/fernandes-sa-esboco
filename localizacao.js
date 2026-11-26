const mapToggle = document.querySelector('[data-map-toggle]');
const mapPanel = document.getElementById(mapToggle.getAttribute('aria-controls'));

mapToggle.hidden = false;
mapToggle.addEventListener('click', () => {
  const opening = mapPanel.hidden;

  if (opening && !mapPanel.firstElementChild) {
    const map = document.createElement('iframe');
    map.title = 'Mapa da Fernandes & Sá Advocacia em Ji-Paraná';
    map.referrerPolicy = 'no-referrer';
    map.src = mapPanel.dataset.mapSrc;
    mapPanel.append(map);
  }

  mapPanel.hidden = !opening;
  mapToggle.setAttribute('aria-expanded', String(opening));
  mapToggle.textContent = opening ? 'Ocultar mapa' : 'Mostrar mapa';
});
