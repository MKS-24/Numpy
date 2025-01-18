# matrix ki inverse ke liye ....

import numpy as np    # order must be same in inverse 2x2 or nxn
arr = np.matrix([[1,2],
                [4,5]])
print(arr)
print(np.linalg.inv(arr))