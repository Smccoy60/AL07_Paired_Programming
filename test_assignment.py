"""Focused regression checks for the AL07 investigations."""

from main import calculate_cached, greedy_change
from investigation_support import (
    cached_fibonacci,
    exhaustive_change,
    uncached_fibonacci,
)


def test_tuesday():
    """Check exactness, greedy limitations, input handling, and immutability."""
    coins = [1, 4, 6]
    original = coins.copy()
    greedy = greedy_change(coins, 8)
    reference = exhaustive_change(coins, 8)
    assert greedy == [6, 1, 1]
    assert reference == [4, 4]
    assert sum(greedy) == sum(reference) == 8
    assert len(greedy) > len(reference)
    assert coins == original

    assert greedy_change([4, 6], 8) is None
    assert exhaustive_change([4, 6], 8) == [4, 4]
    assert greedy_change([4, 6], 7) is None
    assert exhaustive_change([4, 6], 7) is None

    agreed_greedy = greedy_change([1, 5, 10], 12)
    agreed_reference = exhaustive_change([1, 5, 10], 12)
    assert sum(agreed_greedy) == sum(agreed_reference) == 12
    assert len(agreed_greedy) == len(agreed_reference) == 3
    assert greedy_change([1, 5, 10], 0) == []

    unsorted_duplicates = [4, 1, 4, 6]
    unchanged = unsorted_duplicates.copy()
    assert greedy_change(unsorted_duplicates, 8) == [6, 1, 1]
    assert unsorted_duplicates == unchanged

    invalid_cases = [
        ([], 0),
        ([1], True),
        ([True], 1),
        ([0], 1),
        ([-1, 2], 1),
        ([1], 13),
        ([1], 1.5),
        ((1, 2), 2),
    ]
    for denominations, target in invalid_cases:
        try:
            greedy_change(denominations, target)
        except ValueError:
            pass
        else:
            raise AssertionError(
                f"Expected ValueError for {denominations!r}, target {target!r}"
            )


def test_thursday():
    """Check recurrence results, call accounting, storage, and fresh runs."""
    plain_result, plain_calls = uncached_fibonacci(5)
    result, calls, hits, cache = cached_fibonacci(5, calculate_cached)
    assert plain_result == result == 5
    assert plain_calls == 15
    assert calls == 9
    assert hits == 3
    assert cache == {0: 0, 1: 1, 2: 1, 3: 2, 4: 3, 5: 5}
    assert calls == hits + len(cache)

    assert uncached_fibonacci(0) == (0, 1)
    assert uncached_fibonacci(1) == (1, 1)
    assert cached_fibonacci(0, calculate_cached) == (0, 1, 0, {0: 0})
    assert cached_fibonacci(1, calculate_cached) == (1, 1, 0, {1: 1})
    assert uncached_fibonacci(10)[0] == 55
    assert cached_fibonacci(10, calculate_cached)[0] == 55

    first_run = cached_fibonacci(5, calculate_cached)
    second_run = cached_fibonacci(5, calculate_cached)
    assert first_run[:3] == second_run[:3] == (5, 9, 3)
    assert first_run[3] == second_run[3]
    assert first_run[3] is not second_run[3]

    counts = {"calls": 0, "hits": 0}
    zero_cache = {0: 0}
    assert calculate_cached(0, zero_cache, counts) == 0
    assert counts == {"calls": 1, "hits": 1}

    for invalid_n in (-1, 21, True, 1.5):
        for calculate in (
            lambda value: uncached_fibonacci(value),
            lambda value: cached_fibonacci(value, calculate_cached),
        ):
            try:
                calculate(invalid_n)
            except ValueError:
                pass
            else:
                raise AssertionError(f"Expected ValueError for n={invalid_n!r}")


if __name__ == "__main__":
    test_tuesday()
    test_thursday()
    print("All AL07 checks passed.")
