
class Creature(object):
    pass

class Unicorn(Creature):

    # associate creature with Grasslands
    appellation = 'a unicorn'
    description = 'a white horse with a single silver horn'
    start = 'The unicorn approaches cautiously and gazes into your eyes'
    success = 1

    # surely would save work to implement in parent class and overwrite as needed here??
    def encounter(self):
        print(f"You encounter {Unicorn.appellation}: {Unicorn.description}")
        print(Unicorn.start)
        print("""
            What do you do? Enter a number:
            1. Gaze back into the unicorn's eyes
            2. Hold out your hand
            3. Run away
        """)
        choice = input("> ")
        if int(choice) == Unicorn.success:
            print("""
                The unicorn says 'I like you. Here, have my horn of silver. 
                I don't need it; I'll grow a new one in spring!'
                Then prances off with a wistful look in his eye.
            """)
            # then the player should 'get' the silver horn...
            pass
        elif int(choice) == 2:
            print("""
                The unicorn bites your hand. It hurts.
                'Oh, sorry, I thought you had some food in your hand,' he says,
                and walks away.
            """)
            pass
        elif int(choice) == 3:
            print("""
                You run away and never see the unicorn again, 
                dropping all of your belongings in the process!
            """)
            # then the player should lose what they have gained
            pass
        # add else to start the process over

class Troll(Creature):

    # associate with mountains
    appellation = 'a troll'
    description = 'a huge, lumbering, stony-faced humanoid with a large nose'
    start = '''Just as you are preparing to walk accross the bridge, 
                the troll jumps out from behind a tree and says "hello!" in a loud voice'''
    success = 2

    def encounter(self):
        print(f"You encounter {Troll.appellation}: {Troll.description}")
        print(Troll.start)
        print("""
            What do you do? Enter a number:
            1. Scream
            2. Say 'hello to you!'
            3. Run away
        """)
        choice = input("> ")
        if int(choice) == Troll.success:
            print("""
                The troll says 'Always a pleasure to meet a kind traveller. 
                Here--you must have this bag of gold. I insist. Spend it on something fun.
                Toodles!' and walks away.
            """)
            # then the player should 'get' the gold...
            pass
        elif int(choice) == 1:
            print("""
                The troll says 'There's really no need to be rude!'
            """)
            # then the player should lose whatever they have gained
            pass
        elif int(choice) == 3:
            print("""
                You run away. 
            """)
            pass
        # add else to start the process over
