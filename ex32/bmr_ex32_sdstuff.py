
the_count = [1, 2, 3, 4, 5]
fruits = ['apples', 'oranges', 'pears', 'apricots']
change = ['\u0061', '\u265E', 97, '\u007B']

"""
Are "i", "n", etc. in ex32 completely arbitrary? I've changed these below to q, r, x
    From the book:
        The var is defined by the for-loop when it starts, initializing it to the current element
        of the loop iteration each time through.
"""

for q in the_count:
    print(f"This is count {q}")

for r in fruits:
    print(f"A fruit of type: {r}")

#ZS writes:
    # "also we can go through mixed lists too
    # notice we have to use {} since we don't know what's in it"
    # I don't get it. We have to use curly brackets because we don't know the datatype of list items?

for x in change:
    print(f"I got {x}")

"""
SD1:
Looking up range():
    https://docs.python.org/release/3.6.9/library/stdtypes.html?highlight=range#range
    is a little over my head.
    OK so there are three args for the range function:
        start, stop, step
        One (stop) is required
    But it seems to me that if you want to use step, you have to specify start,
        otherwise your stop will be interpreted as start and your step will be interpreted as stop...
"""

"""
SD2/3:
Is it possible to eliminate "for n in range[...]" and create the list when assigning the var??
I don't know how I could append the items from my range on the same line as assigning the elements var...
See #1
"""

elements = []

for n in range(0, 3):
    print(f"Adding {n} to the list.")
    elements.append(n)


for n in elements:
    print(f"Element was {n}")
