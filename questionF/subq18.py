#Question 18: Given x = np.arange(1, 25).reshape(2, 12), split it into 3 equal parts. 
#Split it after the 3rd and 4th columns. 
#Then split np.arange(1, 7) into 4 parts with np.array_split.

#Aim
#to split arrays into 3 equal parts at given positions and unevenly with array_split

#Code

import numpy as np

x = np.arange(1, 25).reshape(2, 12)

p=np.split(x, 3, axis=1)
print(p)

p2=np.split(x, [3, 4], axis=1)
print(p2)

p3=np.array_split(np.arange(1, 7), 4)
print(p3)

'''

Output

[[ 1  2  3  4]
 [13 14 15 16]]
[[ 5  6  7  8]
 [17 18 19 20]]
[[ 9 10 11 12]
 [21 22 23 24]]
--
[[ 1  2  3]
 [13 14 15]]
[[ 4]
 [16]]
[[ 5  6  7  8  9 10 11 12]
 [17 18 19 20 21 22 23 24]]
--
[1 2]
[3 4]
[5]
[6]

Explanation
np.split(x, 3, axis=1) cuts the 12 columns into 3 equal parts of 4 columns each
[3, 4] cuts at column 3 and column 4 so we get 3 pieces 
np.split crashes if it cant divide equally thats why for 6 elements into 4 parts we use array_split which allows uneven sizes 

'''