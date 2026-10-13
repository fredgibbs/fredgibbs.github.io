// deck-check.mjs <url> — the typography and image pass for a built lecture deck.
//
// Run through scripts/deck-check.sh, which builds nothing: it serves _site,
// starts headless Chrome, and calls this. The rules being checked live in
// courses/SLIDE-STYLE.md ("Slide levels", "Every piece of text carries a
// class", "Before publishing: the typography pass"); this is the measurement.
//
// Steps through every slide at the deck's own 960x700 size, with every
// fragment shown, and reports:
//   FAIL overflow     content taller than the 644px the slide can show
//   FAIL unstyled     a paragraph with no class and no styling container
//   FAIL order        commentary, or a second quotation, above the slide's .quote
//   FAIL quote-as-commentary  a .reveal-block or .detail that opens with a quotation
//   FAIL before-intro someone's words, or their name in a headline, before
//                     the portrait slide that introduces them
//   FAIL image <1.0x  an image displayed larger than its own pixels
//   WARN image <1.5x  sharp at 960x700, soft on a 1080p projector
// Exits 1 if anything FAILs.
const [url] = process.argv.slice(2);
const PORT = Number(process.env.CDP_PORT || 9223);
const t = await (await fetch(`http://127.0.0.1:${PORT}/json/new?about:blank`, { method: 'PUT' })).json();
const ws = new WebSocket(t.webSocketDebuggerUrl);
let id = 0; const pend = new Map(), waits = new Map();
ws.onmessage = e => { const m = JSON.parse(e.data);
  if (m.id && pend.has(m.id)) { pend.get(m.id)(m.result); pend.delete(m.id); }
  if (m.method && waits.has(m.method)) { waits.get(m.method)(); waits.delete(m.method); } };
const send = (method, params = {}) => new Promise(r => { pend.set(++id, r); ws.send(JSON.stringify({ id, method, params })); });
const on = method => new Promise(r => waits.set(method, r));
const sleep = ms => new Promise(r => setTimeout(r, ms));
const ev = async expr => (await send('Runtime.evaluate', { expression: expr, returnByValue: true, awaitPromise: true })).result.value;

await new Promise(r => ws.onopen = r);
await send('Page.enable'); await send('Runtime.enable');
await send('Emulation.setDeviceMetricsOverride', { width: 960, height: 700, deviceScaleFactor: 1, mobile: false });
const loaded = on('Page.loadEventFired');
await send('Page.navigate', { url }); await Promise.race([loaded, sleep(20000)]); await sleep(2500);

// Static checks: run once over the whole deck.
const statics = await ev(`(() => {
  const out = [];
  const slides = Reveal.getSlides();
  const STYLED = ['quote','pull-quote','reveal-block','takehome','card','answer','track','step',
    'question','cite','citation-note','eyebrow','main-point','detail','credit','bleed-alt','body','provocation','notes'];
  const styledAncestor = el => { for (let a = el.parentElement; a && a.tagName !== 'SECTION'; a = a.parentElement) {
      if (['FIGURE','FIGCAPTION','LI','UL','OL','BLOCKQUOTE','TABLE'].includes(a.tagName)) return true;
      if ([...a.classList].some(c => STYLED.includes(c))) return true; } return false; };
  const level = el => { const c = el.classList;
    if (c.contains('eyebrow')) return 1; if (c.contains('main-point')) return 2;
    if (c.contains('quote')) return 3; if (c.contains('pull-quote')) return 3.5;
    if (c.contains('reveal-block') && !c.contains('compare')) return 4; if (c.contains('detail')) return 4;
    return null; };
  // the narrator: the "Background:" reading on the title slide
  const bg = [...document.querySelectorAll('ul.source-list li')].map(li => li.textContent).find(t => /^\\s*Background:/.test(t)) || '';
  const narrator = (bg.replace(/^\\s*Background:\\s*/, '').split(',')[0].trim().split(/\\s+/).pop() || '');
  // portraits: surname -> slide index
  const intro = {};
  slides.forEach((s, i) => s.querySelectorAll('figure.portrait figcaption').forEach(fc => {
    const name = (fc.childNodes[0]?.textContent || '').split('·')[0].trim();
    const sur = name.split(/\\s+/).pop(); if (sur && !(sur in intro)) intro[sur] = i; }));
  slides.forEach((s, i) => {
    const n = i + 1;
    s.querySelectorAll('p').forEach(p => {
      const txt = p.textContent.trim();
      if (txt && !p.className && !styledAncestor(p)) out.push(['FAIL', n, 'unstyled', txt.slice(0, 70)]); });
    const els = [...s.querySelectorAll('.eyebrow,.main-point,.quote,.pull-quote,.reveal-block,.detail')].filter(e => level(e) !== null);
    const q = els.findIndex(e => e.classList.contains('quote'));
    if (q >= 0) els.slice(0, q).forEach(e => { if (level(e) > 3) out.push(['FAIL', n, 'order',
      (e.classList.contains('pull-quote') ? 'a second quotation' : 'commentary') + ' above the slide\\'s quotation: ' + e.textContent.trim().slice(0, 50)]); });
    s.querySelectorAll('.reveal-block:not(.compare) p, p.detail').forEach(p => {
      if (/^[\\u201C"]/.test(p.textContent.trim())) out.push(['FAIL', n, 'quote-as-commentary', p.textContent.trim().slice(0, 60)]); });
    for (const [sur, at] of Object.entries(intro)) {
      if (sur === narrator || i >= at) continue;
      const cites = [...s.querySelectorAll('.quote .cite, .pull-quote .cite')].map(c => c.textContent.trim());
      const head = s.querySelector('.main-point')?.textContent || '';
      if (cites.some(c => c.startsWith(sur)) || new RegExp('\\\\b' + sur + '\\\\b').test(head))
        out.push(['FAIL', n, 'before-intro', sur + ' is quoted or named in a headline before the portrait on slide ' + (at + 1)]); }
  });
  return { out, total: slides.length, narrator };
})()`);

// Per-slide checks: need the slide on screen to measure layout.
const findings = statics.out;
for (let i = 0; i < statics.total; i++) {
  await ev(`Reveal.slide(${i}, 0, 99)`); await sleep(500);
  const r = await ev(`(() => { const s = Reveal.getCurrentSlide(); const res = [];
    if (!s.classList.contains('image-slide') && s.scrollHeight > 644) res.push(['FAIL', 'overflow', s.scrollHeight + 'px tall']);
    s.querySelectorAll('img').forEach(img => { if (!img.offsetHeight) return;
      const ratio = Math.min(img.naturalWidth / img.offsetWidth, img.naturalHeight / img.offsetHeight);
      const name = img.getAttribute('src').split('/').pop();
      if (ratio < 0.98) res.push(['FAIL', 'image <1.0x', name + ' ' + img.naturalWidth + 'x' + img.naturalHeight + ' shown at ' + img.offsetWidth + 'x' + img.offsetHeight]);
      else if (ratio < 1.5) res.push(['WARN', 'image <1.5x', name + ' ' + img.naturalWidth + 'x' + img.naturalHeight + ' shown at ' + img.offsetWidth + 'x' + img.offsetHeight + ' (' + ratio.toFixed(2) + 'x)']); });
    s.querySelectorAll('[data-background-image]').forEach(() => {});
    return res; })()`);
  r.forEach(([lvl, kind, msg]) => findings.push([lvl, i + 1, kind, msg]));
}
findings.sort((a, b) => a[1] - b[1]);
for (const [lvl, n, kind, msg] of findings) console.log(`${lvl}  slide ${String(n).padStart(2)}  ${kind.padEnd(20)} ${msg}`);
const fails = findings.filter(f => f[0] === 'FAIL').length;
console.log(`\n${statics.total} slides · ${fails} fail · ${findings.length - fails} warn · narrator: ${statics.narrator || '(none found)'}`);
await fetch(`http://127.0.0.1:${PORT}/json/close/${t.id}`); ws.close();
process.exit(fails ? 1 : 0);
