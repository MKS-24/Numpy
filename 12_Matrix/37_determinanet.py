
import numpy as np    # order must be same in inverse 2x2 or nxn
arr = np.matrix([[1,0],
                [1,0]]) # order must be same
print(np.linalg.det(arr)) # ad-bc

arr = np.matrix([[1,4,1],
                 [2,5,2],
                 [3,9,3]]) # order must be same
print(np.linalg.det(arr)) # ad-bc