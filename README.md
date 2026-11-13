# AL07: Greedy Claims and Memoization Evidence

Name: Mark  
Partner(s): [add assigned partner name(s)]  
My contribution: Implemented the greedy-payment and memoized Fibonacci helpers, added focused tests, and checked the supplied case reports.

## Run

```powershell
py -3.14 main.py
py -3.14 main.py --n 5
py -3.14 main.py --help
py -3.14 test_assignment.py
```

## Handout

See [AL07_Memoization_Caching_and_Assignment_Syntax.md](AL07_Memoization_Caching_and_Assignment_Syntax.md) for the Week 5 memoization, caching, and assignment-syntax handout.

## Work Notes

- Payment finding: With coins 1, 4, and 6 for amount 8, largest-first returns 6 + 1 + 1, while the reference returns 4 + 4. Greedy is not always minimum-coin.
- Saved-answer finding: At n=5, both methods return 5; the uncached recurrence makes 15 calls, while memoization makes 9 calls (3 hits) and stores 6 inputs. The cache uses extra space to avoid repeated recursive work in this run.
- Question/decision: Does greedy getting stuck prove that no exact payment exists? No; for coins 4 and 6 with amount 8, the reference finds 4 + 4, so the two outcomes must be reported separately.

## Assistance

The supplied `coin_cases.py`, `reference_solver.py`, `investigation_support.py`, `investigation_display.py`, and `console_style.py` provide the cases, bounded reference solver, validation/wrappers, reporting, and terminal styling. Copilot SDK in VS Code helped implement the two required helpers and focused checks. I checked the case results, the n=5 call/hit/cache counts, edge cases, and invalid inputs by running `test_assignment.py`.

## Instructor Comments

[Reserved for instructor feedback.]
