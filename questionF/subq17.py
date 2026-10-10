#Question 17: Given a1 = [[1,1],[2,2]] and a2 = [[3,3],[4,4]], produce the vstack result, the hstack result, and np.concatenate along axis=1.

#Aim
#to join two 2x2 arrays in different ways.

#Code

import numpy as np

a1 = np.array([[1, 1], [2, 2]])
a2 = np.array([[3, 3], [4, 4]])

print(np.vstack((a1, a2)))
print(np.hstack((a1, a2)))
print(np.concatenate((a1, a2), axis=1))

'''

Output

[[1 1]
 [2 2]
 [3 3]
 [4 4]]
[[1 1 3 3]
 [2 2 4 4]]
[[1 1 3 3]
 [2 2 4 4]]

Explanation
vstack stacks one below the other 
hstack puts them side by side 
np.concatenate with axis=1 does the same as hstack 

'''