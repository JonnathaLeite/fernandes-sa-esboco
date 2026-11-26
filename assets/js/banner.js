const banner = document.querySelector('.banner');
const slides = Array.from(banner.querySelectorAll('[data-slide]'));
const controls = banner.querySelector('.banner-controls');
const toggle = banner.querySelector('[data-toggle]');
const dots = Array.from(controls.querySelectorAll('[data-dot]'));
const panel = banner.querySelector('#banner-painel');
const announcement = banner.querySelector('[data-announcement]');
const motionPreference = window.matchMedia('(prefers-reduced-motion: reduce)');

let selected = 0;
let playing = !motionPreference.matches;
let timer;
let swipeStart;

function showSlide(index, announce = false) {
  selected = (index + slides.length) % slides.length;
  slides.forEach((slide, slideIndex) => {
    slide.hidden = slideIndex !== selected;
  });
  banner.dataset.active = selected;
  dots.forEach((dot, dotIndex) => {
    if (dotIndex === selected) dot.setAttribute('aria-current', 'true');
    else dot.removeAttribute('aria-current');
  });
  if (announce) {
    const heading = slides[selected].querySelector('h1, h2');
    announcement.textContent = `Destaque ${selected + 1} de ${slides.length}. ${heading.innerText}`;
  }
}

function refreshRotation() {
  window.clearInterval(timer);
  toggle.textContent = playing ? 'Pausar' : 'Reproduzir';
  const interacting = banner.matches(':hover') || slides[selected].contains(document.activeElement);
  if (playing && !interacting && !document.hidden) {
    timer = window.setInterval(() => showSlide(selected + 1), 8500);
  }
}

function navigate(index) {
  playing = false;
  showSlide(index, true);
  refreshRotation();
}

dots.forEach((dot, index) => {
  dot.addEventListener('click', () => navigate(index));
});
panel.addEventListener(
  'touchstart',
  (event) => {
    swipeStart = event.touches.length === 1 ? event.touches[0] : undefined;
  },
  { passive: true },
);
panel.addEventListener(
  'touchend',
  (event) => {
    if (!swipeStart) return;
    const touch = event.changedTouches[0];
    const x = touch.clientX - swipeStart.clientX;
    const y = touch.clientY - swipeStart.clientY;
    swipeStart = undefined;
    if (Math.abs(x) >= 50 && Math.abs(x) > Math.abs(y) * 1.4) {
      navigate(selected + (x < 0 ? 1 : -1));
    }
  },
  { passive: true },
);
panel.addEventListener('touchcancel', () => {
  swipeStart = undefined;
});
toggle.addEventListener('click', () => {
  playing = !playing;
  refreshRotation();
});
banner.addEventListener('mouseenter', refreshRotation);
banner.addEventListener('mouseleave', refreshRotation);
banner.addEventListener('focusin', refreshRotation);
banner.addEventListener('focusout', () => window.setTimeout(refreshRotation, 0));
document.addEventListener('visibilitychange', refreshRotation);
function updateMotionPreference(event) {
  if (event.matches) playing = false;
  refreshRotation();
}

if (typeof motionPreference.addEventListener === 'function') {
  motionPreference.addEventListener('change', updateMotionPreference);
} else {
  motionPreference.addListener(updateMotionPreference);
}

showSlide(0);
controls.hidden = false;
refreshRotation();
