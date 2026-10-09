#Question 5: Use a = np.arange(1, 36).reshape(5, 7). Print the 3rd row, the 4th column, the last row and the last column.

#Aim
#To print the 3rd row, 4th column, last row and last column of a 5x7 array.

#Code:

import numpy as np

a = np.arange(1, 36).reshape(5, 7)
print(a[2])      
print(a[:, 3])   
print(a[-1])     
print(a[:, -1])  

'''
Output

[15 16 17 18 19 20 21]
[ 4 11 18 25 32]
[29 30 31 32 33 34 35]
[ 7 14 21 28 35]

Explanation:
reshape is used to give the elements a shape as in like 2x2 3x3 etc
a[2] gives the 3rd row
a[:, 3] gives the 4th column (with all rows)
a[-1] gives the last row
a[:, -1] gives the last column (with all rows)

'''