# Python3 program to Convert a
# list to dictionary

def Convert(lst):
    res_dct = {lst[i]: lst[i + 1] for i in range(0, len(lst), 2)}
    return res_dct


# Driver code
lst = ['a', 1, 'b', 2, 'c', 3]
print(Convert(lst))
