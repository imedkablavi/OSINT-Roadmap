# Contributing

Thanks for helping improve OSINT Roadmap.

The project is meant to stay practical, current, and safe to use. Contributions are welcome whether they fix one broken link or add a complete learning module.

## What makes a good contribution

Good additions usually do at least one of these:

- explain a useful research method clearly;
- replace an outdated or dead resource;
- add a reproducible practice exercise;
- improve a translation;
- correct a factual or technical mistake;
- add a source that is better than an existing one;
- make a section easier for beginners to follow.

We prefer a smaller number of useful, maintained resources over very large uncurated tool lists.

## Adding a tool

If you suggest a tool, include enough context to answer:

1. What problem does it solve?
2. Is it free, freemium, or paid?
3. What skill level is it suitable for?
4. What are its important limitations?
5. Does using it create a privacy or OPSEC concern?
6. Is there a more direct primary source that should be checked first?

A tool should not be presented as proof by itself.

## Adding a research method

Methods should be lawful, based on public sources, and written so another person can reproduce the important steps.

Do not contribute instructions for:

- unauthorized access;
- credential attacks;
- bypassing access controls;
- impersonation or deceptive social engineering;
- stalking, harassment, or doxxing;
- collecting private or sensitive information without a legitimate basis.

## Adding a practice lab

Use fictional identities, your own material, consenting participants, historical/public-interest examples, public organizations, or purpose-built OSINT challenges.

A lab should include:

- goal;
- approximate difficulty;
- steps or expected workflow;
- skill being practiced;
- what a good conclusion should and should not claim.

## Writing style

Keep it direct.

- Prefer short examples over abstract definitions.
- Explain why a step matters.
- Avoid marketing language.
- Avoid pretending uncertainty does not exist.
- Use `public source`, `evidence`, `lead`, and `assessment` precisely.
- Link to original documentation or primary sources when possible.

## Pull requests

A normal contribution flow is:

```bash
git checkout -b improve/example-topic
# make changes
git add .
git commit -m "docs: improve example topic"
git push origin improve/example-topic
```

Then open a pull request and briefly explain:

- what changed;
- why it improves the roadmap;
- how you checked any new links or factual claims.

If the change is large, splitting it into focused commits makes review easier.

## Link maintenance

For resource updates, prefer official project pages over third-party mirrors. If a service has changed pricing, ownership, behavior, or availability in a way that affects the guide, mention it in the pull request.

## Translations

Translations should read naturally in the target language rather than following English sentence structure word-for-word. Technical names and tool names can stay in their original form when that is clearer.

## Questions

If you are not sure whether an idea fits, open an issue first. A short discussion is better than spending time on a large contribution that does not match the project.
