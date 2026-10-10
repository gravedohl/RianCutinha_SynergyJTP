# Question 25: In one line of NumPy, compute the mean squared error for predictions = np.array([2.5, 0.0, 2.1, 7.8]) and labels = np.array([3.0, -0.5, 2.0, 8.0]). Expected: 0.1375.

## Aim

to calculate MSE in a single line of code

## Code

```python
import numpy as np

predictions = np.array([2.5, 0.0, 2.1, 7.8])
labels = np.array([3.0, -0.5, 2.0, 8.0])

print(np.mean((predictions - labels) ** 2))
```

## Output

```
0.1375
```

## Explanation

mean gives the mean of the array given to it
