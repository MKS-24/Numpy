import numpy as np
arr=np.array([[1,2,3],
              [4,5,6]])
print(arr)

print(np.insert(arr , 2 , 8 , axis=1))
print()
print(np.insert(arr , 2 , 8 , axis=0))
print()
print(np.insert(arr , 2 , [8,9,7] , axis=0))
