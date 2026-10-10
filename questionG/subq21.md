# Question 21: Given m = np.arange(1, 10).reshape(3, 3), add the row [10, 20, 30] to every row. Then add the column [[100], [200], [300]] to every column.

## Aim

to add a row and a column to a 3x3 matrix using broadcasting.

## Code

```python
import numpy as np

m = np.arange(1, 10).reshape(3, 3)
print(m + np.array([10, 20, 30]))
print(m + np.array([[100], [200], [300]]))
```

## Output

```
[[11 22 33]
 [14 25 36]
 [17 28 39]]
[[101 102 103]
 [204 205 206]
 [307 308 309]]
```

## Explanation

in broadcasting what happens is basically one of the arrays is stretched to match the shape of the other  
the row [10,20,30] gets added to every row  
the column [[100],[200],[300]] gets added to every column
