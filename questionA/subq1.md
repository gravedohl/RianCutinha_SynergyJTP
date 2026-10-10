# Question 1: Create an array from [3, 6, 9, 12, 15]. Print its shape, ndim, size and dtype.

## Aim

To make a numpy array and print its shape, ndim, size and dtype.

## Code

```python
import numpy as np

a = np.array([3, 6, 9, 12, 15])
print(a.shape, a.ndim, a.size, a.dtype)
```

## Output

```
(5,) 1 5 int64
```

## Explanation

a numpy array is created using np.array().  
shape gives the shape of the array  
ndim returns the dimensions of the array  
size returns the size of the array  
dtype returns the data type of the elements in the array
