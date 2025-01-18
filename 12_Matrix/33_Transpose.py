import numpy as np
arr = np.matrix([[1,2,3],    # array or matrix ke liye same hi hai
                [2,3,4],
                [5,5,5]])
print(arr)
print(type(arr))

#  Transpose
print(arr.transpose())
print(np.transpose(arr))
print(np.matrix_transpose(arr))




