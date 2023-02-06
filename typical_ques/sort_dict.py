dic= {1: 13, 2: 7, 3: 0, 4: 10 }

sorted_dic= {}
sorted_keys = sorted(dic, key=dic.get)

print("Original dictionary: ",dic)
print("Sorted dictionary: ", sorted_dic)
for i in sorted_keys:
    sorted_dic[i] = dic[i]

print(sorted_dic)
