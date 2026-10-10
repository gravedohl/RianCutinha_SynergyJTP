#Question 22: Write code that tries each of these additions and prints the result shape or the error message: (4,3)+(3,), (4,3)+(4,), (4,3)+(4,1), (2,3,4)+(3,1). 
#Use np.ones for the arrays.

#Aim
#to test which shape combos broadcast and which give errors.

#Code

import numpy as np

tests = [((4, 3), (3,)), ((4, 3), (4,)), ((4, 3), (4, 1)), ((2, 3, 4), (3, 1))]

for s1, s2 in tests:
    try:
        r = np.ones(s1) + np.ones(s2)
        print(s1, '+', s2, '->', r.shape)
    except ValueError:
        print(s1, '+', s2, '-> error')

'''

Output:

(4, 3) + (3,) -> (4, 3)
(4, 3) + (4,) -> error
(4, 3) + (4, 1) -> (4, 3)
(2, 3, 4) + (3, 1) -> (2, 3, 4)

Explanation:
the shape of the array on the right side is adjusted based on the one on the left 
so say if we have an array with only one dimension defined (row or column) then the other is considered as 1 and is broadcasted in a way such that it is valid
(4,3)+(3,) works cuz 3=3
(4,3)+(4,) fails cuz it compares 3 with 4 so error
(4,3)+(4,1) works cuz 1 stretches to 3
(2,3,4)+(3,1) compares 4 vs 1 ok, 3 vs 3 ok, and the missing leading dim is fine 

'''