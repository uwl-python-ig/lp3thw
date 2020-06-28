print("""
This is the BMR game.
It's to do with kinds of pizza that are available to humans for consumption.
Okay, we have to start with a choice--do you want regular crust or whole-wheat crust?
Enter "1" for regular and "2" for whole-wheat:
""")

crust = input("> ")

if crust == "2":
    print("I'm sorry, but that is ABSOLUTELY the wrong answer and this game is now over.")

elif crust == "1":
    print(f"""
    Okay, since you entered {crust}, you are obviously a one who appreciates pizza.
    I will deign to entreat with you.
    We shall discuss pizza further.

    Tell me, would you care for olives to be on the pizza?
    Enter "yes" or "no".
    """)

    olives = input("> ")

    if olives == "yes":
        print("That's great, I like olives as well.")
        print("Tell me, do you prefer green or black?")
        print("Enter \"green\" or \"black\".")

        noMatter = input("> ")

        print(f"""Well that's great that you prefer {noMatter},
        but to be honest it really doesn't matter.""")

    elif olives == "no":
        print("I find that my enthusiasm for discussing pizza with you has cooled somewhat...")

else:
    print(f"""
    Okay, well, you didn't enter either \"1\" or \"2\"...
    You just entered {crust}.
    Soooo... I'm out!""")
