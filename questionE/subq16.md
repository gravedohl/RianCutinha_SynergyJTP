# Question 16: Given a 3x4 array of 1 to 12, print np.flip with no axis, with axis=0 and with axis=1.

## Aim

to flip a 3x4 array with no axis, axis=0 and axis=1.

## Code

```python
import numpy as np

m = np.arange(1, 13).reshape(3, 4)
print(np.flip(m))
print(np.flip(m, axis=0))
print(np.flip(m, axis=1))
```

## Output

```
[[12 11 10  9]
 [ 8  7  6  5]
 [ 4  3  2  1]]
[[ 9 10 11 12]
 [ 5  6  7  8]
 [ 1  2  3  4]]
[[ 4  3  2  1]
 [ 8  7  6  5]
 [12 11 10  9]]
```

## Explanation

no axis flips along all axes  
axis=0 flips the rows upside down so top becomes bottom  
axis=1 reverses each row left to right
