import numpy as np

arr = np.array([1, 2, 3, 4, 5, 6, 7])
arr[5] = 0  # updating
print(arr)
print(arr[1:5])
print(arr[4:])

print(arr[:4])
print(arr[-3:-1])
print(arr[1:5:2])
print(arr[::2])
