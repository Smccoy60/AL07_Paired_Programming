"""Optional AL07 test starting point; expand it with your own expectations."""

from main import greedy_change, calculate_cached
from investigation_support import exhaustive_change, cached_fibonacci, uncached_fibonacci


def test_tuesday():
    """Check greedy change with counterexamples, boundraries, and input preservation"""
    # 1 Test - A Shorter exact payment exists
    assert greedy_change([1, 4, 6], 8) == [6, 1, 1]
    assert exhaustive_change([1, 4, 6], 8) == [4, 4]

    # 2 Test - Greedy gets stuck, even though an exact payment exists
    assert greedy_change([4, 6], 8) is None
    assert exhaustive_change([4, 6], 8) == [4, 4]

    # 3 Test - No exact payment exists
    assert greedy_change([4, 6], 7) is None
    assert exhaustive_change([4, 6], 7) is None

    # 4 Test - Both methods agree
    assert greedy_change([1, 5, 10], 12) == [10, 1, 1]
    assert exhaustive_change([1, 5, 10], 12) == [10, 1, 1]

    # 5 Test - A target of zero needs no coins
    assert greedy_change([1, 5, 10], 0) == []
    assert exhaustive_change([1, 5, 10], 0) == []

    # 6 Test - Unsorted denominations should still work
    assert greedy_change([1, 10, 5], 12) == [10, 1, 1]

    # 7 Test - Duplicate denominations should still work
    assert greedy_change([1, 5, 10, 5, 1], 12) == [10, 1, 1]

    # 8  The original input list should not be changed
    coins = [1, 4, 6]
    original_coins = coins.copy()
    greedy_change(coins, 8)
    assert coins == original_coins

    # 9 Test - Invalid targets shoudl raise ValueError
    try:
        greedy_change([1, 5, 10], -1)
        assert False
    except ValueError:
        pass
    try:
        greedy_change([1, 5, 10], 13)
        assert False
    except ValueError:
        pass

    # 10 - Invalid denomination lists should raise ValueError
    try:
        greedy_change([], 8)
        assert False
    except ValueError:
        pass
    try: 
        greedy_change([1, 0, 5], 8)
        assert False
    except ValueError:
        pass
    try:
        greedy_change([1, -4, 6], 8)
        assert False
    except ValueError:
        pass


def test_thursday():
    """Check saved answers and bounded counts against hand-checkable inputs."""

    # Check Fibonacci 5 and its memoization counts.
    result, calls, hits, cache = cached_fibonacci(5, calculate_cached)

    assert result == 5
    assert calls == 9
    assert hits == 3
    assert len(cache) == 6

    # Check the base case n = 0
    result, calls, hits, cache = cached_fibonacci(0, calculate_cached)
    assert result == 0
    assert calls == 1
    assert hits == 0
    assert len(cache) == 1

    # Check the base case n = 1
    result, calls, hits, cache = cached_fibonacci(1, calculate_cached)
    assert result == 1
    assert calls == 1
    assert hits == 0
    assert len(cache) == 1

    # check another known Fibonacci answer
    result, calls, hits, cache = cached_fibonacci(8, calculate_cached)
    assert result == 21

    # Check that repeated runs start fresh.
    first_run = cached_fibonacci(5, calculate_cached)
    second_run = cached_fibonacci(5, calculate_cached)
    assert first_run[0] == second_run[0]
    assert first_run[1] == second_run[1]
    assert first_run[2] == second_run[2]
    assert first_run[3] == second_run[3]

    # Compare the cached and uncached Fibonacci answers.
    cached_result, calls, hits, cache = cached_fibonacci(5, calculate_cached)
    uncached_result, uncached_calls =uncached_fibonacci(5)
    assert cached_result == uncached_result
    assert calls < uncached_calls

    # Invalid n below the allowed range shoudl raise ValueError.
    try: 
        cached_fibonacci(-1, calculate_cached)
        assert False
    except ValueError:
        pass

    # invalid n above the allowed range shoudl raise VlaueError.
    try:
        cached_fibonacci(21, calculate_cached)
        assert False
    except ValueError:
        pass


if __name__ == "__main__":
    test_tuesday()
    test_thursday()
    print("AL07 Checks Passed.")
