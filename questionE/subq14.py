#Question 14: Reshape np.arange(1, 13) into (3, 4), (2, 6), (2, 3, 2) and (4, -1). Print the shape of each.

#Aim
#to reshape 1 to 12 into different shapes and print the shapes

#Code

import numpy as np

n = np.arange(1, 13)

print(n.reshape(3, 4).shape)
print(n.reshape(2, 6).shape)
print(n.reshape(2, 3, 2).shape)
print(n.reshape(4, -1).shape)

'''

Output

(3, 4)
(2, 6)
(2, 3, 2)
(4, 3)

Explanation
reshape is used to reshape an array into whichever size needed and shape returns the shape of the array

'''