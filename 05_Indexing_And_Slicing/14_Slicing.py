import numpy as np
arr = np.array([1,2,3,4,5,6,7,8,9])
print(arr[2:4])   # last wala exclude hota hai
arr = np.array([[1,2,3,4],[1,2,3,4]])
print(arr[0][2:3])
arr = np.array([[[1,2,3,4],[1,2,3,4]]])
print(arr[0][1][1:4])
print(arr[0][1][:4])
print(arr[0][1][0: : 3]) # steps