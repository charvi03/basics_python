list = [4, 8, 2, 15, 3]
size = len(list)
temp = list[0]
list[0] = list[size - 1]
list[size - 1] = temp
print(list)
