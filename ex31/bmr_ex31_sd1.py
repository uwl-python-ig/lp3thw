# Note that I'm getting the indentation that we see in the code in the output.
# How to not get indentation in output?

print("""You enter a dark room with two doors.
Do you go through door #1 or door #2?""")

door = input("> ")

if door == "1":
    print("There's a giant bear here eating a cheese cake.")
    print("What do you do?")
    print("Enter '1' to take the cake.")
    print("Enter '2' to scream at the bear.")
    print("Enter something else if you don't like either option.")

    bear = input("> ")

    if bear == "1":
        print("The bear eats your face off. Good job!")
    elif bear == "2":
        print("The bear eats your legs off. Good job!")
    else:
        print(f"You made a different choice. You chose: {bear}.")
        print("Let's explore the choice that you made a bit further.")
        print(f"""
        So moving forward with {bear}, tell me...
        are you hoping to become friends with the bear, or are you hoping to scare it away?
        Enter '1' if you'd like to become friends with it.
        Enter '2' if you'd like to scare it away.
        """)

        more = input("> ")

        if more == "1":
            print("""
            It just isn't a good idea to try and befriend a bear in this situation. Game over.

            No wait! Okay, another chance.
            Will you, now that you've been given another chance, run?
            Enter 'yes' or 'no'.
            """)

            run = input(">")

            if run == "yes":
                print("I'm glad that you learned something. Well done.")
            elif run == "no":
                print("You haven't learned anything and it now truly is game over.")
            else:
                Print("Does not compute.")
                
        elif bear == "2":
            print(f"""
            Okay, well, it's probably a good idea to try and scare the bear away.
            But let's remember, what you are actually doing in this situation is {bear}.
            It just isn't scary enough. The bear *is not scared*. Game over.
            """)
        else:
            print(f"""
            You've done it. With your brilliant strategy to first {bear},
            and then {more}, you've truly revolutionized bear-human relations.
            At this point the bear is asking you for advice.
            """)

# What I'd like to do is say, "you can either type in some advice, or just hit enter if you don't want to give the bear advice"
# Then have conditions where any input of alphanumeric chars does one thing, and no input does another

elif door == "2":
    print("You stare into the endless abyss at Cthulhu's retina.")
    print("1. Blueberries.")
    print("2. Yellow jacket clothespins.")
    print("3. Understanding revolvers yelling melodies.")

    insanity = input("> ")

    if insanity == "1" or insanity == "2":
        print("Your body survives powered by a mind of jello.")
        print("Good job!")
    else:
        print("The insanity rots your eyes into a pool of muck.")
        print("Good job!")

else:
    print("You stumble around and fall on a knife and die. Good job!")
