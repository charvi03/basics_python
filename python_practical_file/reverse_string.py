name = 'Charvi Khurana'
reverse_str = ""
length = len(name)
for i in range(length - 1, -1, -1):
    reverse_str = reverse_str + name[i]
print("The reverse of given name is ")
print(name, "=", reverse_str)


