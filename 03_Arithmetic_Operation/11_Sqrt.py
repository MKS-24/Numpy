import numpy as np
arr = np.array([90,0])

#  sqrt
print(np.sqrt(arr))
print()


# sin and cos
print(np.sin(arr)) # Apply radian me hota hai
print(np.cos(arr)) # Apply radian me hota hai
print()


# cumsum
arr3 = np.array([1,2,3,4,5])    
print(np.cumprod(arr3))# left * right * next  [1   2   6  24 120]
print(np.cumsum(arr3)) # left + right + next  [1  3  6 10 15]
