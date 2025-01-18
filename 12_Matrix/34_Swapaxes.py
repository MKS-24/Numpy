import numpy as np
arr = np.array([[[1, 2, 3], [4, 5, 6], [7, 8, 9]],  
                [[10, 11, 12], [13, 14, 15], [16, 17, 18]]])
print(arr)
print("**********************************")
print(arr.swapaxes(0,1))
print("**********************************")
print(arr.swapaxes(1,2))

arr = np.array([[1,2,3],
                [4,5,6]])
print(arr)
print("**********************************")
print(arr.swapaxes(0,1))      #  row ko coloum banadu




# matrix per ager apply kerna hai tu 2d tak hi apply hoga....
# Ager multiple dimentions per swapaxes kerna hai tu aap arrays per swapaxs ka function lagae gaige