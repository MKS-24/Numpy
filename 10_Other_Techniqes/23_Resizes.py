import numpy as np
arr = np.array([1,2,3,2,5,2,2,2,2,2])
print(arr)
y = np.resize(arr,(2,1))  # appni marzi se array ko resize kersakhte hai ( arr , (kitni rows , kitne size))
print(y)