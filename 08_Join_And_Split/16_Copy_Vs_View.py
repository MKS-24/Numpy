import numpy as np
arr = np.array([1,2,3,4,5])
nakal = arr.copy() # for create copy 
print(arr)
print(nakal)

dekhu = arr.view() # for create view 
print(arr)
print(dekhu)

#  diff between copy and view

arr[0] = 999  # arr ko change kiya tu view change hojae ga copy wala nh change hoga
print(arr)
print(dekhu)
print(nakal)

dekhu[0] =1000 # view ko change kiya tu arr change hojae ga copy wala nh change hoga
print(arr)
print(dekhu)
print(nakal)
print()
arr = np.array([1,2,3,4,5])
print(arr)
arr = np.append([6,5,6],arr)
print(arr)
arr[0] = 5000
print(dekhu)
# arr = np.append(6,arr)
# arr = np.append(arr,6)
# print(arr)
# arr = np.delete(arr,3)  # arr ka 3rd index remove kerte hai delete se


