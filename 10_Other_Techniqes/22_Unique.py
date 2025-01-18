import numpy as np
arr = np.array([1,2,3,2,5,2,2,2,2,2])
print(arr)
print(np.unique(arr))  # for unique array
print(np.unique(arr,return_index=True)) # for unique array along with elementy index
print(np.unique(arr,return_inverse=True)) # for unique array along with elementy index in a complete array
print(np.unique(arr,return_index=True,return_inverse=True)) # for unique array along with elementy index in a complete array
print(np.unique(arr,return_counts=True)) # for unique array ke all element ko count kerke batae ga ke kitni baar array me aae hai ye elements
