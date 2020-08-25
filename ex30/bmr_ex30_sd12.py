people = 30
cars = 40
trucks = 15

if cars > people:
    print("We should take the cars.")
elif cars < people:
    print("We should not take the cars.")
else:
    print("We can't decide.")

if trucks > cars:
    print("That's too many trucks.")
elif trucks < cars:
    print("Maybe we could take the trucks.")
else:
    print("We still can't decide.")

if people > trucks:
    print("Alright, let's just take the trucks.")
else:
    print("Fine, let's stay home then.")

people += 10
trucks += 25

# Here and below--how to not have to repeat the code block?
    # Can if/elif/else be defined in a function?

print("\n")

if cars > people:
    print("We should take the cars.")
elif cars < people:
    print("We should not take the cars.")
else:
    print("We can't decide.")

if trucks > cars:
    print("That's too many trucks.")
elif trucks < cars:
    print("Maybe we could take the trucks.")
else:
    print("We still can't decide.")

if people > trucks:
    print("Alright, let's just take the trucks.")
else:
    print("Fine, let's stay home then.")

"""
1. From docs.python.org/3.6/tutorial/controlflow.html:

    Perhaps the most well-known statement type is the if statement [...]
    There can be zero or more elif parts, and the else part is optional.
    The keyword 'elif' is short for 'else if', and is useful to avoid excessive
    indentation. An if ... elif ... elif ... sequence is a substitute for the switch
    or case statements found in other languages.

My question is, in cases where more than one if/elif might apply, what happens once a condition is met?
"""
print("\n")

people = 10
frogs = 10

if frogs == people:
    print("frogs equals people.")
elif frogs >= people:
    print("frogs are greater than or equal to people.")
elif frogs <= people:
    print("frogs are less than or equal to people")
else:
    print("finally, people have the upper hand with frogs (whew).")

people += 5

print("\n")

if frogs == people:
    print("frogs equals people.")
elif frogs >= people:
    print("frogs are greater than or equal to people.")
elif frogs <= people:
    print("frogs are less than or equal to people")
else:
    print("finally, people have the upper hand with frogs (whew).")

"""
An answer to my question:
Once a condition is met in an if/elif/else block, the rest of the block is ignored!
"""
