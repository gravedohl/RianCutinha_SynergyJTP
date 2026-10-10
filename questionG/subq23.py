#Question 23: Create a 3x4 array with rng.random. 
#Print its overall sum, mean, min, max, std and prod, then the column sums, the row maxima, and the index of the overall maximum.

#Aim
#to use sum, mean, min, max, std, prod and axis-wise operations on a random 3x4 array.

#Code

import numpy as np

rng = np.random.default_rng()
z = rng.random((3, 4))
print(z)
print(z.sum(), z.mean(), z.min(), z.max(), z.std(), z.prod())
print(z.sum(axis=0))
print(z.max(axis=1))
print(z.argmax())

'''

Output

[[0.2121899  0.7417929  0.29162055 0.81468509]
 [0.68295438 0.6371789  0.87443023 0.18290048]
 [0.39066899 0.9375661  0.70788425 0.09062747]]
6.56449923478039 0.5470416028983659 0.09062747480818123 0.9375660981850912 0.2834977602235518 6.115631528853086e-05
[1.28581327 2.31653789 1.87393502 1.08821304]
[0.81468509 0.87443023 0.9375661 ]
9

Explanation
without axis the functions work on the whole array
axis=0 takes rows one by one so we get column sums 
axis=1 takes columns one by one so we get one max per row
argmax() gives the index of the biggest value in the flattened array  

'''