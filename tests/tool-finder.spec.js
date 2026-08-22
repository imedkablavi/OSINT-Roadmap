const { test, expect } = require('@playwright/test');

async function openFinder(page) {
  const browserErrors = [];
  page.on('pageerror', error => browserErrors.push(`pageerror: ${error.message}`));
  page.on('console', message => {
    if (message.type() === 'error') browserErrors.push(`console: ${message.text()}`);
  });

  await page.goto('/tool-finder.html');
  await expect(page.locator('#count')).toHaveText('80 of 80 curated tools');
  await expect(page.locator('article.tool')).toHaveCount(80);
  expect(browserErrors).toEqual([]);
}

test('loads the full curated catalogue without browser errors', async ({ page }) => {
  await openFinder(page);

  await expect(page.locator('#category option')).not.toHaveCount(1);
  await expect(page.locator('#input option')).not.toHaveCount(1);
  await expect(page.locator('#cost option')).not.toHaveCount(1);
  await expect(page.locator('#level option')).not.toHaveCount(1);
});

test('search narrows results to a matching tool', async ({ page }) => {
  await openFinder(page);

  await page.locator('#q').fill('OCRmyPDF');
  await expect(page.locator('#count')).toHaveText('1 of 80 curated tools');
  await expect(page.locator('article.tool')).toHaveCount(1);
  await expect(page.getByRole('heading', { name: 'OCRmyPDF', exact: true })).toBeVisible();
});

test('input filter only returns tools that accept the selected input', async ({ page }) => {
  await openFinder(page);

  await page.locator('#input').selectOption('Domain');
  const cards = page.locator('article.tool');
  const count = await cards.count();
  expect(count).toBeGreaterThan(0);
  expect(count).toBeLessThan(80);

  for (let index = 0; index < count; index += 1) {
    await expect(cards.nth(index).locator('.chip', { hasText: 'Domain' })).toHaveCount(1);
  }
});

test('no-result state and reset behavior work', async ({ page }) => {
  await openFinder(page);

  await page.locator('#q').fill('__no_such_osint_tool__');
  await expect(page.locator('#count')).toHaveText('0 of 80 curated tools');
  await expect(page.locator('article.tool')).toHaveCount(0);
  await expect(page.locator('.empty')).toBeVisible();

  await page.getByRole('button', { name: 'Reset filters' }).click();
  await expect(page.locator('#count')).toHaveText('80 of 80 curated tools');
  await expect(page.locator('article.tool')).toHaveCount(80);
  await expect(page.locator('#q')).toHaveValue('');
});

test('rendered external tool links use safe new-tab attributes', async ({ page }) => {
  await openFinder(page);

  const links = page.locator('a.open');
  await expect(links).toHaveCount(80);

  const invalid = await links.evaluateAll(nodes => nodes
    .map(node => ({
      href: node.getAttribute('href'),
      target: node.getAttribute('target'),
      rel: node.getAttribute('rel') || '',
    }))
    .filter(link => !/^https:\/\//.test(link.href || '') || link.target !== '_blank' || !link.rel.includes('noopener') || !link.rel.includes('noreferrer')));

  expect(invalid).toEqual([]);
});
