k = 0
rows = 4
for i in range(1, 4 + 1):
    for j in range(1, 4 - i + 1):
        print(end="  ")
    """for k in range(0, i + 1):
        print("*", end=" ")
    print()"""
    while k != (2 * i - 1):
        print("* ", end="")
        k += 1
    k = 0
    print()
