# This comes in handy
rule = '-' * 20

print("First we'll make a dict and retrieve a value with a key.")

mystuff = {'apple': "I AM APPLES!"}
print(mystuff['apple'])

print(rule)

print("Now we'll do the same thing by importing a function from bmr_ex40_mystuff.py")

import bmr_ex40_mystuff
bmr_ex40_mystuff.apple()

print(rule)

print("Now we'll use the var in bmr_ex40_mystuff.py")
print(bmr_ex40_mystuff.tangerine)

print(rule)

print("So to sum up:")
print("Get apple from the dict:\n", mystuff['apple']) # A ha! The key is a string, so it needs to be in quotes
print("Get apple from the module:")
bmr_ex40_mystuff.apple() # Syntax: parens needed after apple because it's a function
print("Get a var from the module:")
print(bmr_ex40_mystuff.tangerine) # Syntax: no parens needed after tangerine because it's just a variable

    # Also, printing seems to work a little differently for functions and vars from the module?
    # When I put the apple function inside the print function's parens something funny happened...
    # When I tried using module.var outside of the print function nothing happened
