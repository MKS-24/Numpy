#  Data type pata kerne ke liye dtype ka use kerte hai

import numpy as np

arr = np.array([1.5,2])
print(arr.dtype)

arr = np.array(['A','V'])
print(arr.dtype)

arr = np.array([1,2])
print(arr.dtype)
# change datatype as an argument int8
arr = np.array([1,2],dtype = np.int8)
print(arr.dtype)

# change datatype float  'shortcut'
arr = np.array([1,2],dtype = 'str')
arr = np.array([1,2],dtype = 'f')
print(arr.dtype)
print(arr)

# change datatype float
arr = np.array([1,2])
new = np.int16(arr)
# new = np.int_(arr)
print(new.dtype)

# # Change data type
print(arr.astype(int))
print(arr.astype(float))
print(arr.astype(str))