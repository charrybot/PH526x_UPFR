import numpy as np
x=np.empty(26)
for i in range(12, 38):
    x[i-12]=i

print(x)
y=np.flipud(x)
print(y)
