const { test, expect } = require('@playwright/test');

async function openSearch(page, path = '/search.html') {
  const errors = [];
  page.on('pageerror', error => errors.push(error.message));
  page.on('console', message => { if (message.type() === 'error') errors.push(message.text()); });
  await page.goto(path, { waitUntil: 'networkidle' });
  await expect(page.locator('#status')).not.toContainText('Loading');
  expect(errors).toEqual([]);
}

test('full-content search index loads and returns documentation', async ({ page }) => {
  await openSearch(page);
  await page.locator('#q').fill('report');
  await expect(page.locator('.result').first()).toBeVisible();
  await expect(page.locator('#status')).toContainText('result');
  const paths = await page.locator('.result .meta').allTextContents();
  expect(paths.some(text => text.toLowerCase().includes('documentation'))).toBeTruthy();
});

test('search deep links accept a query parameter', async ({ page }) => {
  await openSearch(page, '/search.html?q=username');
  await expect(page.locator('#q')).toHaveValue('username');
  await expect(page.locator('.result').first()).toBeVisible();
});

test('language and content-type filters work', async ({ page }) => {
  await openSearch(page);
  await page.locator('#lang').selectOption('ar');
  await expect(page.locator('.result').first()).toBeVisible();
  const arabicMeta = await page.locator('.result .meta').allTextContents();
  expect(arabicMeta.every(text => text.includes('AR'))).toBeTruthy();

  await page.locator('#lang').selectOption('');
  await page.locator('#kind').selectOption('Website');
  await expect(page.locator('.result').first()).toBeVisible();
  const websiteMeta = await page.locator('.result .meta').allTextContents();
  expect(websiteMeta.every(text => text.includes('Website'))).toBeTruthy();
});
