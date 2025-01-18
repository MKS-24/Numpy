import numpy as np
arr = np.matrix([[1,2,3],
                [2,3,4],
                [5,5,5]])
arr2 = np.matrix([[1,2,3],
                  [2,3,4],
                  [5,5,5]])

vrr = np.array([[1,2,3],
                [2,3,4],
                [5,5,5]])
vrr2 = np.array([[1,2,3],
                  [2,3,4],
                  [5,5,5]])

# matrix operation ke liye
print(arr+arr2)
print(arr-arr2)
print(arr/arr2)
print("Array opertaion below")
print(vrr+vrr2)
print(vrr-vrr2)
print(vrr/vrr2)
print()
# matrix multiplication ke liye hum 
print(arr.dot(arr2))
# or
print(arr*arr2)
print(vrr * vrr2)
print(vrr.dot(vrr2)) # form matrix multiplication 
# print(np.min_scalar_type(arr))
