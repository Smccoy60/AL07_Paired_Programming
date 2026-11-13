"""Supplied human-readable reports and Thursday-only command-line wiring."""

import argparse
from coin_cases import CASES
from console_style import color_text, print_color
from investigation_support import exhaustive_change, uncached_fibonacci, cached_fibonacci, validate_n


def describe_payment(payment):
    """Describe an exact payment without displaying a raw collection."""
    if payment is None:
        return "No exact payment produced"
    if not payment:
        return "No coins needed (amount is zero)"
    parts = []
    for coin in payment:
        parts.append(str(coin))
    return " + ".join(parts) + f" ({len(payment)} coins)"


def show_change_cases(greedy_change):
    """Show usable payment choices and distinguish three different outcomes."""
    print()
    print_color("EXACT PAYMENT PLANNER", "heading")
    print("  Goal: exact payment with as few coins as possible.")
    print("  Assumption: unlimited coins of each listed value.\n")
    for index, case in enumerate(CASES):
        if index:
            print_color("  " + "-" * 52, "code")
        print_color(f"  CASE {index + 1}  |  {case['label']}", "heading")
        values = []
        for coin in case["coins"]:
            values.append(str(coin))
        print(f"    Coins available : {', '.join(values)}")
        print(f"    Target amount   : {case['target']}")
        greedy = greedy_change(case["coins"], case["target"])
        best = exhaustive_change(case["coins"], case["target"])
        print("    Largest-first   : " + color_text(describe_payment(greedy), "code"))
        print("    Minimum reference: " + color_text(describe_payment(best), "code"))
        if best is None:
            print_color("    RESULT: No exact payment exists with these coins.", "caution")
        elif greedy is None:
            print_color("    RESULT: A payment exists, but largest-first missed it.", "caution")
        elif len(greedy) > len(best):
            print_color("    RESULT: Exact, but largest-first uses extra coins.", "caution")
        else:
            print_color("    RESULT: Largest-first matches the minimum count.", "success")
        print()


def read_n():
    """Supply Thursday's single bounded argument, its default, and help text."""
    parser = argparse.ArgumentParser(description="AL07: bounded Fibonacci comparison")
    parser.add_argument("--n", type=int, default=8, help="Fibonacci input, 0-20 (default: 8)")
    args = parser.parse_args()
    try:
        validate_n(args.n)
    except ValueError as error:
        parser.error(str(error))
    return args.n


def show_memoization(n, calculate_cached):
    """Separate the unchanged recurrence answer from optional teaching evidence."""
    result, plain_calls = uncached_fibonacci(n)
    cached_result, calls, hits, cache = cached_fibonacci(n, calculate_cached)
    print_color("MEMOIZATION CHECK", "heading")
    print(f"  Input n              : {n}")
    print(f"  Fibonacci result     : {color_text(str(result), 'success')}")
    print(f"  Result with cache    : {color_text(str(cached_result), 'success')}")
    print_color("\n  WORK COMPARISON", "heading")
    print(f"  Calls without cache  : {plain_calls}")
    print(f"  Calls with cache     : {color_text(str(calls), 'success')}")
    print(f"  Cache hits           : {hits} (included in calls)")
    print(f"  Distinct inputs saved: {len(cache)}")
    print_color(
        "\n  Both runs start fresh. Counts show work, not elapsed time.",
        "code",
    )


def run(greedy_change, calculate_cached, enable_memoization):
    """Run Tuesday independently and add Thursday's comparison only when ready."""
    # No parser prerequisite on Tuesday; the Thursday stage introduces --n.
    n = None
    if enable_memoization:
        n = read_n()
    show_change_cases(greedy_change)
    if enable_memoization:
        show_memoization(n, calculate_cached)
