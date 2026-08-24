const { test, expect } = require('@playwright/test');
const coreCatalogue = require('../site/tools.json');
const specialistCatalogue = require('../site/tools-specialist.json');
const trust = require('../site/tool-trust.json');

const catalogue = [...coreCatalogue, ...specialistCatalogue];
const CATALOG_SIZE = catalogue.length;
const OFFICIAL_COUNT = Object.values(trust.entries).filter(entry => entry.source_type === 'Official primary source').length;
const US_COUNT = Object.values(trust.entries).filter(entry => entry.jurisdiction === 'US').length;

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

test('loads the full curated catalogue, freshness and trust metadata without browser errors', async ({ page }) => {
  await openFinder(page);
  await expect(page.locator('#count')).toHaveText(`${CATALOG_SIZE} of ${CATALOG_SIZE} curated tools`);
  await expect(page.locator('article.tool')).toHaveCount(CATALOG_SIZE);
  await expect(page.locator('.chip.reviewed')).toHaveCount(CATALOG_SIZE);
  await expect(page.locator('#catalog-review')).toContainText('2026-08-23');
  await expect(page.locator('#catalog-review')).toContainText('schema v1');

  for (const id of ['category', 'input', 'sourceType', 'jurisdiction', 'cost', 'level']) {
    await expect(page.locator(`#${id} option`)).not.toHaveCount(1);
  }
});

test('search narrows results to a matching tool', async ({ page }) => {
  await openFinder(page);

  await page.locator('#q').fill('OCRmyPDF');
  await expect(page.locator('#count')).toHaveText(`1 of ${CATALOG_SIZE} curated tools`);
  await expect(page.locator('article.tool')).toHaveCount(1);
  await expect(page.getByRole('heading', { name: 'OCRmyPDF', exact: true })).toBeVisible();
  await expect(page.locator('.chip.reviewed')).toContainText('Reviewed 2026-08-23');
});

test('specialist expansion tools are searchable in the same finder', async ({ page }) => {
  await openFinder(page);
  await page.locator('#q').fill('PhoneInfoga');
  await expect(page.locator('#count')).toHaveText(`1 of ${CATALOG_SIZE} curated tools`);
  await expect(page.getByRole('heading', { name: 'PhoneInfoga', exact: true })).toBeVisible();
  await expect(page.getByText('GPL-3.0', { exact: true })).toBeVisible();
  await expect(page.locator('article.tool .chip.sourcekind', { hasText: 'Open-source tool' })).toHaveCount(1);
});

test('official primary-source filter returns only explicitly classified official sources', async ({ page }) => {
  await openFinder(page);
  await page.locator('#sourceType').selectOption('Official primary source');
  await expect(page.locator('article.tool')).toHaveCount(OFFICIAL_COUNT);
  expect(OFFICIAL_COUNT).toBeGreaterThanOrEqual(10);
  await expect(page.getByRole('heading', { name: 'OFAC Sanctions List Search', exact: true })).toBeVisible();

  const badges = page.locator('article.tool .chip.official');
  await expect(badges).toHaveCount(OFFICIAL_COUNT);
  for (let index = 0; index < OFFICIAL_COUNT; index += 1) {
    await expect(badges.nth(index)).toHaveText('Official primary source');
  }
});

test('jurisdiction filter exposes legal and registry scope without name guessing', async ({ page }) => {
  await openFinder(page);
  await page.locator('#jurisdiction').selectOption('US');
  await expect(page.locator('article.tool')).toHaveCount(US_COUNT);
  expect(US_COUNT).toBeGreaterThanOrEqual(8);
  await expect(page.getByRole('heading', { name: 'FEC Campaign Finance Data', exact: true })).toBeVisible();
  await expect(page.getByRole('heading', { name: 'LDA.gov Lobbying Disclosure Reports', exact: true })).toBeVisible();
  await expect(page.getByRole('heading', { name: 'UK Sanctions List', exact: true })).toHaveCount(0);
});

test('official and non-official resource buttons are labelled accurately', async ({ page }) => {
  await openFinder(page);
  await page.locator('#q').fill('OFAC Sanctions List Search');
  await expect(page.locator('article.tool')).toHaveCount(1);
  await expect(page.getByRole('link', { name: 'Open official source ↗', exact: true })).toBeVisible();

  await page.locator('#q').fill('MISP');
  await expect(page.locator('article.tool')).toHaveCount(1);
  await expect(page.getByRole('link', { name: 'Open resource ↗', exact: true })).toBeVisible();
});

test('new academic research category is available', async ({ page }) => {
  await openFinder(page);
  await page.locator('#category').selectOption('Academic & Research');
  await expect(page.locator('article.tool')).toHaveCount(3);
  await expect(page.getByRole('heading', { name: 'OpenAlex', exact: true })).toBeVisible();
  await expect(page.getByRole('heading', { name: 'Crossref Metadata Search', exact: true })).toBeVisible();
  await expect(page.getByRole('heading', { name: 'ORCID Search', exact: true })).toBeVisible();
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

test('no-result state and reset behavior work across trust filters', async ({ page }) => {
  await openFinder(page);

  await page.locator('#sourceType').selectOption('Official primary source');
  await page.locator('#jurisdiction').selectOption('UK');
  await page.locator('#q').fill('__no_such_osint_tool__');
  await expect(page.locator('#count')).toHaveText(`0 of ${CATALOG_SIZE} curated tools`);
  await expect(page.locator('article.tool')).toHaveCount(0);
  await expect(page.locator('.empty')).toBeVisible();

  await page.getByRole('button', { name: 'Reset filters' }).click();
  await expect(page.locator('#count')).toHaveText(`${CATALOG_SIZE} of ${CATALOG_SIZE} curated tools`);
  await expect(page.locator('article.tool')).toHaveCount(CATALOG_SIZE);
  await expect(page.locator('#q')).toHaveValue('');
  await expect(page.locator('#sourceType')).toHaveValue('');
  await expect(page.locator('#jurisdiction')).toHaveValue('');
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
  expect(count).toBeGreaterThanOrEqual(20);
  await expect(cards.first().getByText('Open Source', { exact: true })).toBeVisible();
});

test('mobile viewport keeps all trust filters and result actions usable', async ({ page }) => {
  await page.setViewportSize({ width: 390, height: 844 });
  await openFinder(page);

  for (const id of ['q', 'category', 'sourceType', 'jurisdiction']) {
    await expect(page.locator(`#${id}`)).toBeVisible();
  }
  await page.locator('#q').fill('MISP');
  await expect(page.locator('article.tool')).toHaveCount(1);
  await expect(page.locator('article.tool a.open')).toBeVisible();

  const overflow = await page.evaluate(() => document.documentElement.scrollWidth > document.documentElement.clientWidth);
  expect(overflow).toBe(false);
});