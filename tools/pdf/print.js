// usage: node print.js <in.html> <out.pdf>
const puppeteer = require('puppeteer-core');
const path = require('path');
const fs = require('fs');

// Navigateur Chromium : variable BROWSER_PATH, sinon Edge ou Chrome aux emplacements usuels.
const CANDIDATES = [
  process.env.BROWSER_PATH,
  'C:\\Program Files (x86)\\Microsoft\\Edge\\Application\\msedge.exe',
  'C:\\Program Files\\Microsoft\\Edge\\Application\\msedge.exe',
  'C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe',
  '/Applications/Microsoft Edge.app/Contents/MacOS/Microsoft Edge',
  '/Applications/Google Chrome.app/Contents/MacOS/Google Chrome',
  '/usr/bin/microsoft-edge',
  '/usr/bin/google-chrome',
  '/usr/bin/chromium',
];

(async () => {
  const [inHtml, outPdf] = process.argv.slice(2);
  const executablePath = CANDIDATES.find(p => p && fs.existsSync(p));
  if (!executablePath) throw new Error('Aucun navigateur Chromium trouvé : définissez BROWSER_PATH.');
  const browser = await puppeteer.launch({
    executablePath,
    headless: true,
    args: ['--allow-file-access-from-files'],
  });
  const page = await browser.newPage();
  page.on('console', m => { if (m.type() === 'error') console.error('PAGE:', m.text()); });
  await page.goto('file:///' + path.resolve(inHtml).replace(/\\/g, '/'), { waitUntil: 'load' });
  await page.waitForFunction('window.__mermaidDone === true', { timeout: 120000 });
  const errs = await page.evaluate('window.__mermaidErrors');
  if (errs && errs.length) console.error('Mermaid errors:', errs);
  console.log('FIGS [w,h,scale,wrap,font pt]', JSON.stringify(await page.evaluate('window.__figSizes')));
  await page.pdf({
    path: outPdf,
    format: 'A4',
    preferCSSPageSize: true,
    printBackground: true,
    outline: true,
    tagged: true,
    displayHeaderFooter: true,
    headerTemplate: '<span></span>',
    footerTemplate: '<div style="width:100%;font-size:8pt;text-align:center;color:#666;font-family:Segoe UI,sans-serif"><span class="pageNumber"></span></div>',
  });
  await browser.close();
})().catch(e => { console.error(e); process.exit(1); });
