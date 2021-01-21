class Animal(object):
    def __init__(self, name):
        self.name = name

        self.nearby = None
        # NOTE THAT nearby attribute is NOT GIVEN in the __init__
            # My understanding is that this:
                # Makes the attribute optional
                # Means that we *cannot* set this attribute when we create an instance of the class
            # (My understanding may or may not be correct...)

    def whenNearby(self, nearby):
        if isinstance(self, Cat) == True and self.nearby == None:
            print("I'm going to lounge here in this sunspot.")
        elif isinstance(self, Cat) == True and self.nearby != None:
            print("I'm running away!")
        elif isinstance(self, Dog) == True and self.nearby == None:
            print("Is there any food to eat at the moment??")
        elif isinstance(self, Dog) == True and self.nearby != None:
            print("ATTAAAAAAACK!!!")
        else:
            print(f"""
            I don't really know what to do...
            What kind of animal am I?
            Does it matter whether another animal is nearby??
            All I really know is that my name is {self.name}.
            """)

class Cat(Animal):
    def __init__(self, name):
        super(Cat, self).__init__(name)

class Dog(Animal):
    def __init__(self, name):
        super(Dog, self).__init__(name)

"""
I think that I did what I wanted to do with whenNearby().
From P3 interpreter:

    >>> from bmr_ex42_sd3 import *

    >>> rover = Dog("Rover")
    >>> rover.nearby = "bigCat"
    >>> rover.whenNearby(rover.nearby)
    ATTAAAAAAACK!!!

    >>> webster = Dog("Webster")
    >>> webster.whenNearby(webster.nearby)
    Is there any food to eat at the moment??

    >>> seamus = Cat("Seamus")
    >>> seamus.whenNearby(seamus.nearby)
    I'm going to lounge here in this sunspot.

    >>> kayenta = Cat("Kayenta")
    >>> kayenta.nearby = "bigDog"
    >>> kayenta.whenNearby(kayenta.nearby)
    I'm running away!

The calls for the whenNearby functions for the Dogs and Cats above seem verbose
and I wonder if they could be done in a different way?

    >>> someAnimal = Animal("Chester")
    >>> someAnimal.whenNearby(someAnimal.nearby)

            I don't really know what to do...
            What kind of animal am I?
            Does it matter whether another animal is nearby??
            All I really know is that my name is Chester.
"""
