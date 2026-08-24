const { test, expect } = require('@playwright/test');
const AxeBuilder = require('@axe-core/playwright').default;
const catalogue = require('../site/tools.json');

const CATALOG_SIZE = catalogue.length;

const pages = [
  ['Home', '/'],
  ['Learn OSINT', '/learn-osint.html'],
  ['OSINT for Beginners', '/osint-for-beginners.html'],
  ['OSINT Tools', '/osint-tools.html'],
  ['Tool Finder', '/tool-finder.html'],
  ['Search', '/search.html'],
  ['Username OSINT', '/username-osint.html'],
  ['Reverse Image OSINT', '/reverse-image-osint.html'],
  ['Domain OSINT', '/domain-osint.html'],
  ['Company OSINT', '/company-osint.html'],
  ['GEOINT Guide', '/geoint-guide.html'],
  ['CTI OSINT', '/cti-osint.html'],
  ['Digital Footprint', '/digital-footprint.html'],
  ['Company Investigation', '/company-investigation.html'],
  ['Arabic', '/ar/'],
  ['Turkish', '/tr/'],
];

for (const [name, path] of pages) {
  test(`${name} has no automated WCAG A/AA violations`, async ({ page }) => {
    await page.goto(path, { waitUntil: 'networkidle' });

    const results = await new AxeBuilder({ page })
      .withTags(['wcag2a', 'wcag2aa', 'wcag21a', 'wcag21aa', 'wcag22aa'])
      .analyze();

    const summary = results.violations.map((violation) => ({
      id: violation.id,
      impact: violation.impact,
      help: violation.help,
      nodes: violation.nodes.map((node) => node.target),
    }));

    expect(summary, JSON.stringify(summary, null, 2)).toEqual([]);
  });
}

test('Tool Finder core controls are keyboard reachable without a focus trap', async ({ page }) => {
  await page.goto('/tool-finder.html', { waitUntil: 'networkidle' });
  await expect(page.locator('.tool')).toHaveCount(CATALOG_SIZE);

  const requiredIds = new Set(['q', 'category', 'input', 'cost', 'level', 'reset']);
  const reached = new Set();

  for (let i = 0; i < 18; i += 1) {
    await page.keyboard.press('Tab');
    const id = await page.evaluate(() => document.activeElement?.id || '');
    if (requiredIds.has(id)) reached.add(id);
  }

  expect([...reached].sort()).toEqual([...requiredIds].sort());
});

test('Tool Finder visible labels are associated with core filters', async ({ page }) => {
  await page.goto('/tool-finder.html', { waitUntil: 'networkidle' });

  for (const id of ['q', 'category', 'input', 'cost', 'level']) {
    await expect(page.locator(`label[for="${id}"]`)).toHaveCount(1);
  }
});

test('Full search controls are keyboard reachable', async ({ page }) => {
  await page.goto('/search.html', { waitUntil: 'networkidle' });
  const requiredIds = new Set(['q', 'lang', 'kind']);
  const reached = new Set();

  let id = await page.evaluate(() => document.activeElement?.id || '');
  if (requiredIds.has(id)) reached.add(id);

  for (let i = 0; i < 10; i += 1) {
    await page.keyboard.press('Tab');
    id = await page.evaluate(() => document.activeElement?.id || '');
    if (requiredIds.has(id)) reached.add(id);
  }

  expect([...reached].sort()).toEqual([...requiredIds].sort());
});
