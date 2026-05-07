"""Always-failing tests. Only contribute when FAILURE_MODE=true env var is set.

Used to ensure pipeline-failure metrics populate even when ATR retries
recover most flakes (e.g., to drive §6.2 #5 "ATR couldn't catch X" branch).

Owned by @oscar-datadog-tests/flaky-team-d per CODEOWNERS.
"""

import pytest

from conftest import is_failure_mode


@pytest.mark.skipif(not is_failure_mode(), reason="FAILURE_MODE not enabled")
def test_unrecoverable_one():
    raise AssertionError("Hard failure — never passes")


@pytest.mark.skipif(not is_failure_mode(), reason="FAILURE_MODE not enabled")
def test_unrecoverable_two():
    raise AssertionError("Hard failure — never passes")
