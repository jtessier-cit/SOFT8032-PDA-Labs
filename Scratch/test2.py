import numpy as np

arr = np.array([5.5, 45.6, 3.2], float)
print(arr)

arr1 = np.array([5.5], float)
arr2 = np.append(arr1, 4.3)

print(arr2)

arr1 = np.array([5.5], float)
arr2 = np.append(arr1, [4.3, 6.4, 6])

print(arr2)

arr1 = np.array([5.5, 45.6, 3.2], float)
arr2 = np.array([3.5, 4.1, 8.4], float)
arr3 = np.concatenate((arr1, arr2))
print(arr3)

arr1 = np.array([5.5, 45.6, 3.2], float)
arr2 = np.insert(arr1, 1, 99)
print(arr2)

arr1 = np.array([5.5, 45.6, 3.2], float)
arr2 = np.delete(arr1, 1)
print(arr2)

arr = np.array([5.5, 45.6, 3.2], float)
print(arr)
print(arr[0])
arr[0] = 5
print(arr)

arr = np.array([[1, 2, 3], [4, 5, 6]], float)
print(arr)
print(arr[0, 0])
print(arr[1, 2])
print(arr[0])
print(arr[1])