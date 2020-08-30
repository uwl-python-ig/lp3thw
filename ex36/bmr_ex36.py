"""
The Tome of Excellence
"""

from sys import exit

def begin():
    print("""
After much reading and study, you have been gifted with the Tome of Excellence (ToE) by the Council of Gifting of the Tome of Excellence (CoGotToE).
This is Excellent!
But don't get to excited.
You will be thrice tested, each test having three parts.
The book is in your hands.
The Tests of the Tome of Excellence (TotToE) shall begin!
    """)
    tome()

def tome():
    print("What will you do first? Will you open the tome (enter 'A'), or closely inspect the cover and binding (enter 'B')?")
    first = False
    second = False

    while True:
        choice = input("> ")

        if choice == "B":
            print("""
You are a most circumspect afficionado of tomes.
This is clearly stated as a requirement in the CoGotToE's Rules for Opening the Tome of Excellence (RfOtToE).
Wonderful. Now, you sense that the book may be opened.
Will you gently open to the title page (enter 'C'), or will you peer into the mid-text-block (enter 'D')?
            """)
            first = True
        elif choice == "A":
            end("A most unfortunate choice.")
        elif choice == "C" and first == True:
            print("""
You are indeed One who Appreciates the Tome of Excellence (OwAtToE).
One final question--will you take notes in this book? Yes ('E') or no ('F')?
            """)
            second = True
        elif choice == "D":
            end("A most unfortunate choice.")
        elif choice == "E" and second == True:
            print("You know, I really can't blame you. It is handy to take notes in a book. You shall pass on to the second test--the tree!")
            tree()
        elif choice == "F" and second == True:
            print("Most circumspect! Truly reverential of the ToE. Well, OK. Great. Oh, yes--the next test--the tree!")
            tree()
        else:
            end("It would seem that you have not followed the directions for input.")

def tree():
    print("Test ex36 up to this point.")
    # The plan for the next two three-part tests is to see if I can find a different way to structure each than the method used above.
    # What might work? String more functions together? What else??
    # Note that above I ONLY used if statements. I don't think this is a good thing...
    exit(0)

def end(message):
    print(message, "\nGAME OVER")
    exit(0)

begin()
