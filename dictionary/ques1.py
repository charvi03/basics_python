# a = {}
# a['a'] = 1
# a['b'] = [2, 3, 4]
# print(a)

# b = {}
# print(all(b))

count = {}
count[(1, 2, 4)] = 5
count[(4, 2, 1)] = 7
count[(1, 2)] = 6
count[(4, 2, 1)] = 2
tot = 0
for i in count:
    tot = tot + count[i]
print(len(count) + tot)
