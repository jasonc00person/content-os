// node render.js  ->  slide-1.png .. slide-4.png (1080x1920) next to this file
const path = require('path');
const { chromium } = require('/Users/jasoncooperson/Projects/content-os/.claude/skills/carousel-generator/scripts/node_modules/playwright');

(async () => {
  const browser = await chromium.launch({ channel: 'chrome' }); // headless, throwaway profile
  const page = await browser.newPage({ viewport: { width: 900, height: 1600 }, deviceScaleFactor: 1.2 });
  await page.goto('file://' + path.join(__dirname, 'slides.html'));
  await page.evaluate(() => document.fonts.ready);
  await page.waitForLoadState('networkidle');
  const slides = await page.$$('.slide');
  for (let i = 0; i < slides.length; i++) {
    await slides[i].screenshot({ path: path.join(__dirname, `slide-${i + 1}.png`) });
  }
  await browser.close();
})();
