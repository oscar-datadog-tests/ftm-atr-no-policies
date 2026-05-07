"""Specific named flaky tests with distinct identities.

Unlike test_flaky_pool which is parametrized, these have stable test names
so they're easier to refer to in QA setup steps (manual quarantine, manual
notification rule scoping, etc.).

Owned by @oscar-datadog-tests/flaky-team-c per CODEOWNERS.
"""

import random

from conftest import get_flake_rate


def test_targeted_alpha():
    """Targeted flaky alpha — for manual quarantine demos."""
    if random.random() < get_flake_rate():
        raise AssertionError("Simulated flake: alpha")


def test_targeted_beta():
    """Targeted flaky beta — for manual notification rule scoping."""
    if random.random() < get_flake_rate():
        raise AssertionError("Simulated flake: beta")


def test_targeted_gamma():
    """Targeted flaky gamma — reserved for future QA scenarios."""
    if random.random() < get_flake_rate():
        raise AssertionError("Simulated flake: gamma")
