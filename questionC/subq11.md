# Question 11: Given s = np.array([2, 5, 8, 11, 14]), use np.searchsorted to find where 9 would be inserted. Then do it for [1, 12, 5] in one call. Expected: 3, then [0 4 1].

## Aim

to find where values would go in a sorted array to keep it sorted.

## Code

```python
import numpy as np

s = np.array([2, 5, 8, 11, 14])
print(np.searchsorted(s, 9))
print(np.searchsorted(s, [1, 12, 5]))
```

## Output

```
3
[0 4 1]
```

## Explanation

searchsorted does a binary search and gives the index where the value can be inserted  
9 goes between 8 and 11 so index 3  
1 goes at 0, 12 goes at 4, and 5 is already there so it returns index 1  
array must be sorted already or u get nonsense
