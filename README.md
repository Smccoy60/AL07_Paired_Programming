# AL07: Greedy Claims and Memoization Evidence

Name: Sarah Imhoff
Partner(s): Mark VanDenBeckens
My contribution: Mark and I used paried programmign for both Tuesday and Thursday.  We switched roles about every 20 minutes while workgn on teh programming and test assignments so that we both had time coding and reviewign/testing the work. 

## Run

```powershell
py -3.14 main.py
py -3.14 main.py --n 5
py -3.14 test_assignment.py
```

The --n option is used after enabling Thursday's stage.

## Work Notes

- Payment finding: With coin values [1, 4, 6] and a target of 8, the greedy method chose 6 + 1 + 1, which used 3 coins. The reference method found 4 + 4, which only used 2 coins. THis showed us that choosing the largest coin first does not always produce the fewest coins.
- Saved-answer finding: For Fibonacci 5, the memoized version returend the same answer of 5 while reusing answers that had already been clauclated.  It used 9 function calls, had 3 cache hits, and stored 6 distinct inputs. This showed us how memoization reduces repeated work, but it requires additional storage for the saved results.
- Pair question/decision: During paired programming, we discussed whether a greedy result of None meant tha tno exact payment was possible. Test [4, 6] with a target of 8 showed that greedy gets stuck after choosing 6, even though 4 + 4 is a valid solution. THis helped us decide that we needed the reference method to tell the difference between greedy getting stuck and no solution actually existing.

## Assistance

We used the supplied AL07 starter files, coin cases, validation and reference solver, investigation display, assignmetn directions, and class slides.

## Instructor Comments

[Reserved for instructor feedback.]
