import numpy as np
arr=np.array([1,2,3,4,5,6])
arr=np.insert(arr,2,99)   # single value insert ki
print(arr)
arr=np.insert(arr,(2,4,1),99)   # Multiple single value insert ki
print(arr)
print(np.insert(arr,(2,4,1),99))
print(arr)

# arr = np.float16(arr)
arr2 = np.array([1,2,3])
print(arr2.dtype)
arr2=np.insert(arr2,2,99)
print(arr2)
arr2=np.insert(arr2,2,5.79)   # ye integer value hi only insert kerwaraha hai 
arr2 = np.float16(arr2)
print(arr2)
print(arr2.dtype)
arr2=np.insert(arr2,2,5.79)
print(arr2)