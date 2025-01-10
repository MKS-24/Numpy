import numpy as np


#  0 Array
arr1 = np.zeros(4) # 1d Array 
arr2 = np.zeros((3,4))  # 2d  row , colume
print(arr1)
print()
print(arr2)
print()

# ones
arr1 = np.ones(4) # 1d Array 
arr2 = np.ones((3,4))  # 2d Array  row , colume
print(arr1)
print()
print(arr2)
print()

# empty
arr1 = np.empty((1)) # 1d Array
arr1 = np.empty((1,6)) # nd Array
print(arr1)
print()


# arange
arr2 = np.arange(5,2)  # step wagera like pyton range
# arr2 = np.arange(5,10,2) # start end steps
print(arr2)
print()


# diagonal array
arr1 = np.eye(5) # diagonal array
arr1 = np.eye(5,10) # diagonal array  row colume
print(arr1)
print()


# linspace
arr1 = np.linspace(2,10,num = 5)  # yanii 2 se 10 tak itne 5 number hone chahiye is case me
print(arr1)