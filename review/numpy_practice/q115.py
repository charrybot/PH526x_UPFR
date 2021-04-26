"""
115. Write a NumPy program to find indices of elements equal to zero in a NumPy array. Go to the editor
Sample Output:
Original array:
[1 0 2 0 3 0 4 5 6 7 8]
Indices of elements equal to zero of the said array:
[1 3 5]
"""
import numpy as np
arr = np.array([[1, 0, 2],
                [0, 3, 0],
                [4, 5, 6]])
ans = np.where(arr==0)
print(ans)
