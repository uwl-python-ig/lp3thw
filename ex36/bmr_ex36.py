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
One final question--will you take notes in this book? Yes ('Y') or no ('N')?
            """)
            second = True
        elif choice == "D":
            end("A most unfortunate choice.")
        elif choice == "Y" and second == True:
            print("You know, I really can't blame you. It is handy to take notes in a book. You shall pass on to the second test--the tree!")
            tree()
        elif choice == "N" and second == True:
            print("Most circumspect! Truly reverential of the ToE. Well, OK. Great. Oh, yes--the next test--the tree!")
            tree()
        else:
            end("It would seem that you have not followed the directions for input.")

def tree():
    list = []
    print("""
You are now called upon to demonstrate a knowledge of trees.
The task before you is to name three parts of a tree, and then remember which parts of a tree you have named.
I know that it sounds simple.
But you know, maybe that is fine.
Maybe tests don't really need to be overly difficult.
    """)
    while len(list) < 3:
        list.append(input("Name a part of a tree: "))

    print("""
Now. Which three parts of a tree did you just enter?
Enter them as follows:
1. Start with a left bracket ([)
2. Enter your first and second items in single quotes (''), each followed by a comma and a space
3. Enter your last item in single quotes, followed by a right square bracket (])
4. Hit the 'enter key'
    """)
    memory = input("> ")

    if memory == str(list):
        print("""
Perhaps you just looked back at what you entered in the terminal window.
Oh, well... You passed the test, at any rate!
Maybe tests *should* be at least moderately difficult?
I shall have to check the Recommended Level of Difficulty for Tests Related to the Tome of Excellence (RLoDfTRttToE).
        """)
        ocean()
    else:
        print("Not quite right. Try again from the top!")
        tree()

"""
Lots of improvements could be made to the tree function:
- If it truly is a memory test the entered strings shouldn't be visible in the terminal window
    --it might work like password entry, where strings aren't visible?
- The user has to enter the string with brackets, quotes, and commas because of my lack of ability...
    It should be possible to enter just the words, one at a time or all together with just spaces, etc.
    to compare here, but I haven't taken the time to try something else out.
"""

def ocean():
    end("Seems to be working up to the final function--ocean.")

def end(message):
    print(message, "\nGAME OVER")
    exit(0)

begin()
