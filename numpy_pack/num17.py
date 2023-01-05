import numpy as np

arr = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
slice_ar = arr[0:5]
print(slice_ar)
slice_ar[:]=55
print(slice_ar)
