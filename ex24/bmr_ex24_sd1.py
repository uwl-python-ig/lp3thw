# Just some printing with escape characters in the three lines below
print("Let's practice everything.")
print('You\'d need to know \'bout escapes with \\ that do:')
print('\n newlines and \t tabs.')

# creating var 'poem' with a multi-line string (""") value
poem = """
\tThe lovely world
with logic so firmly planted
cannot discern \n the needs of love
nor comprehend passion from intuition
and requires an explanation
\n\t\twhere there is none.
"""

# more printing!
print("--------------")
print(poem)
print("--------------")

# create var 'five' that will be the result of some mathematical operations
five = 10 - 2 + 3 - 6
# printing a formatted string
print(f"This should be five: {five}")

# create function 'secret_formula', which takes one argument and returns three things
def secret_formula(started):
    jelly_beans = started * 500
    jars = jelly_beans / 1000
    crates = jars / 100
    return jelly_beans, jars, crates

# creating a var to use as an argument for the function defined above
start_point = 10000
# here's the tricky part in my opinion:
    # I DON'T UNDERSTAND WHY HAVE TO DO THIS
beans, jars, crates = secret_formula(start_point)
# Once I figure it out I can write it here:
# I still don't understand totally... but even though this line seems circular/redundant to me
    # it seems like the only way we can 'get' our return from the function
    # But wait--it ISN'T the only way! Because look below!!

# remember that this is another way to format a string
print("With a starting point of: {}".format(start_point))
# it's just like with an f"" string
print(f"We'd have {beans} beans, {jars} jars, and {crates} crates.")

start_point = start_point / 10

print("We can also do that this way:")
formula = secret_formula(start_point)
# this is an easy way to apply a list to a format string
print("We'd have {} beans, {} jars, and {} crates.".format(*formula))
