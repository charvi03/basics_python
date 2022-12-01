# adding elmnts
thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}

thisdict.update({"color": "red"})
print(thisdict)
print("the model of car is ", thisdict.get('model'))
