"""AL07 greedy-payment and memoized Fibonacci investigations."""

from investigation_support import validate_change
from investigation_display import run

ENABLE_MEMOIZATION = True


def greedy_change(denominations, target):
    """Return a largest-first exact payment, or None if greedy gets stuck."""
    coins = validate_change(denominations, target)
    payment = []
    remaining = target

    for coin in coins:
        while coin <= remaining:
            payment.append(coin)
            remaining -= coin

    if remaining:
        return None
    return payment


def calculate_cached(n, cache, counts):
    """Return F(n), reusing saved answers while counting every call and hit."""
    counts["calls"] += 1
    if n in cache:
        counts["hits"] += 1
        return cache[n]

    if n < 2:
        result = n
    else:
        previous = calculate_cached(n - 1, cache, counts)
        earlier = calculate_cached(n - 2, cache, counts)
        result = previous + earlier

    cache[n] = result
    return result


def main():
    """Present the payment cases and the optional memoization comparison."""
    run(greedy_change, calculate_cached, ENABLE_MEMOIZATION)


if __name__ == "__main__":
    main()
