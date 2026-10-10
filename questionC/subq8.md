# Question 8: Use arr = np.array([4, 15, 8, 23, 42, 16, 7, 30]). Print the values greater than 10, the even values, and the values from 10 to 30 inclusive.

## Aim

To filter array values using boolean conditions.

## Code

```python
import numpy as np

arr = np.array([4, 15, 8, 23, 42, 16, 7, 30])
print(arr[arr > 10])
print(arr[arr % 2 == 0])
print(arr[(arr >= 10) & (arr <= 30)])
```

## Output

```
[15 23 42 16 30]
[ 4  8 42 16 30]
[15 23 16 30]
```

## Explanation

arr > 10 makes a True/False array and putting it inside arr[] keeps only the true ones  
% 2 == 0 checks even  
& is the bitwise and operator
