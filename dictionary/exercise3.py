# dict1 = {1: "Mon", 2: "Tue", 3: "Wed"}
# dict2 = {}
# # Given dictionaries
# print("The original dictionary : ", (dict1))
# print("The original dictionary : ", (dict2))
# # Check if dictionary is empty
# print("Is dict1 empty? :", not bool(dict1))
# print("Is dict2 empty? :", not bool(dict2))

# 2nd method

test_dict = {}

# printing original dictionary
print("The original dictionary : " + str(test_dict))

# Check if dictionary is empty using len
res = len(test_dict) == 0

# print result
print("Is dictionary empty ? : " + str(res))
