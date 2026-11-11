"""Optional AL07 scaffold: Tuesday payment choices, Thursday saved answers."""

from investigation_support import validate_change
from investigation_display import run

ENABLE_MEMOIZATION = True


# TUESDAY — Implement the local choice; the reference solver is supplied.
def greedy_change(denominations, target):
    """Return an exact payment using the largest fitting coins first"""
    coins = validate_change(denominations, target)
    chosen = []
    remaining = target
    for coin in coins:
        while remaining >= coin:
            chosen.append(coin)
            remaining -= coin

    if remaining == 0:
        return chosen
    return None

# THURSDAY — The recurrence and counters are supplied; add lookup and storage.
def calculate_cached(n, cache, counts):
    """Calculate Fibonacci while saving and reusing previous answers."""
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
    """Run the AL07 investigation"""
    run(greedy_change, calculate_cached, ENABLE_MEMOIZATION)


if __name__ == "__main__":
    main()
