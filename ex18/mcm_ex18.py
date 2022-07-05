# def = define (used to define a function)
# this one is like your scripts with argv
def print_two(*args):
    #print_two is the name of the function
    #*args is the function version of argv
        arg1, arg2 = args
        #unpacks arguments
        print(f"arg1: {arg1}, arg2: {arg2}")
        #all lines indented four spaces after that : (colon) are attached to print_two

# ok, that *args is actually pointless, we can just do this
def print_two_again(arg1, arg2):
    print(f"arg1: {arg1}, arg2: {arg2}")
    #in python we can skip the unpacking of arguments and just use the names we want right inside parentheses

# this just takes one argument
def print_one(arg1):
    print(f"arg1: {arg1}")

#this one takes no arguments
def print_none():
    print("I got nothin'.")

print_two("Zed","Shaw")
print_two_again("Zed","Shaw")
print_one("First!")
print_none()
