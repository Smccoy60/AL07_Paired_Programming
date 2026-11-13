# AL07: Greedy Claims and Memoization Evidence

Name: Mark  
Partner(s): Sarah  
My contribution: Sarah and I split the AL07 work evenly. Sarah started, and we exchanged the driver/navigator role and shared progress every 20–30 minutes. I also added an extra console color for code output. I was sick on Thursday so Sarah worked alone and did about half of Thursdays work and then I finished it and checked everything on Friday. 

## Run

I keep the Python files and supplied modules together in this folder.

```powershell
py -3.14 main.py
py -3.14 main.py --n 5
py -3.14 main.py --help
py -3.14 test_assignment.py
```

## Handout

I used [AL07_Memoization_Caching_and_Assignment_Syntax.md](AL07_Memoization_Caching_and_Assignment_Syntax.md) for the Week 5 memoization, caching, and assignment-syntax handout.

## Work Notes

- I compared greedy and the supplied reference for coins 1, 4, and 6 with target 8. Greedy returns 6 + 1 + 1, while the reference returns 4 + 4, so this example shows that greedy does not always use the fewest coins.
- At n=5, both Fibonacci methods return 5. The uncached helper makes 15 calls; the cached helper makes 9 calls, including 3 hits, and stores 6 inputs. I use this run as evidence of fewer repeated helper calls in exchange for cache space, not as a timing benchmark or a universal performance claim.
- I checked whether greedy getting stuck proves that no exact payment exists. For coins 4 and 6 with target 8, the reference finds 4 + 4, so I report greedy failure separately from impossibility.

## Team Work and Handoffs

Sarah and I worked together in class on Tuesday. Sarah started, and we took turns driving and navigating while sharing our progress every 20–30 minutes. We split the Thursday enhancement evenly: Sarah completed the first half on Thursday without a fixed time limit, then handed off her work and progress. I finished the second half on Friday, including the remaining checks, after she was done. We shared the finished changes and results.

## Assistance

I used the supplied `coin_cases.py`, `reference_solver.py`, `investigation_support.py`, `investigation_display.py`, and `console_style.py` for the cases, reference solver, validation, reporting, and terminal styling. Copilot SDK in VS Code helped me with implementation, focused checks, and the optional memoization/caching handout. I checked the work against the assignment and ran `py -3.14 test_assignment.py`; all checks passed.

## Instructor Comments

