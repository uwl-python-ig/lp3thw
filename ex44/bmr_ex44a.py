# ex44a.py
# this is meant to be an example of 'implicit inheritance'

class Parent(object):

	def implicit(self):
		print("PARENT implicit()")

class Child(Parent):
	pass # strange to see a pass statement right under a class def...

dad = Parent()
son = Child()

dad.implicit()
son.implicit()

# === end book exercise ===

class Parent(object):

	def implicit(self):
		print("PARENT implicit()")

class Child(Parent):
	
	def child_method(self):
		print("CHILD child_method()")

dad = Parent()
son = Child()

dad.implicit()
son.implicit()
son.child_method()

# trying some super()

class Food(object):
	def __init__(self, on_tasting):
		self.on_tasting = on_tasting
	
	def reaction(self, on_tasting):
		print(f"I just ate this, and here's my reaction: {on_tasting}")

class Sushi(Food):
	def __init__(self, on_tasting):
		super().__init__(on_tasting)

# don't fully understand what I did with super()
maguro = Sushi(Food) # why don't I pass on_tasting here?
maguro.reaction("DELICIOUS") # I only pass on_tasting when calling reaction method?
# as I say, don't fully understand what I did, and so far LP3THW has not used super()

