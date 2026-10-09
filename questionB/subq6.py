#Question 6: 
# Use the same array from Question 5. 
# Print every second element of the first row. 
# Print the 2x3 block from rows 1 to 2 and columns 2 to 4.

#Aim
#To print every second element of the first row and a 2x3 block from the array.

#Code:

import numpy as np

a = np.arange(1, 36).reshape(5, 7)
print(a[0, ::2])
print(a[1:3, 2:5])

'''

Output:

[1 3 5 7]

[[10 11 12]
 [17 18 19]]

Explanation:
print(a[0, ::2]) selects the 1st row and every second element of it
print(a[1:3, 2:5]) selects rows 1 to 2 and columns 2 to 4 and prints the 2x3 block of elements

'''