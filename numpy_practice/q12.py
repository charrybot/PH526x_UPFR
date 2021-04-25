"""
12. Write a NumPy program to append values to the end of an array. Go to the editor
Expected Output:
Original array:
[10, 20, 30]
After append values to the end of the array:
[10 20 30 40 50 60 70 80 90]
"""
import numpy as np
x=np.array([10, 20, 30])
for i in range(4, 10):
    x = np.append(x, i*10)

print(x)


