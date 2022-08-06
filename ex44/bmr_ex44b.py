# bmr_ex44b.py
# meant to demonstrate how to 'override explicitly'
# [...] you want to override the function in the child [...]
# [...] just define a function with the same name in Child

class Parent(object):
	
	def override(self):
		print("PARENT override()")

class Child(Parent):

	def override(self):
		print("CHILD override()")

dad = Parent()
son = Child()

dad.override()
son.override()

# === end book exercise ===

class Food(object):
	def __init__(self, on_tasting):
		self.on_tasting = on_tasting
		
	def reaction(on_tasting):
		print(f"I'll tell you what I think of this FOOD: {on_tasting}")

class Sushi(Food):
	def __init__(self, on_tasting):
		super().__init__(on_tasting)

	def reaction(on_tasting):
		print(f"I'll tell you what I think of this SUSHI: {on_tasting}")

sandwich = Food("pretty good")
sandwich.reaction()
maguro = Sushi("delicious")
maguro.reaction()

# interesting output, which proves I don't really know what I'm doing:
"""
I'll tell you what I think of this FOOD: <__main__.Food object at 0x7f1d477cabb0>
I'll tell you what I think of this SUSHI: <__main__.Sushi object at 0x7f1d47774ee0>
"""


