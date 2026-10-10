# Question 12: Create a = np.arange(1, 9) and b = a[2:6]. Set b[0] = 99 and print a. Repeat with b = a[2:6].copy() and print a again.

## Aim

to show that slicing changes original but .copy() doesnt

## Code

```python
import numpy as np

a = np.arange(1, 9)
b = a[2:6]
b[0] = 99
print(a)

a = np.arange(1, 9)
b = a[2:6].copy()
b[0] = 99
print(a)
```

## Output

```
[ 1  2 99  4  5  6  7  8]
[1 2 3 4 5 6 7 8]
```

## Explanation

A slice is just the part of the original array displayed  
it shares memory with the original, so changing b[0] changed a too  
with .copy() we get a  new array so a stays same
