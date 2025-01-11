import numpy as np
arr = np.array([[1,2,3,4],[1,2,3,4]]) .reshape(2,4)
arr2 = np.array([[1,2],[3,4],[5,6],[7,8]])      .reshape(2,4)
print(arr)
print(arr2)
print(f"arr ki Shape : {arr.shape}",f"arr ki Shape : {arr2.shape}")
print(arr+arr2)  # operation tab hogi jab dimension same hogi ya dono matrix k order me same hu ya  kisi aik me (2,1)(1,2) me 1 hu


arr = np.array([1,2,3]) .reshape(1,3)
arr2 = np.array([1,2,3]) .reshape(3,1)
print(arr)
print(arr2)
print(f"arr ki Shape : {arr.shape}",f"arr ki Shape : {arr2.shape}")
print(arr+arr2)  # operation tab hogi jab dimension same hogi ya dono matrix k order me right aligned (1,2)(4,2) same hu 

arr = np.array([1,2]) .reshape(2,1)
arr2 = np.array([[1,2],[1,2]]) .reshape(2,2)
print(arr)
print(arr2)
print(f"arr ki Shape : {arr.shape}",f"arr ki Shape : {arr2.shape}")
print(arr+arr2)  # operation tab hogi jab dimension same hogi ya dono matrix k order me right aligned (1,2)(4,2) same hu 




#  after operation new matrix ka order hoga
# order of new matrix = (Bignumber from first matrix array order , Bignumber from Second matrix array order)