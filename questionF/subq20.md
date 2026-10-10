# Question 20: Given a = np.array([1,2,3,4,5]) and b = np.array([4,5,6,7]), compute the union, intersection, difference (a minus b) and symmetric difference. Expected: [1..7], [4 5], [1 2 3], [1 2 3 6 7].

## Aim

to do union, intersection, difference and symmetric difference on two arrays.

## Code

```python
import numpy as np

a = np.array([1, 2, 3, 4, 5])
b = np.array([4, 5, 6, 7])

print(np.union1d(a, b))
print(np.intersect1d(a, b))
print(np.setdiff1d(a, b))
print(np.setxor1d(a, b))
```

## Output

```
[1 2 3 4 5 6 7]
[4 5]
[1 2 3]
[1 2 3 6 7]
```

## Explanation

union1d gives the union of two arrays without repeating common values  
intersect1d gives only common values  
setdiff1d(a, b) gives elements in a but not in b  
setxor1d gives elements in one of them but not both  
also all of the above give sorted outputs
