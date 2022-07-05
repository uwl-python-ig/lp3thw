

class test_class(object):
# OK seriously will *any* class *ever* not be an object??

	def __init__(self, rating):
		self.rating = rating
		
	def assessRating(self):
		if self.rating == 1:
			print("This test class has received a rating of 1, the best rating possible")
		elif self.rating == 2:
			print("This test class has received a rating of 2, this is the 'middle-of-the-road' rating")
		elif self.rating == 3:
			print("This test class has received a rating of 3, this is unfortunately the worst rating")
		else:
			print("Sorry, rating has been entered incorrectly")

tc = test_class(int(input("Enter a rating between 1 and 3--1 is the best 3 is the worst: ")))

tc.assessRating()

