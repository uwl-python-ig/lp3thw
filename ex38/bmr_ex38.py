ten_things = "Apples Oranges Crows Telephone Light Sugar"

print("Wait there are not 10 things in that list. Let's fix that.")

# Wouldn't really need to pass the ' ' arg to split below because the default separator is whitespace
stuff = ten_things.split(' ')
more_stuff = ["Day", "Night", "Song", "Frisbee",
                "Corn", "Banana", "Girl", "Boy"]

while len(stuff) != 10:
    # Here and below we are using the default index for the pop method, which is -1 (the last object in a list)
    next_one = more_stuff.pop()
    print("Adding: ", next_one)
    stuff.append(next_one)
    print(f"There are {len(stuff)} items now.")

print("There we go: ", stuff)

print("Let's do some things with stuff.")

print(stuff[1])
print(stuff[-1])
print(stuff.pop())
# the join string method is new on me I think... details below
print(' '.join(stuff))
# Note that 3:5 below indicates objects from index 3 (the fourth item in the list) up to *but not including* at index 5
print('#'.join(stuff[3:5]))

# join string method from https://www.programiz.com/python-programming/methods/string/join
    # "returns a string by joining all the elements of an iterable, separated by a string separator"
    # A ha! This explains the syntax, which looked funny to me:
        # It joins each element of an iterable [...] by a string separator (the string on which the join() method is called)
