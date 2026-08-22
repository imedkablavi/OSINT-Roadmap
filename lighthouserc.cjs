module.exports = {
  ci: {
    collect: {
      startServerCommand: 'python3 -m http.server 4173 --directory site',
      startServerReadyPattern: 'Serving HTTP',
      startServerReadyTimeout: 15000,
      numberOfRuns: 3,
      url: [
        'http://127.0.0.1:4173/',
        'http://127.0.0.1:4173/learn-osint.html',
        'http://127.0.0.1:4173/osint-tools.html',
        'http://127.0.0.1:4173/tool-finder.html',
        'http://127.0.0.1:4173/geoint-guide.html',
        'http://127.0.0.1:4173/cti-osint.html',
        'http://127.0.0.1:4173/digital-footprint.html',
        'http://127.0.0.1:4173/company-investigation.html',
        'http://127.0.0.1:4173/ar/',
        'http://127.0.0.1:4173/tr/',
      ],
      settings: {
        chromeFlags: '--headless --no-sandbox --disable-dev-shm-usage',
      },
    },
    assert: {
      assertions: {
        'categories:performance': ['error', { minScore: 0.90, aggregationMethod: 'median-run' }],
        'categories:accessibility': ['error', { minScore: 1.00, aggregationMethod: 'median-run' }],
        'categories:best-practices': ['error', { minScore: 0.95, aggregationMethod: 'median-run' }],
        'categories:seo': ['error', { minScore: 0.95, aggregationMethod: 'median-run' }],
        'first-contentful-paint': ['error', { maxNumericValue: 2500, aggregationMethod: 'median-run' }],
        'largest-contentful-paint': ['error', { maxNumericValue: 3000, aggregationMethod: 'median-run' }],
        'cumulative-layout-shift': ['error', { maxNumericValue: 0.10, aggregationMethod: 'median-run' }],
        'total-blocking-time': ['error', { maxNumericValue: 300, aggregationMethod: 'median-run' }],
      },
    },
    upload: {
      target: 'filesystem',
      outputDir: './lighthouse-reports',
    },
  },
};
