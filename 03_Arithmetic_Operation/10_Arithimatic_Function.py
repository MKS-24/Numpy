import numpy as np
arr = np.array([2,3,9,4,5,1,7,8])

print(arr.max())
print(np.max(arr))
print(arr.argmax()) # poisition batataa max ki

print(arr.min())
print(np.min(arr))
print(arr.argmin()) # poisition batataa min ki

arr3 = np.array([[6,1,3],[5,6,7]])
print(np.max(arr3,axis=1))
print(arr3.max(axis=1))
print(arr3.min(axis=1))
print(np.min(arr3,axis=1))

print(np.max(arr3,axis=0))
print(arr3.max(axis=0))
print(arr3.min(axis=0))
print(np.min(arr3,axis=0))  # axis = 0 dono ke colume check kerta hai firsr colume fistrt matirix ka compare hoga second matrix ke first colume se  