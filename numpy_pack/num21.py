import numpy as np

arr = np.arange(0, 10)
arr1 = np.arange(20, 30)
t = (arr, arr)
print(t)
print(type(t))
print(np.concatenate((arr, arr1)))
print(np.hstack((arr, arr1)))
print(np.vstack((arr, arr1)))
