def findremainder(arr, lens, n):
    mul = 1
    # find the individual remainder
    for i in range(lens):
        mul = (mul * (arr[i] % n)) % n
    return mul % n


# Driven code
arr = [100, 1, 2, 3, 4, 5, 6, 6, 7]
lens = len(arr)
n = 11
print("Output is ", findremainder(arr, lens, n))
