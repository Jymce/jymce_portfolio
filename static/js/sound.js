// Mechanical-keyboard sound effects: soft "thock" on hover, deeper press on click.
// Uses Web Audio API so rapid repeated triggers stay snappy.
const SoundFX = (() => {
    let ctx = null;
    const buffers = {};
    let enabled = localStorage.sound !== 'off';
    let lastHover = 0;
    const HOVER_GAP_MS = 80;

    const FILES = {
        hover: ['/static/sounds/hover.wav'],
        click: [
            '/static/sounds/click1.wav',
            '/static/sounds/click2.wav',
            '/static/sounds/click3.wav',
        ],
    };

    async function init() {
        if (ctx) return;
        ctx = new (window.AudioContext || window.webkitAudioContext)();
        await Promise.all(Object.entries(FILES).map(async ([name, urls]) => {
            buffers[name] = await Promise.all(urls.map(async (url) => {
                const res = await fetch(url);
                return ctx.decodeAudioData(await res.arrayBuffer());
            }));
        }));
    }

    function play(name, volume) {
        if (!enabled || !ctx || !buffers[name]) return;
        if (ctx.state === 'suspended') ctx.resume();
        const list = buffers[name];
        const src = ctx.createBufferSource();
        src.buffer = list[Math.floor(Math.random() * list.length)];
        const gain = ctx.createGain();
        gain.gain.value = volume;
        src.connect(gain).connect(ctx.destination);
        src.start();
    }

    // Press sound — fires on pointerdown (the "downstroke"), feels like a real switch
    document.addEventListener('pointerdown', async (e) => {
        await init();  // AudioContext can only start after a user gesture
        if (e.target.closest('a, button')) play('click', 0.35);
    });

    // Hover sound — throttled, and only fires when entering a different control
    document.addEventListener('pointerover', (e) => {
        if (!ctx) return;
        const el = e.target.closest('a, button');
        if (!el) return;
        const prev = e.relatedTarget && e.relatedTarget.closest
            ? e.relatedTarget.closest('a, button') : null;
        if (el === prev) return;
        const now = performance.now();
        if (now - lastHover < HOVER_GAP_MS) return;
        lastHover = now;
        play('hover', 0.12);
    });

    return {
        get enabled() { return enabled; },
        toggle() {
            enabled = !enabled;
            localStorage.sound = enabled ? 'on' : 'off';
            return enabled;
        },
    };
})();

function syncSoundIcons() {
    document.querySelectorAll('[data-icon-sound-on]').forEach(el => el.classList.toggle('hidden', !SoundFX.enabled));
    document.querySelectorAll('[data-icon-sound-off]').forEach(el => el.classList.toggle('hidden', SoundFX.enabled));
}

function toggleSound() {
    SoundFX.toggle();
    syncSoundIcons();
}

document.addEventListener('DOMContentLoaded', syncSoundIcons);
