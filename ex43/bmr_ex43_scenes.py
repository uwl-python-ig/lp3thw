from random import randint
from textwrap import dedent
from sys import exit

class Scene(object):
    def enter(self):
        print("not yet configured")
        print("subclass it and implement enter()")
        exit(1)

# Child classes Death, CentralCorridor, LaserWeaponArmory, TheBridge, EscapePod
class Death(Scene):

    quips = [
        "The quest is at an end.",
        "I tried my best, but alas...",
        "This did not work out well."
        "Dangit!"
    ]
    
    def enter(self):
        print(Death.quips[randint(0, len(self.quips)-1)])
        exit(1)

class DarkForest(Scene):

    def enter(self):
        print(dedent("""
            You've entered the Dark Forest WyldeWoode in search of adventure.
            You're not entirely sure it was a good idea, but you were pretty
            bored in the village.
            You're walking down the path when a giant spider drops from a tree
            and approaches you. 
            What will you do??
            ('attack', 'run', 'say hello')
            """))
    
        action = input("> ")

        if action == 'attack':
            print(dedent("""
                You run shouting toward the spider and try to punch it in the face.
                But this was a bad idea. It bites you and the world goes dark.
                """))
            return 'death'

        if action == 'run':
            print(dedent("""
                You try to run away but the spider is much faster than you.
                Whether it means to or not, it crushes you beneath its huge weight
                and your vision fades to black.
                """))
            return 'death'
        
        if action == 'say hello':
            print(dedent("""
                The spider says 'oh, yeah, hello! I really appreciate that. 
                Can I help you find your way through the forest?'
                You're thrilled, and you tell them you'd like to see the river.
                """))
            return 'the_river'
        
        else:
            print("that wasn't an option...")
            return 'dark_forest'

class TheRiver(Scene):

    def enter(self):
        print(dedent("""
            You arrive at the river on spider-back and bid farewell to your
            new arachnid friend. No sooner do you turn back to the water than 
            a woman rises from the rushing currents, holding a sword out 
            hilt-first in your direction.
            She looks into your eyes and says:
            'To be worthy of the Sword of Guessing a Number Between One and Ten,
            you must, well, guess the number I'm thinking of. 
            It's between one and ten.
            BUT YOU ONLY HAVE TEN GUESSES!!!'
            Input guesses as numerals ('1', '2', '3', etc.)
            """))
        
        the_number = str(randint(1,10))
        guess = input("> ")
        guesses = 0

        while guess != the_number and guesses < 10:
            print("try again")
            guesses += 1
            guess = input("> ")
        
        if guess == the_number:
            print(dedent("""
                She says to you, 'Well done, wanderer!' and presents the sword to you.
                You think to yourself, 'I'm not really sure why people make such a big
                deal about this forest. I think everyone's pretty nice, really.'
                """))
            return 'finished'
        else:
            print(dedent("""
                She looks in your eyes and says:
                'Oh. Well, I really thought you might be able to guess that...'
                """))
            return 'death'

class Finished(Scene):

    def enter(self):
        print(dedent("""
            You return to the village with a spring in your step and the Sword of 
            Guessing a Number Between One and Ten by your side.
            """))
        return 'finished' # I think this may be significant
