total = 0  # This is global variable.


def sum(arg1, arg2):  # Function definition is here

    total = arg1 + arg2 # Add both the parameters and return   them.“
    # Here total is local variable.
    print("Inside the function local total : ", total)


sum(10, 20);  # Now you can call sum function

print("Outside the function global total : ", total)
