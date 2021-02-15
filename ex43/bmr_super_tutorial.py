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

# Now use inheritance

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
