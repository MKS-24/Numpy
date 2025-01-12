import numpy as np
arr = np.array([[5,6,7,4,2,8],[1,2,3,4,5,6]])
    # jitni dimension hogi utni loop ke ander loop lage ga taqe access hojae
for i in arr:
    for j in i:
        print(j,end=" ") 
        
for i in arr:
    print(i,end=" ") 

# print by using function
for i in np.nditer(arr):  # print All loop without using n-dimension loop like the first loop in that program
    print(i)

for i in np.nditer(arr,flags=['buffered'] , op_dtypes = ["S"]):
    print(i)
# op_dtypes=["S"]:
# Is argument ke through, aap specify karte hain ki iteration ke dauran elements ko kaunsa data type banaya jaye.
# flags=['buffered'] ki zarurat tab hoti hai jab input aur output data types alag ho, jaise integer to string conversion.
for i in arr:
    print(i.astype("float"))

for i in enumerate(arr): # along with index
    print(i)

for i in np.ndenumerate(arr): # along with exact index
    print(i)