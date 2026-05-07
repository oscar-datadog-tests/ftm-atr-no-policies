"""Flaky test pool. Each test fails at probability FLAKE_RATE per run.

Pool size driven by NUM_FLAKY_TESTS env var.

Datadog's Early Flake Detection (and the flaky-test orchestrator) classifies
these as flaky after seeing the same test pass-and-fail across runs.

Owned by @oscar-datadog-tests/flaky-team-b per CODEOWNERS.
"""

import random

import pytest

from conftest import get_flake_rate, get_num_flaky_tests


@pytest.mark.parametrize("i", range(max(get_num_flaky_tests(), 0)))
def test_flaky(i):
    """Flaky test #{i}: fails at FLAKE_RATE probability per run."""
    if random.random() < get_flake_rate():
        pytest.fail(f"Simulated flake in test_flaky[{i}]")
