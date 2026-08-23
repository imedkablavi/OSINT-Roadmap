const { test, expect } = require('@playwright/test');

// Generates the repository preview from the real static page in Chromium.
test.use({ viewport: { width: 1440, height: 900 } });

test('capture Tool Finder preview', async ({ page }) => {
  await page.goto('/tool-finder.html', { waitUntil: 'networkidle' });
  await expect(page.locator('#count')).toHaveText('80 of 80 curated tools');
  await expect(page.locator('article.tool')).toHaveCount(80);
  await page.screenshot({
    path: 'preview-artifact/tool-finder-preview.png',
    fullPage: false,
    animations: 'disabled',
  });
});
