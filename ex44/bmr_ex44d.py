# bmr_ex44d.py
# meant to show all three:
	# implicit inheritance
	# override explicitly
	# alter before or after
# (i'm reordering the methods below to match the order of 
	# kinds of interaction just above)
# ZS: write a comment on each line explaining what it does and whether it's an override or not

class Parent(object): # class definition for class Parent

	def implicit(self): # define method implicit() for class Parent
		print("PARENT implicit()") # here's what the method does

	def override(self): # define method override() for class Parent
		print("PARENT override()") # here's what override() does

	def altered(self): # define method altered() for parent
		print("PARENT altered()") # here's what altered() does

class Child(Parent): # class definition for class Child, class Child is a child or derived class of Parent (Parent is the parent or base class)

	# implicit() defined above ha

	def override(self): # define method override() *differently* for the child class Child
		print("CHILD override()") # here's what override() does for the child class Child

	def altered(self): # define method altered() differently for the child class Child,
		# but note that the method incorporates the operations as they are defined in the base or parent class Parent
		print("CHILD, before PARENT altered()") # here's what altered() does for the child class Child, line 1
		super(Child, self).altered() # here's what altered() does for Child, line 2 -- the method operation as implemented in the parent class Parent
		# hm still don't get this syntax, super seems to have different ways it can be used
		print("CHILD, after PARENT altered()") # here's what altered does for Child, line 3

parent = Parent() # class instantiation for parent, which is an object of class Parent
child = Child() # class instantiation for child [...]

parent.implicit() # call the implicit method for the parent
child.implicit() # call the implicit method, which is defined in the Parent class, for child

parent.override() # call the override method for parent
child.override() # call the override method for child, which is defined differently in the child Child than in the parent Parent

parent.altered() # call the altered method for parent
child.altered() # call the altered method for child, which incorporates the same operations as the altered method for parent 
	# but also does some different things 


