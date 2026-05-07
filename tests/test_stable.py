"""Always-passing tests. Pool size driven by NUM_STABLE_TESTS env var.

Owned by @oscar-datadog-tests/flaky-team-a per CODEOWNERS.
"""

import pytest

from conftest import get_num_stable_tests


@pytest.mark.parametrize("i", range(max(get_num_stable_tests(), 0)))
def test_stable(i):
    """Stable test #{i}: always passes."""
    assert True
