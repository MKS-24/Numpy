import numpy as np

dd = np.array([[1,2,3],[1,2,3],[1,2,3]]) # number of colume same hone chahiye

print(dd)
print("Number of Dimentioanal",dd.ndim)   # ndim is for n-dimentional array batata hai

dd = np.array([[[1,2,3],[1,2,3],[1,2,3]]]) # number of colume same hone chahiye
print(dd)
print("Number of Dimentioanal",dd.ndim)

#  ab ager mujhe bht sari dimension print kerni hai tu kya me sab ke liye [[[[[[[[[]]]]]]]]] lagat jao?
#  nh me kuch yu karu ga .array([] , ndmin = (no.of dimension))


dd = np.array([[1,2,3],[1,2,3],[1,2,3]] , ndmin = 10)
print(dd)
print("Number of Dimentioanal",dd.ndim)