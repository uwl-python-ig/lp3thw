people = 10
cars = 10
trucks = 10

if cars > people:
    print("We should take the cars.")
elif cars < people:
    print("We should not take the cars.")
else:
    print("We can't decide.")

if trucks > cars:
    print("That's too many trucks.")
elif trucks < cars:
    print("Maybe we could take the trucks.")
else:
    print("We still can't decide.")

if people > trucks:
    print("Alright, let's just take the trucks.")
else:
    print("Fine, let's stay home then.")

people += 10
trucks += 5

print("\n")

if cars > people and trucks > people:
    print("People are outnumbered by all the vehicle types.")
elif cars < people:
    print("Fewer cars than people. Hm.")
else:
    print("We can't decide.")

if trucks > cars or trucks == cars:
    print("That's a good amount of trucks.")
else:
    print("Fewer trucks than cars.")

if cars < trucks and cars < people:
    print("There just aren't many cars.")
else:
    print("Well there are at least a few cars around here.")

cars += 100
trucks += 30

print("\n")

if cars > people and trucks > people:
    print("People are outnumbered by all the vehicle types.")
elif cars < people:
    print("Fewer cars than people. Hm.")
else:
    print("We can't decide.")

if trucks > cars or trucks == cars:
    print("That's a good amount of trucks.")
else:
    print("Fewer trucks than cars.")

if cars < trucks and cars < people:
    print("There just aren't many cars.")
else:
    print("Well there are at least a few cars around here.")
