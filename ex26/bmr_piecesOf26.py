
people = 20
cats = 30
dogs = 15

# Interesting thing here...
    # Unlike in whatever that example was from the PyMARC class,
    # HERE even when the first condition is met the remaining conditions are evaluated
    # I suppose this is because these are all independent if statements, not multiple conditions that are part of a single loop??

if people < cats:
    print("Too many cats! The world is doomed!")

if people < cats:
    print("Not many cats! The world is saved!")

if people < dogs:
    print("The world is drooled on!")

if people > dogs:
    print("The world is dry!")


dogs += 5

if people >= dogs:
    print("People are greater than or equal to dogs.")

if people <= dogs:
    print("People are less than or equal to dogs.")


if people == dogs:
    print("People are dogs.")
