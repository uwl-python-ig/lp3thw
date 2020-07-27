numbers = []

for n in range(0, 23, 2):
    print(f"Now the number is {n}.")
    numbers.append(n)
    print(numbers)

print(f"""Now let's review our final list of numbers once again:
{numbers}""")

"""
SD 5 asks:
Do you need the incrementor in the middle again? What happens if you do not get rid of it?
Well, I'm not really sure how you could cram it back in there...
I mean, as soon as the directions were to use range() I knew I could use the incrementor there...
"""
numz = []

for n in range(0, 23, 2):
    print(f"Current number is {n}.")
    numz.append(n)
    print(numz)
    # This is my attempt to see "[w]hat happens if you do not get rid of [the incrementor]"
    # It seems to do nothing at all, to have no effect...
    # This makes sense to me on some level but not sure I could explain it
    n += 4

print(f"Final list of numbers:\n{numbers}")
