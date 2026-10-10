# Question 7: Given arr = np.arange(1, 13).reshape(2, 2, 3), print 6, then the first row of the second block ([7 8 9]), then the last element using negative indices (12).

## Aim

to navigate through given arr n return elemenst/subarrays using indexing and negative indexing

## Code

```python
import numpy as np

arr = np.arange(1, 13).reshape(2, 2, 3)
print(arr[0, 1, 2])
print(arr[1, 0])
print(arr[-1, -1, -1])
```

## Output

```
6
[7 8 9]
12
```

## Explanation

arr[0,1,2] means block 0, row 1, col 2, which is 6  
arr[1,0] is block 1 row 0 so the whole row [7 8 9]  
[-1,-1,-1] is the last element of the whole i.e. 12
