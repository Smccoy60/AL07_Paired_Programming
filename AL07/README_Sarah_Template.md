# AL07: Greedy Claims and Memoization Evidence

Name: Sarah  
Partner(s): Mark  
My contribution: I worked with Mark on the shared AL07 implementation and checks during Tuesday's session. I started, and we alternated driver and navigator about every 20–30 minutes, sharing progress at each handoff. We worked through the payment rules, compared the supplied cases with the reference, and checked the results together.

## Run

I keep the Python files and supplied modules together in this folder.

```powershell
py -3.14 main.py
py -3.14 main.py --n 5
py -3.14 main.py --help
py -3.14 test_assignment.py
```

## Work Notes

- For coins 1, 4, and 6 with target 8, greedy returns 6 + 1 + 1, while the supplied reference returns 4 + 4. This example shows that choosing the largest coin first does not always use the fewest coins.
- At n=5, both Fibonacci methods return 5. The uncached helper makes 15 calls; the cached helper makes 9 calls, including 3 hits, and stores 6 inputs. The cache stores calculated answers by input so repeated calls can reuse them. These counts show fewer helper calls in this run, not a timing benchmark or a universal performance claim.
- We discussed whether greedy getting stuck proves that no exact payment exists. For coins 4 and 6 with target 8, the reference finds 4 + 4, so a greedy failure does not prove that exact payment is impossible.

## Work Timing

Mark and I worked together in class on Tuesday and alternated driver and navigator about every 20–30 minutes. Mark was ill on Thursday, so I completed the first half of the Thursday enhancement that day, without a fixed time limit. I reviewed the recurrence, worked on the cache lookup, hit counting, and answer storage, and enabled the memoization stage. I handed off my work and progress to Mark, who completed the remaining comparisons and checks on Friday.

## Assistance

I used the supplied `coin_cases.py`, `reference_solver.py`, `investigation_support.py`, `investigation_display.py`, and `console_style.py` for the cases, reference solver, validation, reporting, and terminal styling. Copilot SDK in VS Code helped with the shared implementation and focused checks. I checked the results against the assignment requirements and the supplied reference.

## Instructor Comments

