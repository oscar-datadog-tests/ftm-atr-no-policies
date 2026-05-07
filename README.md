# ftm-fixture-template

Source template for the FTM Overview page QA fixtures.

This repo is **not** a runnable fixture — it's the source for spawning fixture
repos via GitHub's "Use this template" button (or `gh repo create --template`).

## Spawning a fixture

```bash
gh repo create oscar-datadog-tests/ftm-<scenario> \
    --template oscar-datadog-tests/ftm-fixture-template \
    --public \
    --clone
```

Then customize `qa.config.yml`, set per-repo variables (`FLAKE_RATE`,
`NUM_FLAKY_TESTS`, etc.) via `gh variable set`, and add `DD_API_KEY` as a
repo secret.

## See also

- `oscar-datadog-tests/ftm-qa-index` — the QA index for all fixtures
- `2026-05-05-ftm-overview-qa-fixtures-design.md` — design doc
- `2026-04-30-ftm-overview-copy-audit.md` — audit ground truth
