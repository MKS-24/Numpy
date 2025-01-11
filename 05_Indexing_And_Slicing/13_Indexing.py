import numpy as np
arr = np.array([1,2,3,4,5,6])
print(arr[5])
print(arr[-2]) # (Same as List)

arr = np.array([[1,2,3,4,5],
                [1,2,3,4,5]])
print(arr[0][4])  # arr[row][order]

arr = np.array([[[1,2,3,4,5],[1,2,3,4,5]]])

print(arr[0][1][4]) # arr[row][row][order]
