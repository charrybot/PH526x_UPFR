"""
91. Write a NumPy program to remove all rows in a NumPy array that contain non-numeric values. Go to the editor
Expected Output:
Original array:
[[ 1. 2. 3.]
[ 4. 5. nan]
[ 7. 8. 9.]
[ 1. 0. 1.]]
Remove all non-numeric elements of the said array
[[ 1. 2. 3.]
[ 7. 8. 9.]
[ 1. 0. 1.]]
"""
import numpy as np
arr = np.array([[1., 2., 3.],
                [4., 5., np.nan],
                [7., 8., 9.],
                [1., 0., 1.]])

arr=arr[~np.isnan(arr).any(axis=1)]
print(arr)
