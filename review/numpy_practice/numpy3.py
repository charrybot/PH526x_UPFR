import numpy as np
z1 = np.array([1, 3, 5, 7, 9])
z2 = z1+1
print(z1)
print(z2)
ind = [0, 2, 3]
z3 = z1[ind]
print(z3)
z4 = (z1>6)
print(z4)
z5 = z1[z1 > 6]  # only returns values where the index is true

# slicing vs indexing
z1 = np.array([1, 3, 5, 7, 9])
w = z1[0:3] # if w is modified, z1 also gets modified
w[0]=3
print(w)
print(z1)

ind=[0, 1, 2]
x=z1[ind] # even if x is modified, z1 does not get modified



