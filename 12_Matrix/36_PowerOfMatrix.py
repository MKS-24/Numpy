import numpy as np
arr = np.array([[1,2],   # matrix and arrays are same
                 [4,5]])
print(arr)
print(np.linalg.matrix_power(arr,-1))
print(np.linalg.matrix_power(arr,0))
print(np.linalg.matrix_power(arr,1))

# np.linalg.matrix_power(matrix name,n = ?)
# jab n = 0 hu tu identity matrix aaega
# jab n > 0 power apply hogi multiplication of matrix perform hogi 
# jab n < 0 inverse of matrix and power apply hogi multiplication of matrix perform hogi 
