"""Reads env vars that drive flake behavior across all fixtures."""

import os
import random

# Read once at import; tests reference these via the conftest_settings fixture.
FLAKE_RATE = float(os.environ.get("FLAKE_RATE", "0"))
NUM_FLAKY_TESTS = int(os.environ.get("NUM_FLAKY_TESTS", "0"))
NUM_STABLE_TESTS = int(os.environ.get("NUM_STABLE_TESTS", "0"))
FAILURE_MODE = os.environ.get("FAILURE_MODE", "false").lower() == "true"


def get_flake_rate() -> float:
    return FLAKE_RATE


def get_num_flaky_tests() -> int:
    return NUM_FLAKY_TESTS


def get_num_stable_tests() -> int:
    return NUM_STABLE_TESTS


def is_failure_mode() -> bool:
    return FAILURE_MODE


# Optional: seed RNG via env so flake patterns are reproducible if needed.
_seed = os.environ.get("FLAKE_SEED")
if _seed is not None:
    random.seed(int(_seed))
