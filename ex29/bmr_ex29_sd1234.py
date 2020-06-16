people = 20
cats = 30
dogs = 15


if people < cats:
    print("Too many cats! The world is doomed!")

if people > cats:
    print("Not many cats! The world is saved!")

if people != cats:
    print("People are NOT cats, obviously.")

if people < dogs:
    print("The world is drooled on!")

if people > dogs:
    print("The world is dry!")

print("\nHere we go again:\n")

dogs += 5

if people >= dogs:
    print("People are greater than or equal to dogs.")

if people <= dogs:
    print("People are less than or equal to dogs.")

if people == dogs:
    print("People are dogs.")

print("\nAnd again:\n")
people += 20

if people < cats:
    print("Too many cats! The world is doomed!")

if people > cats:
    print("Not many cats! The world is saved!")

if people != cats:
    print("People are NOT cats, obviously.")

if people < dogs:
    print("The world is drooled on!")

if people > dogs:
    print("The world is dry!")

if people >= dogs:
    print("People are greater than or equal to dogs.")

if people <= dogs:
    print("People are less than or equal to dogs.")

if people == dogs:
    print("People are dogs.")

if people != dogs:
    print("People are not dogs; there are pros and cons.")

"""
Study drill questions:
1. IF the statement following "if" evaluates as boolean True, the indented code underneath runs.

2. Because those are the rules?
This is similar to defining a function, where lines following the first line
    including def and args are indented by four spaces.
So I'll say that they need to be indented because the indented lines of code are dependent
    on the line above.

3. (Testing with all lines dedented)
Python throws an error:
    File "bmr_ex29_sd1234.py", line 7
        print("Too many cats! The world is doomed!")
            ^
            IndentationError: expected an indented block

 4, 5. See above
"""
