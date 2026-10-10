# Question 15: Given a = np.array([1, 2, 3, 4, 5, 6]), make a row vector (1, 6) and a column vector (6, 1). Do it once with np.newaxis and once with np.expand_dims.

## Aim

to convert a 1d array into row vector and colums vector using np.newaxis and np.expand_dims

## Code

```python
import numpy as np

a = np.array([1, 2, 3, 4, 5, 6])

row1 = a[np.newaxis, :]
col1 = a[:, np.newaxis]
row2 = np.expand_dims(a, axis=0)
col2 = np.expand_dims(a, axis=1)

print(row1.shape, col1.shape)
print(row2.shape, col2.shape)
```

## Output

```
(1, 6) (6, 1)
(1, 6) (6, 1)
```

## Explanation

np.newaxis adds a new axis basically while np.expand_dims does the same but like it extends the dimensions of the array
