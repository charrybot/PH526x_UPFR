import numpy as np
x=np.empty((3, 3))
add=2
for i in range(0, 3):
    for j in range(0, 3):
        x[i][j]=add
        add+=1

print(x)

