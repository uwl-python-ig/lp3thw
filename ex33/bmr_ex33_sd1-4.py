numbers = []
i = 0
limit = 22
inc = 2

def to_limit(i, limit, inc):
    while i < limit:
        print(f"At the top i is {i}")
        numbers.append(i)

        i += inc
        print("Numbers now: ", numbers)
        print(f"At the bottom i is {i}")

    print("The numbers: ")
    for num in numbers:
        print(num)

to_limit(i, limit, inc)
