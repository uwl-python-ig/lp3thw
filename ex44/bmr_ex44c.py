# bmr_ex44c.py
# meant to demonstrate how to 'alter before or after'

class Parent(object):

	def altered(self):
		print("PARENT altered()")

class Child(Parent):

	def altered(self):
		print("CHILD, BEFORE PARENT altered()")
		super(Child, self).altered() # SYNTAX - I don't think I've ever seen super() like this?
		print("CHILD, AFTER PARENT altered()")

dad = Parent()
son = Child()

dad.altered()
son.altered()

# ZS explains line 13 as:
	# 'call super with arguments Child and self, 
	# then call the function altered on whatever it returns
	
