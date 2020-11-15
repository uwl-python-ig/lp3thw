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
