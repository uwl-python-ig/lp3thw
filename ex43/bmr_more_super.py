class UberClass(object):
	def __init__(self, description):
		self.description = description
	def tell_print(self):
		print(f"Here is my description:\n{self.description}")
	def tell_return(self):
		return f"Here is my description:\n{self.description}"
"""
TEST:
	>>> from bmr_why_001 import UberClass
	>>> test = UberClass("I am an instance of the UberClass class!!")
	>>> # OK first I'll try calling a method, but forgetting the parens as I so often do
	>>> test.tell_print
	<bound method UberClass.tell_print of <bmr_why_001.UberClass object at 0x7fe7fddcc1f0>>
	>>> # OK now I'll call it the right way
	>>> test.tell_print()
	Here is my description:
	I am an instance of the UberClass class!!
	>>> # Now--will the output be any different when using return?
	>>> test.tell_return()
	'Here is my description:\nI am an instance of the UberClass class!!'
	>>> # It *IS* different...
	>>>
"""

# OK, now to test use of super() per https://realpython.com/python-super/
class SubClass(UberClass):
	def __init__(self, description):
		super().__init__(description)
		# I don't understand *exactly* how this is working...
		# See
			# https://realpython.com/python-super/#super-in-single-inheritance
			# and bmr_super_tutorial.py
		# Line 29 gives me access to all of the methods of the superclass??
			# What if the SubClass had additional init arguments? Would the methods still work?
"""
TEST:
	>>> from bmr_more_super import *
	>>> test2 = SubClass("I am an instance of the SubClass class!!")
	>>> test2.tell_print()
	Here is my description:
	I am an instance of the SubClass class!!
	>>> test2.tell_return()
	'Here is my description:\nI am an instance of the SubClass class!!'
	>>>
"""
