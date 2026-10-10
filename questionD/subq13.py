#Question 13: Given x = np.array([[1,2,3],[4,5,6]]), create f = x.flatten() and r = x.ravel(). 
#Set f[0] = 100 and r[1] = 200, then print x.

#Aim
#to see which one of flatten and ravel returns a copy and which a view.

#Code

import numpy as np

x = np.array([[1, 2, 3], [4, 5, 6]])
f = x.flatten()
r = x.ravel()
f[0] = 100
r[1] = 200
print(x)

'''

Output

[[  1 200   3]
 [  4   5   6]]

Explanation
flatten() always returns a copy so changing f[0] did nothing to x 
ravel() returns a view so r[1] = 200 changed x So flatten = safe copy, ravel = faster but linked to original.
so flatten is basically a safe copy while ravel shows a view of the original array

'''