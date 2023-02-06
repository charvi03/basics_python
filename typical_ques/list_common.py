# Initialization of list
list1 = [1, 2, 3, 4, 55]
list2 = [2, 3, 90, 22]
# Finding intersection
common_elements = set(list1).intersection(list2)

if common_elements:
    print("True", common_elements, "exist as  common element")
else:
    print("False, no common element")
