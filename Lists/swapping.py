list = [4, 8, 2, 15, 3]
a, b = 2, 4
print("before swap", list)
size = len(list)
temp = list[a]
list[a] = list[b]
list[b] = temp
print("after swap", list)
