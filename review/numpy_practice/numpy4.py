import numpy as np
x=np.linspace(0, 100, 10)
print(x)
y=np.logspace(np.log10(10), np.log10(100), 10)
print(y)
z = np.logspace(np.log10(250), np.log10(500), 10)
print(z)

# shape, size of array
X = np.array([[1, 2, 3], [4, 5, 6]])
print(X.shape)
print(X.size)

x = np.random.random(10)  # create 10 random numbers between 0 and 1
print(np.any(x>0.9))
print(np.all(x>=0.1))
print(x)