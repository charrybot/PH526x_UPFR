"""
88. Write a NumPy program to replace all elements of NumPy array that are greater than specified array. Go to the editor

Expected Output:
Original array:
[[ 0.42436315 0.48558583 0.32924763]
[ 0.7439979 0.58220701 0.38213418]
[ 0.5097581 0.34528799 0.1563123 ]]
Replace all elements of the said array with .5 which are greater than. 5
[[ 0.42436315 0.48558583 0.32924763]
[ 0.5 0.5 0.38213418]
[ 0.5 0.34528799 0.1563123 ]]
"""
import numpy as np
arr = np.array([[0.42436315, 0.48558583, 0.32924763],
                [0.7439979, 0.58220701, 0.38213418],
                [0.5097581, 0.34528799, 0.1563123]])
arr[arr>0.5]=0.5
print(arr)