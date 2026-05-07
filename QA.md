# QA card — ftm-atr-no-policies

## Description

EFD + PR Gate + ATR on, Policies off. High flake rate (60%) so some pipelines slip past ATR retries.

## Audit cells exercised

- §3.4 #5 next-action — "Next: Mitigation. Enable Flaky Test Policies."
- §6.2 #5 mitigation verdict — "Auto Test Retries couldn't catch {N} flaky failures this month."
- §6.2 #6a/#6b — when flake rate happens to be low for a window
- §6.6 *some* state — after manually quarantining one targeted test

## Required Datadog toggles

| Toggle | State | Notes |
| --- | --- | --- |
| EFD | **on** | Repo settings |
| PR Gate | **on** | Source Code rule scoping this repo |
| ATR | **on** | Repo settings; max retries 2 |
| Policies | **none** | Default policy off |

## Special setup steps

To exercise §6.6 *some* (partial Policies state): after T+14, open Datadog → Test Optimization → Tests Explorer, search for `test_targeted_alpha` scoped to this repo, set Status: Quarantined. Reversal: set back to Active.

## Expected verdicts (after warm-up)

- §3.4 next-action: "Next: Mitigation. Enable Flaky Test Policies."
- §6.2 mitigation verdict: §6.2 #5 "Auto Test Retries couldn't catch {N} flaky failures this month."

## Readiness

T+14.

## How to refresh

```bash
git commit --allow-empty -m "rerun" && git push
```
