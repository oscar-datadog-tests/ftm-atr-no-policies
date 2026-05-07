# QA card — `<fixture-repo-name>`

Each fixture overrides this file with concrete values.

## Description

(One sentence — what FTM Overview state does this fixture demonstrate?)

## Audit cells exercised

(Reference rows from `2026-04-30-ftm-overview-copy-audit.md`. Example: `§3.4 #4`, `§5.2 #1/#2`.)

## Required Datadog toggles

| Toggle | State | Where to set |
| --- | --- | --- |
| EFD | on / off | Test Optimization → Repo settings → Early Flake Detection |
| PR Gate | covering / not | Source Code → PR Gates → rule type `no_new_flaky_tests` |
| ATR | on / off | Test Optimization → Repo settings → Auto Test Retries |
| Policies | none / some / full | Test Optimization → Repo settings → Flaky Test Policies |

## Special setup steps

(Anything beyond toggles. E.g., install GitHub App, manually quarantine X, create notification rule for team Y.)

## Expected verdicts (after warm-up)

- §3.4 next-action: `<the exact copy this fixture should render>`
- §5.2 prevention verdict: `<...>`
- §6.2 mitigation verdict: `<...>`
- §7.2 remediation verdict: `<...>`

## Readiness

Ready for QA at: T+_ days after first push.

## How to refresh

If CI has gone silent (>60d inactive), kick a run:

```bash
git commit --allow-empty -m "rerun" && git push
```
