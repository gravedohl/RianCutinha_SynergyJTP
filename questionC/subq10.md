# Question 10: Given marks = np.array([[45,80,67],[90,55,72],[38,60,85]]), print the marks that are 60 or above. Then count how many students scored 40 or more in each subject (column). Expected: [2 3 3].

## Aim

to print marks >= 60 and count the no of students scoring 40 n above in each subject.

## Code

```python
import numpy as np

marks = np.array([[45, 80, 67], [90, 55, 72], [38, 60, 85]])
print(marks[marks >= 60])
print((marks >= 40).sum(axis=0))
```

## Output

```
[80 67 90 72 60 85]
[2 3 3]
```

## Explanation

The mask marks >= 60 picks the matching values  
marks >= 40 gives true or false and true counts as 1 so .sum(axis=0) adds each column
