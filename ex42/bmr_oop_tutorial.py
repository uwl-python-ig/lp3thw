"""
Tutorial from:
https://realpython.com/python3-object-oriented-programming/
"""

class Dog:
# class attribute
# See RE: class attributes below
    species = "Canis familiaris"
    
    # instance attributes
    # See RE: instance attributes below
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    """
    Quick test at this point:

	>>> from bmr_oop_tutorial import *
	>>> fido = Dog("Fido", 2)
	>>> print(fido.name)
	Fido
	>>> print(fido.age)
	2
    """
     
    # instance methods
        
    def speak(self, sound):
        return f"{self.name} barks: {sound}"
    
    # Replace .description() with __str__() - see below
    # def description(self):
        # return f"{self.name} is {self.age} years old"
    
    """
    Another quick test, including some errors in calling instance methods:
    
        >>> from bmr_oop_tutorial import *
	>>> daisy = Dog("Daisy", 4)
	>>> speak(daisy, "RUFF")
	Traceback (most recent call last):
	  File "<stdin>", line 1, in <module>
	NameError: name 'speak' is not defined
	>>> daisy.speak("RUFF RUFF!")
	'Daisy says RUFF RUFF!'
	>>> daisy.description
	<bound method Dog.description of <bmr_oop_tutorial.Dog object at 0x7f2a49f35a90>>
	>>> daisy.description()
	'Daisy is 4 years old'
    """
    # Another 'dunder method'--see RE: dunder methods below
    def __str__(self):
        return f"{self.name} is {self.age} years old"
        
    # I'll be darned!
    	# print(daisy)
    	# Daisy is 4 years old

class Dachshund(Dog):
    pass

class Bulldog(Dog):
    pass

"""
	>>> from bmr_oop_tutorial import *
	>>> miles = JackRussellTerrier("Miles", 4)
	>>> buddy = Dachshund("Buddy", 9)
	>>> jack = Bulldog("Jack", 3)
	>>> jim = Bulldog("Jim", 5)
	>>> miles.species
	'Canis familiaris'
	>>> buddy.name
	'Buddy'
	>>> print(jack)
	Jack is 3 years old
	>>> jim.speak("Woof")
	'Jim says Woof'
	
	**NEW STUFF: built-ins type() and isinstance()**
	
	# I can also use the built-in type()
	>>> type(miles)
	<class 'bmr_oop_tutorial.JackRussellTerrier'>	
	
	# "What if you want to determine if miles is also an instance of the Dog class?
	# You can do this with the built-in isinstance()"
	>>> isinstance(miles, Dog)
	True
"""

class JackRussellTerrier(Dog):
    # To override a method defined on the parent class, you define a method with the same name on the child class
    def speak(self, sound="Arf"):
        # return f"{self.name} says {sound}"
        # You can now call .speak() on a JackRussellTerrier instance without passing an argument to sound
        # BUT instead of specifying the format of the return in the child class, I'll use super()
        return super().speak(sound)

        """
        >>> from bmr_oop_tutorial import *
	>>> miles = JackRussellTerrier("Miles", 4)
	>>> print(miles)
	Miles is 4 years old
	>>> miles.speak # forgot my parens when calling the method!
	<bound method JackRussellTerrier.speak of <bmr_oop_tutorial.JackRussellTerrier object at 0x7f8ab1a4f1f0>>
	
	# Before switching to super() above, L97
	>>> miles.speak()
	'Miles says Arf'
	# you can still call .speak() with a different sound
	>>> miles.speak("Grrr")
	'Miles says Grrr'
	
	# One thing to keep in mind about class inheritance is that changes to the parent class automatically propagate to child classes
	# This occurrs as long as the attribute or method being changed isn't overridden in the child class
	
	# After switching to super() above in L100
	>>> from bmr_oop_tutorial import *
	>>> miles = JackRussellTerrier("Miles", 4)
	>>> miles.speak()
	'Miles barks: Arf'	
        """

# RE: dunder methods, from tutorial
	# Methods like .__init__() and .__str__() are called dunder methods because they begin and end with double underscores
    	# There are many dunder methods that you can use to customize classes in Python
    	# Understanding dunder methods is an important part of mastering [OOP] in Python

# RE: class attributes, from tutorial linked above
	# Class attributes are defined directly beneath the first line of the class name and are indented by four spaces
	# They must always be assigned an initial value
	# When an instance of the class is created, class attributes are automatically created and assigned to their initial values
	# Use class attributes to define properties that should have the same value for every class instance


# RE: instance attributes, from tutorial
	# An instance attribute's value is specific to a particular instance of the class
	# The properties that all Dog objects must have are defined in a method called .__init__()
	# Every time a new Dog object is created, .__init__() sets the initial *state* of the object by assigning the values of the object's properties
	# That is, .__init__() initializes a new instance of the class
	# You can give .__init__() any number of parameters, but the first parameter will always be a variable called self
	# When a new class instance is created, teh instance is automatically passed to the self parameter in .__init__() so that new attributes can be defined on the object

# More on 'self', from tutorial:
	# The Dog class's .__init__() method has three parameters, so why are only two agruments passed to it in the example?
	# When you instantiate a Dog object, Python creates a new instance and passes it to the first parameter of .__init__()
	# This essentially removes the self parameter, so you only need to worry about the name and age parameters

"""
Left off here:
https://realpython.com/python3-object-oriented-programming/#extend-the-functionality-of-a-parent-class
	At:
	"You can access the parent class from inside a method of a child class by using super():"
	I still **don't really understand** super
"""

