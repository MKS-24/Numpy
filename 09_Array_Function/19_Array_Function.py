import numpy as np
arr = np.array([1,2,3,4,2,6])
print(np.where(arr == 2))  # index through kerta ke 2 kaha kaha per hai
print(np.where((arr%2) == 0) ) # index through kerta ke 2 kaha kaha per hai
#  like condition

# for  Searching 
arr = np.array([9,0,8,1,2,7,5,6,10])
x = np.searchsorted(arr,6)
print(x)

arr = np.array([1,2,3,4,5,8,9,10])
x = np.searchsorted(arr,5,side="left")
x = np.searchsorted(arr,5,side="right")
x = np.searchsorted(arr,[5,6,7],side="right") # koi array me number insert kerna hai tu find kersakhte hai
print(x)


# for Sort
arr = np.array([9,0,8,1,2,7,5,6,10])
arr = np.array(["khan" , "aslam"])
x = np.sort(arr)
print(x)

arr = np.array([[9,0,8],[1,2,3] , [0,0,0]])
x = np.sort(arr)
print(x)