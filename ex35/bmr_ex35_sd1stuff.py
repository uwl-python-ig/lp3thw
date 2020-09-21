from sys import exit

def gold_room():
    print("""
This room is full of gold.
Will you solve the riddle of the gold?
If I ask you whether you desire the gold, will you say yes or no?""")
    solved = False

    while True:
        choice2 = input("> ")

        if choice2 == "yes" and solved == False:
            print("Well at least you are honest. Now, will you take a few pieces of gold to pay the the bills?")
            solved = True
        elif choice2 == "yes" and solved == True:
            print("And why not? Yes, there you are. Now go on your way.")
            exit(0)
        elif choice2 == "no":
            print("C'mon--who are you kidding!?")
            exit(0)
        else:
            print("I don't get what you are saying.")

def bear_room():
    print("There is a bear here.")
    print("The bear has a bunch of honey.")
    print("The fat bear is in front of another door.")
    print("How are you going to move the bear?")
    bear_moved = False

    while True:
        choice = input("> ")

        if choice == "take honey":
            dead("The bear looks at you and then slaps your face off.")
        elif choice == "taunt bear" and not bear_moved:
            print("The bear has moved from the door.")
            print("You can go through it now.")
            bear_moved = True
        elif choice == "open door" and bear_moved:
            gold_room()
        elif choice == "taunt bear" and bear_moved:
            dead("The bear gets angry and chews your leg off.")
        elif choice == "something else" and bear_moved:
            print("Well, you blew it. The bear is back in front of the door now.")
            bear_moved = False
        else:
            print("I got no idea what that means.")

        # I tried putting this comment in the middle of the if/elif/else statements and it caused errors
        """ NOTE on in these if/elif statements:
            Here we are using:
                `and bear_moved` / `and not bear_moved`
            But I believe that we could also use:
                `and bear_moved = True` / `and bear_moved = False` """

def dead(why):
    print(why, "Good job!")
    exit(0)

def start():
    print("You are in the 'bear_room.'")
    bear_room()

start()
