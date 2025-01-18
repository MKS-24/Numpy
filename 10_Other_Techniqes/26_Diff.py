import numpy as np

# Original array
arr = np.array([[1, 2, 3],
                [4, 5, 6],
                [7, 8, 9]])

# Using ravel (returns a view if possible)
raveled_arr = arr.ravel()
raveled_arr[0] = 99  # Modify the flattened array

# Using flatten (always returns a copy)
flattened_arr = arr.flatten()
flattened_arr[0] = 88  # Modify the flattened array

print("Original Array after modifying ravel:")
print(arr)  # Will reflect the change made through ravel

print("\nFlattened Array (Copy):")
print(flattened_arr)  # Independent copy, changes won't reflect in the original

print("\nOriginal Array remains unaffected by flatten:")
print(arr)  # No changes because flatten works on a copy
