const { test, expect } = require('@playwright/test');
const AxeBuilder = require('@axe-core/playwright').default;

const pages = [
  ['Home', '/'],
  ['Learn OSINT', '/learn-osint.html'],
  ['OSINT Tools', '/osint-tools.html'],
  ['Tool Finder', '/tool-finder.html'],
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
  await expect(page.locator('.tool')).toHaveCount(80);

  const requiredIds = new Set(['q', 'category', 'input', 'cost', 'level', 'reset']);
  const reached = new Set();

  for (let i = 0; i < 16; i += 1) {
    await page.keyboard.press('Tab');
    const id = await page.evaluate(() => document.activeElement?.id || '');
    if (requiredIds.has(id)) reached.add(id);
  }

  expect([...reached].sort()).toEqual([...requiredIds].sort());
});
