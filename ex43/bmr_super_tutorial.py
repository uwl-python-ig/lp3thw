"""
From:
https://realpython.com/python-super/
"""

# Making object explicit when defining simple classes per ZS
class Rectangle(object):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

    def perimeter(self):
        # Just noted that I would have entered this as return 2 * self.length + self.width
        # That wouldn't work...
            # >>> 2 * 2 + 2
            # 6
        return 2 * self.length + 2 * self.width

"""
First, define class Square without using super()

class Square(object):
    def __init__(self, length):
        self.length = length

    def area(self):
        return self.length * self.length

    def perimeter(self):
        return 4 * self.length

"""

"""
# Now use inheritance
# Examples below call super() with no params, see farther down for calling it *with* params

class Square(Rectangle):
    def __init__(self, length):
        super().__init__(length, length)
        # "[...] you've used super() to call the __init__() of the Rectangle class,
        # allowing you to use it in the Square class without repeating code.
        # [...] the core functionality remains after making changes."

# "In the example below, you will create a class Cube that inherits from Square and extends the functionality of .area()
# (inherited from the Rectangle class through Square) to calculate the surface area and volume of a Cube instance

class Cube(Square):
    # No __init__ method here...
    # "Also notice that the Cube class definition does not have an .__init__(). Because Cube inherits from Square and .__init__() doesn’t really do anything differently for Cube than it already does for Square, you can skip defining it, and the .__init__() of the superclass (Square) will be called automatically."
    def surface_area(self):
        face_area = super().area()
        return face_area * 6
    def volume(self):
        face_area = super().area()
        return face_area * self.length
"""
# A ha! Now we are getting to the way that super() is called in LP3THW--with params:
    # "super() can also take two parameters: the first is the subclass, and the second parameter is an object that is an instance of that subclass."

class Square(Rectangle):
    def __init__(self, length):
        super(Square, self).__init__(length, length)

class Cube(Square):

    def surface_area(self):
        face_area = super(Square, self).area()
        return face_area * 6

    def volume(self):
        face_area = super(Square, self).area()
        return face_area * self.length

# "In this example, you are setting Square as the subclass argument to super(), instead of Cube.
# This causes super() to start searching for a matching method (in this case, .area()) at one level above Square in the instance hierarchy, in this case Rectangle.
# In this specific example, the behavior doesn’t change. But imagine that Square also implemented an .area() function that you wanted to make sure Cube did not use.
# Calling super() in this way allows you to do that."

# OK...but this is confusing to me...A ha!
    # "The parameterless call to super() is recommended and sufficient for most use cases,
    # and needing to change the search hierarchy regularly could be indicative of a larger design issue."

# But also:
    # "By including an instantiated object, super() returns a bound method: a method that is bound to the object, which gives the method the object’s context such as any instance attributes.
    # If this parameter is not included, the method returned is just a function, unassociated with an object’s context."

# MULTIPLE INHERITANCE STUFF

class Triangle(object):

    def __init__(self, base, height):
        self.base = base
        self.height = height

    def area(self):
        return 0.5 * self.base * self.height

class RightPyramid(Square, Triangle):
    def __init__(self, base, slant_height):
        self.base = base
        self.slant_height = slant_height
        super().__init__(self.base)

    def area(self):
        base_area = super().area()
        perimeter = super().perimeter()
        return 0.5 * perimeter * self.slant_height + base_area
"""
    TEST
        >>> from bmr_super_tutorial import *
        >>> pyramid = RightPyramid(2, 4)
        >>> RightPyramid.__mro__
        (<class 'bmr_super_tutorial.RightPyramid'>, <class 'bmr_super_tutorial.Square'>, <class 'bmr_super_tutorial.Rectangle'>, <class 'bmr_super_tutorial.Triangle'>, <class 'object'>)
        >>> pyramid.area()
        20.0
"""
# TAKEAWAY: I'm not ready for multiple inheritance
