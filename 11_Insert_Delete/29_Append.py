import numpy as np
arr=np.array([1,2,3,4,5,6])
arr= np.append(arr , 4.5)
print(arr)
arr=np.append(arr , [5,5,6,7])


# array 2d 

arr=np.array([[1,2,3],
              [4,5,6]])
print(arr)
arr= np.append(arr , [[6,6,5]] , axis=1)
print(arr)
# Ensure that the array to be appended has the same number of rows (2 rows in this case)
arr = np.append(arr, [[8], [6]], axis=1)
print(arr)
