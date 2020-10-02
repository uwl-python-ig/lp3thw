# Assigning integer values to the following variables
cars = 100
space_in_a_car = 4
drivers = 30
passengers = 90

# Cars available minus number of drivers available to drive those cars, equals number of cars unused
cars_not_driven = cars - drivers
# The number of drivers available is equal to the number of cars driven
cars_driven = drivers
# The number of cars driven multiplied by the space in each car is equal to the number of passengers that can be driven
carpool_capacity = cars_driven * space_in_a_car
# The number of passengers divided by the number of cars driven equals the average number of passengers per car
average_passengers_per_car = passengers / cars_driven

print("There are", cars, "cars available.")
print("There are only", drivers, "drivers available.")
print("There will be", cars_not_driven, "empty cars today.")
print("We can transport", carpool_capacity, "people today.")
print("We have", passengers, "to carpool today.")
print("We need to put about", average_passengers_per_car, "in each car.")
