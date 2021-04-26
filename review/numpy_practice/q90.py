"""
90. Write a NumPy program to remove the negative values in a NumPy array with 0. Go to the editor

Expected Output:
Original array:
[-1 -4 0 2 3 4 5 -6]
Replace the negative values of the said array with 0:
[0 0 0 2 3 4 5 0]
"""
import numpy as np
arr = np.array([-1, -4, 0, 2, 3, 4, 5, -6])
arr[arr<0]=0
print(arr)
