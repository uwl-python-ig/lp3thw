# this is exercise 21. it shows how functions can return something
# using the "return" command

# this section creates a simple function that returns the sum
# of two values
def add(a, b): # define our function arguments
    print(f"ADDING {a} + {b}") # define our function output as a string
    return a + b #use return to create our output

# the next lines of code are a repeat of the first chunk of code with
# subtraction, multiplication, and division (no modulo?)
def subtract(a, b):
    print(f"SUBTRACTING {a} - {b}")
    return a - b

def multiply(a, b):
    print(f"MULTIPLY {a} * {b}")
    return a * b

def divide(a, b):
    print(f"DIVIDING {a} / {b}")
    return a / b

# create a string with some "zed talk"
print("Let's do some math with just functions!")

# declare some variables that call the functions for later use in a string
age = add(30, 5)
height = subtract(78, 4)
weight = multiply(90, 2)
iq = divide(100, 2)

# put the variables all together in a string
print(f"Age: {age}, Height: {height}, Weight: {weight}, IQ: {iq}")
