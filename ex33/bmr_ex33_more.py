numbers = []
i = 0
limit = 22
inc = 2

def to_limit(i, limit, inc):
    while i < limit:
        print("Start of 'to_limit' function.")
        print(f"Current 'i' value: {i}")
        # Note that function executes to this point at an i value of 22!
        # Why does it get to here?? It shouldn't execute at all??
        print("Appending current 'i' value to list 'numbers'.")
        numbers.append(i)
        print(f"Current contents of list 'numbers':\n{numbers}.")
        # Interesting that I don't have to convert inc to a string to print--
        print(f"Incrementing 'i' value {i} by value of var 'inc', which is {inc}, to make {i+inc}")
        i += inc
        print(f"Current 'i' value {i}")

to_limit(i, limit, inc)

# Interesting that the below need not be indented
# Perhaps I can just consider that the work above has been done, so the list 'numbers' has been assigned contents
# and the contents will still be there as long as the script is running?
print(f"""I didn't think it'd work to print the list here, but it did!
Two ways.
I can do this:""")
print(numbers)
print("Or I can do this:")
for n in numbers:
    print(n)
