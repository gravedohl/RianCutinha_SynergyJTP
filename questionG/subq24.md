# Question 24: Given A = [[1,2],[3,4]] and B = [[5,6],[7,8]], print the element-wise product, the matrix product with np.matmul ([[19 22] [43 50]]), and the determinant of A with np.linalg.det (-2.0).

## Aim

to find element-wise product, matrix product and determinant.

## Code

```python
import numpy as np

A = np.array([[1, 2], [3, 4]])
B = np.array([[5, 6], [7, 8]])

print(A * B)
print(np.matmul(A, B))
print(np.linalg.det(A))
```

## Output

```
[[ 5 12]
 [21 32]]
[[19 22]
 [43 50]]
-2.0000000000000004
```

## Explanation

A * B multiplies matching positions which is NOT matrix multiplication  
np.matmul does the real row-by-column thing  
np.linalg.det() gives the determinant
