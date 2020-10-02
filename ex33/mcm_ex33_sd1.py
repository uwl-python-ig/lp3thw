numbers  = []

def counting(max_num):
    i = 0
    while i < max_num:
        print(f"At the top i is {i}")
        numbers.append(i)

        i = i + 1
        print("Numbers now: ", numbers)
        print(f"At the bottom i is {i}")

counting(6)

print("The numbers: ")

for num in numbers:
    print(num)
