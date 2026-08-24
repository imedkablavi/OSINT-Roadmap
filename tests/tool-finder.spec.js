const { test, expect } = require('@playwright/test');
const catalogue = require('../site/tools.json');

const CATALOG_SIZE = catalogue.length;

async function openFinder(page, path = '/tool-finder.html') {
  const browserErrors = [];
  page.on('pageerror', error => browserErrors.push(`pageerror: ${error.message}`));
  page.on('console', message => {
    if (message.type() === 'error') browserErrors.push(`console: ${message.text()}`);
  });

  await page.goto(path);
  await expect(page.locator('#count')).toHaveText(new RegExp(`\\d+ of ${CATALOG_SIZE} curated tools`));
  expect(browserErrors).toEqual([]);
}

test('loads the full curated catalogue and freshness metadata without browser errors', async ({ page }) => {
  await openFinder(page);
  await expect(page.locator('#count')).toHaveText(`${CATALOG_SIZE} of ${CATALOG_SIZE} curated tools`);
  await expect(page.locator('article.tool')).toHaveCount(CATALOG_SIZE);
  await expect(page.locator('.chip.reviewed')).toHaveCount(CATALOG_SIZE);
  await expect(page.locator('#catalog-review')).toContainText('2026-08-23');

  await expect(page.locator('#category option')).not.toHaveCount(1);
  await expect(page.locator('#input option')).not.toHaveCount(1);
  await expect(page.locator('#cost option')).not.toHaveCount(1);
  await expect(page.locator('#level option')).not.toHaveCount(1);
});

test('search narrows results to a matching tool', async ({ page }) => {
  await openFinder(page);

  await page.locator('#q').fill('OCRmyPDF');
  await expect(page.locator('#count')).toHaveText(`1 of ${CATALOG_SIZE} curated tools`);
  await expect(page.locator('article.tool')).toHaveCount(1);
  await expect(page.getByRole('heading', { name: 'OCRmyPDF', exact: true })).toBeVisible();
  await expect(page.locator('.chip.reviewed')).toContainText('Reviewed 2026-08-23');
});

test('query-string searches deep-link into Tool Finder', async ({ page }) => {
  await openFinder(page, '/tool-finder.html?q=domain');
  await expect(page.locator('#q')).toHaveValue('domain');
  const count = await page.locator('article.tool').count();
  expect(count).toBeGreaterThan(0);
  expect(count).toBeLessThan(CATALOG_SIZE);
});

test('input filter only returns tools that accept the selected input', async ({ page }) => {
  await openFinder(page);

  await page.locator('#input').selectOption('Domain');
  const cards = page.locator('article.tool');
  const count = await cards.count();
  expect(count).toBeGreaterThan(0);
  expect(count).toBeLessThan(CATALOG_SIZE);

  for (let index = 0; index < count; index += 1) {
    await expect(cards.nth(index).locator('.chip', { hasText: 'Domain' })).toHaveCount(1);
  }
});

test('no-result state and reset behavior work', async ({ page }) => {
  await openFinder(page);

  await page.locator('#q').fill('__no_such_osint_tool__');
  await expect(page.locator('#count')).toHaveText(`0 of ${CATALOG_SIZE} curated tools`);
  await expect(page.locator('article.tool')).toHaveCount(0);
  await expect(page.locator('.empty')).toBeVisible();

  await page.getByRole('button', { name: 'Reset filters' }).click();
  await expect(page.locator('#count')).toHaveText(`${CATALOG_SIZE} of ${CATALOG_SIZE} curated tools`);
  await expect(page.locator('article.tool')).toHaveCount(CATALOG_SIZE);
  await expect(page.locator('#q')).toHaveValue('');
});

test('rendered external tool links use safe new-tab attributes', async ({ page }) => {
  await openFinder(page);

  const links = page.locator('a.open');
  await expect(links).toHaveCount(CATALOG_SIZE);

  const invalid = await links.evaluateAll(nodes => nodes
    .map(node => ({
      href: node.getAttribute('href'),
      target: node.getAttribute('target'),
      rel: node.getAttribute('rel') || '',
    }))
    .filter(link => !/^https:\/\//.test(link.href || '') || link.target !== '_blank' || !link.rel.includes('noopener') || !link.rel.includes('noreferrer')));

  expect(invalid).toEqual([]);
});

test('open-source tools are discoverable with provenance metadata', async ({ page }) => {
  await openFinder(page);

  await page.locator('#q').fill('Open Source');
  const cards = page.locator('article.tool');
  const count = await cards.count();
  expect(count).toBeGreaterThanOrEqual(5);
  await expect(cards.first().locator('.chip.opensource')).toBeVisible();
});

test('mobile viewport keeps filters and result actions usable', async ({ page }) => {
  await page.setViewportSize({ width: 390, height: 844 });
  await openFinder(page);

  await expect(page.locator('#q')).toBeVisible();
  await expect(page.locator('#category')).toBeVisible();
  await page.locator('#q').fill('MISP');
  await expect(page.locator('article.tool')).toHaveCount(1);
  await expect(page.locator('article.tool a.open')).toBeVisible();

  const overflow = await page.evaluate(() => document.documentElement.scrollWidth > document.documentElement.clientWidth);
  expect(overflow).toBe(false);
});
