thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964,
}
# print
print(thisdict)
# acess item using key
print(thisdict["brand"])
x = thisdict.get("model")
print(x)
# using key
y = thisdict.keys()
print(y)
# using values
z = thisdict.values()
print(z)
# length of dict
print(len(thisdict))
