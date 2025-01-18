import numpy as np
arr = np.array([[1,2,3],
                [2,5,2],
                [2,2,2]])
print(arr)
print()
print(arr.ravel(order = 'K'))
print()
print(arr)
arr[0][1] = 50
print(arr)
print(arr.ravel(order = 'K'))


