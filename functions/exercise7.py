# declare global variable
message = 'Global Hello'


def greet():
    # declare local variable
    msg = "Local hello"
    print(msg)
    print(message)


greet()
print(message)

