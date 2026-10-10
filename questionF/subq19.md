# Question 19: Given a = np.array([11,11,12,13,14,15,16,17,12,13,11,14,18,19,20]), print the unique values, how many times each occurs, and the first index of each. Expected counts: [3 2 2 2 1 1 1 1 1 1].

## Aim

to find unique values, their counts and their first index

## Code

```python
import numpy as np

a = np.array([11,11,12,13,14,15,16,17,12,13,11,14,18,19,20])
u, idx, cnt = np.unique(a, return_index=True, return_counts=True)
print(u)
print(cnt)
print(idx)
```

## Output

```
[11 12 13 14 15 16 17 18 19 20]
[3 2 2 2 1 1 1 1 1 1]
[ 0  2  3  4  5  6  7 12 13 14]
```

## Explanation

np.unique returns sorted unique values  
return_index and return_counts give the first position and the count of each
