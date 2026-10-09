#Question 4: Create the numbers 0 to 9 as int8 and as int64. Print the nbytes of each

#Aim
#to compare how many bytes 0 to 9 takes as int8 and int64

#Code

import numpy as np

x8 = np.arange(10, dtype=np.int8)
x64 = np.arange(10, dtype=np.int64)
print(x8.nbytes)
print(x64.nbytes)

'''

Output 

10
80

Explanation:
np.arange is used to arange a particular range of numbers of a specified data type
nbytes = total no of bbytes
int8 is 1 byte each so 10 x 1 = 10 and int64 is 8 bytes each so 10 x 8 = 80
int64 uses 8 times more memory

'''