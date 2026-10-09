#Question 9: Find the indices of values greater than 15 using np.nonzero, then again using np.where. Expected: [1 3 4 5 7].

#Aim
#to find indices of values > 15 using np.nonzero and np.where.

#Code:

import numpy as np

arr = np.array([4, 15, 8, 23, 42, 16, 7, 30])
print(arr[np.nonzero(arr >= 15)])
print(arr[np.where(arr >= 15)])

'''

Output

[1 3 4 5 7]
[1 3 4 5 7]

Explanation
Both give the positions where the condition is true
these positions are entered into the array to access the elements at the positions
values >= 15 are 15, 23, 42, 16, 30 which sit at indices 1, 3, 4, 5, 7

'''