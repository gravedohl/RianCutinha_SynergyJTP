# Question 2: Create a 3x2 array of zeros, a 2x4 array of ones with dtype=int, and a 2x3 array filled with 7 using np.full

## Aim

To create arrays filled with zeros ones and a constant value using np.zeros np.ones and np.full

## Code

```python
import numpy as np

print(np.zeros((3, 2)))
print(np.ones((2, 4), dtype=int))
print(np.full((2, 3), 7))
```

## Output

```
[[0. 0.]
 [0. 0.]
 [0. 0.]]
[[1 1 1 1]
 [1 1 1 1]]
[[7 7 7]
 [7 7 7]]
```

## Explanation

np.zeros((3,2)) makes 3 rows 2 cols of zeros with type float cuz default tdtype is float  
in np.ones i gave dtype=int so we get 1 not 1.  
np.full((2,3), 7) fills the whole 2x3 with 7
