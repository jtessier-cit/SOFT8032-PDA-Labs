import numpy as np

# use np.zeros to create an array with 12 rows and 3 columns
num_rows = 12
num_cols = 3

arr1 = np.zeros((num_rows, num_cols), dtype=int)

# print out the array
print("\nArray arr1 created as 12 rows and 3 columns ")
print(arr1)

# reshape to 6x6
num_rows = 6
num_cols = 6
arr2 = arr1.reshape((num_rows, num_cols))

print("\nArray arr2 reshaped as 6x6")
print(arr2)