// shot.mjs <out.png> <url> [captureHeight]
//
// Captures past the viewport WITHOUT growing the viewport. These sites give
// their heroes `min-height: 100vh`, so a tall --window-size makes the hero as
// tall as the capture and you see nothing else. CDP lets the layout viewport
// stay one normal screen (900px, so 100vh === 900px) while the screenshot
// extends below it, which is the only way to get a normal hero AND the page
// under it in one image.
const [out, url, wantH, offY] = process.argv.slice(2);
const W = 1400, VH = 900, H = Number(wantH || 1900), Y = Number(offY || 0);
const PORT = 9222;

const t = await (await fetch(`http://127.0.0.1:${PORT}/json/new?about:blank`, { method: 'PUT' })).json();
const ws = new WebSocket(t.webSocketDebuggerUrl);
let id = 0;
const pend = new Map(), waits = new Map();
ws.onmessage = e => {
  const m = JSON.parse(e.data);
  if (m.id && pend.has(m.id)) { pend.get(m.id)(m.result); pend.delete(m.id); }
  if (m.method && waits.has(m.method)) { waits.get(m.method)(); waits.delete(m.method); }
};
const send = (method, params = {}) => new Promise(r => { pend.set(++id, r); ws.send(JSON.stringify({ id, method, params })); });
const on = method => new Promise(r => waits.set(method, r));
const sleep = ms => new Promise(r => setTimeout(r, ms));

await new Promise(r => ws.onopen = r);
await send('Page.enable');
await send('Emulation.setDeviceMetricsOverride', { width: W, height: VH, deviceScaleFactor: 2, mobile: false });
const loaded = on('Page.loadEventFired');
await send('Page.navigate', { url });
await Promise.race([loaded, sleep(20000)]);
await sleep(3000);

const { cssContentSize } = await send('Page.getLayoutMetrics');
const clipH = Math.min(H, Math.round(cssContentSize.height) - Y);
const shot = await send('Page.captureScreenshot', {
  format: 'png', captureBeyondViewport: true,
  clip: { x: 0, y: Y, width: W, height: clipH, scale: 1 }
});
const fs = await import('node:fs');
fs.writeFileSync(out, Buffer.from(shot.data, 'base64'));
console.log(`${out.split('/').pop().padEnd(22)} ${W}x${clipH} at y=${Y}   page ${Math.round(cssContentSize.height)} tall (${(cssContentSize.height/VH).toFixed(1)} screens)`);
await fetch(`http://127.0.0.1:${PORT}/json/close/${t.id}`);
ws.close();
process.exit(0);
