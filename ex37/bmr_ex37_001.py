
# Attempting to use all of the keywords from the list...
    # and
    # as (in one usage)
    # try (still fuzzy)
    # except (still fuzzy)

from sys import exit as bye

"""
INTERESTING:
All functions to be called must be defined prior to call?
But no...see second_input below...
"""

def multiply(c, d):
    try:
        value = int(c) * int(d)
    except ValueError as ve:
        print("You needed to enter integers, not strings or decimals or whatever other kind of non-compatible values you may have entered.")
        return None
        multiply_input()
        # Note that the following except does not get used, no matter whether strings or decimals are entered...
        # Also, returning to multiply_input doesn't work...
        # Must be because exit is at the end of the try block???
    except TypeError as te:
        # This doesn't seem to get used, regardless of input I've tried so far.
        print("You needed to enter ingegers, not decimals or whatever other kind of numbers you may have just entered.")
        return None
        multiply_input()
    return value
    bye(0)

def multiply_input():
    e = input("Please enter an integer: ")
    f = input("Please enter another integer: ")
    print(multiply(e, f))

def start():
    print("""OK just need you to enter a couple of words.
Please follow the directions...
...or enter 'skip' at the first prompt to move on to the next section.""")
    a = input("Please type 'a couple' and then hit enter: ")
    if a == "skip":
        multiply_input()
    else:
        second_input(a)

def second_input(from_before):
    b = input("Please type 'of words' and then hit enter: ")
    if from_before == "a couple" and b == "of words":
        print("OK thanks for doing that.")
        multiply_input()
    else:
        print(f"""I'm afraid that didn't get entered quite right.
Looks like you entered '{a}' and '{b}'.""")
        bye(0)

start()
