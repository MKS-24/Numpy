#  List and array me difference hota hai 
# list me koi bhi datatype store kersakhte hai
# Array me hum koi aik datatype store kerte hai

import numpy as np

# x = [1,2,3,"khan",4]
# y = np.array(x)
# print(type(y))  # <class 'numpy.ndarray'> nd mean n-dimentional
# print(y)




lst = []
for i in range(1,5):
    val = int(input("Enter Value : "))
    lst.append(val)

print(type(lst))
print(lst)
arr = np.array(lst)
print()
print(type(arr))
print(arr)

print("Number of Dimentioanal",arr.ndim)   # ndim is for n-dimentional array batata hai