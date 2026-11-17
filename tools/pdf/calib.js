// Rendu et calibrage des schémas Mermaid pour l'impression.
// Pour chaque schéma, plusieurs largeurs de retour à la ligne des étiquettes sont essayées ;
// on garde celle qui donne la plus grande échelle (donc le texte le plus lisible)
// en tenant dans la largeur du texte (W) et une hauteur maximale (MAX_H).
(async () => {
  const W = (7 - 1.6) * 96, MAX_H = 3.6 * 96, FONT_PX = 13;
  const WRAPS = [90, 120, 160, 200, 250, 320];
  window.__mermaidErrors = []; window.__figSizes = [];
  mermaid.initialize({
    startOnLoad: false, theme: 'neutral', fontFamily: 'Segoe UI, sans-serif',
    themeVariables: { fontSize: FONT_PX + 'px' },
    flowchart: { htmlLabels: true, useMaxWidth: false, nodeSpacing: 22, rankSpacing: 28, padding: 6 },
  });
  const sandbox = document.createElement('div');
  sandbox.style.cssText = 'position:absolute;left:-10000px;top:0;width:4000px';
  document.body.append(sandbox);
  let n = 0;
  for (const pre of [...document.querySelectorAll('pre.mermaid')]) {
    const code = pre.textContent;
    let best = null;
    for (const wrap of WRAPS) {
      try {
        const src = `%%{init: {"flowchart": {"wrappingWidth": ${wrap}, "nodeSpacing": 14, "rankSpacing": 18, "padding": 4, "diagramPadding": 2, "subGraphTitleMargin": {"top": 2, "bottom": 2}}}}%%\n` + code;
        const { svg } = await mermaid.render(`m${n++}`, src);
        sandbox.innerHTML = svg;
        const el = sandbox.querySelector('svg'), bb = el.getBBox();
        const w = bb.width + 8, h = bb.height + 8, s = Math.min(1, W / w, MAX_H / h);
        if (!best || s > best.s + 0.01) best = { svg, vb: [bb.x - 4, bb.y - 4, w, h], s, wrap };
      } catch (e) { window.__mermaidErrors.push(String(e)); }
    }
    if (!best) continue;
    const d = document.createElement('div'); d.className = 'mermaid'; d.innerHTML = best.svg;
    const el = d.querySelector('svg'), [, , w, h] = best.vb;
    el.removeAttribute('style'); el.setAttribute('viewBox', best.vb.join(' '));
    el.setAttribute('width', w * best.s); el.setAttribute('height', h * best.s);
    pre.replaceWith(d);
    window.__figSizes.push([Math.round(w), Math.round(h), +best.s.toFixed(2), best.wrap, +(FONT_PX * best.s * 0.75).toFixed(1)]);
  }
  sandbox.remove();
  // Garder la légende avec son illustration, son exemple ou son tableau court.
  document.querySelectorAll('p').forEach(p => {
    const nx = p.nextElementSibling;
    if (!nx || !/^(Figure|Exemple|Tableau) \d/.test(p.textContent.trim())) return;
    if (nx.tagName === 'TABLE' && nx.rows.length > 15) return;
    const k = document.createElement('div'); k.className = 'keep';
    p.before(k); k.append(p, nx);
  });
})().catch(e => window.__mermaidErrors.push(String(e))).finally(() => { window.__mermaidDone = true; });
