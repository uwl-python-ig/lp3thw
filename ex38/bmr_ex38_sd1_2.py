ten_things = "Apples Oranges Crows Telephone Light Sugar"

print("Wait there are not 10 things in that list. Let's fix that.")

# Wouldn't really need to pass the ' ' arg to split below because the default separator is whitespace
stuff = ten_things.split(' ')
    # stuff = split(ten_things, ' ')
    # for the string that is the value of the var ten_things, create a list by splitting the string at each instance of ' '
more_stuff = ["Day", "Night", "Song", "Frisbee",
                "Corn", "Banana", "Girl", "Boy"]

# Why use does not equal here? <= seems like a more natural choice...
while len(stuff) <= 10:
    # Here and below we are using the default index for the pop method, which is -1 (the last object in a list)
    next_one = more_stuff.pop()
        # pop(more_stuff, -1)
        # for the list that is the value of the var more_stuff, remove* and return the object at the given index, which is here -1
        # *I checked and it really is removed:
            # >>> bmrList = ['pizza', 'nachos', 'sushi', 'burgers']
            # >>> print(bmrList.pop())
            # burgers
            # >>> print(bmrList)
            # ['pizza', 'nachos', 'sushi']
    print("Adding: ", next_one)
    stuff.append(next_one)
        # append(stuff, next one)
        # For the list that is the value of the var stuff, append the value of the var next one
    print(f"There are {len(stuff)} items now.")

print("There we go: ", stuff)

print("Let's do some things with stuff.")

print(stuff[1])
print(stuff[-1])
print(stuff.pop())
    # remove and print the last (default index -1) object in the list that's the value of var stuff
print(' '.join(stuff))
    # Join the objects that are in the list that is the value of the var stuff, separated with the string separator ' ' to create a string, and print this result
print('#'.join(stuff[3:5]))
    # Join the objects from index position 3 up to but not including index position 5 in the list that is the value of the var stuff
        # separated with the string separator '#' to create a string, and print this result
