# Question 3: With rng = np.random.default_rng(), create a 3x3 array of random floats and a 2x5 array of random integers from 0 to 9. Then use np.random.randint to create a 4x4 array of integers from 1 to 100.

## Aim

To generate random floats and integers using rng=np.random.default_rng() and np.random.randint.

## Code

```python
import numpy as np

rng = np.random.default_rng()
print(rng.random((3, 3)))
print(rng.integers(0, 10, size=(2, 5)))
print(np.random.randint(1, 101, size=(4, 4)))
```

## Output

```
[[0.97822302 0.33368641 0.97236334]
 [0.14947489 0.25828825 0.98812262]
 [0.87944967 0.45451306 0.02476837]]

[[6 3 1 8 8]
 [3 9 3 0 4]]

[[36  9 12  8]
 [89 47 76 29]
 [80 49  6 10]
 [24 29 94 41]]
```

## Explanation

rng.random((3,3)) gives floats between 0 and 1  
rng.integers(0, 10, ...) gives ints from 0 to 9  
np.random.randint(1, 101, ...) is the other way and to get 1 to 100 we hv to write 101 cuz the upper limit is excluded and also values change on every run since no seed is set.
