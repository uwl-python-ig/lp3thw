#defines function cheese_and_crackers with two variables: cheese_count and boxes_of_crackers
def cheese_and_crackers(cheese_count, boxes_of_crackers):
    # formatted string containing the first variable
    print(f"You have {cheese_count} cheeses!")
    # formatted string containing the second variable
    print(f"You have {boxes_of_crackers} boxes of crackers!")
    # string
    print("Man that's enough for a party!")
    # string with an escape to create a new line
    print("Get a blanket.\n")

print("We can just give the function numbers directly:")
# runs the function with 20 for the first variable and 30 for the second
cheese_and_crackers(20, 30)

print("OR, we can use variable from our script:")
# setting variables
amount_of_cheese = 10
amount_of_crackers = 50

# runs the functions with the first variable as the first variable and the second as the second
cheese_and_crackers(amount_of_cheese, amount_of_crackers)

print("We can even do math inside too:")
# runs the function with 10 + 20 for the first variable and 5 + 6 for the second
cheese_and_crackers(10 + 20, 5 + 6)

print("And we can combine the two, variables and math:")
# runs the function with the first variable + 100 for the first variable, and the second + 1000 for the second
cheese_and_crackers(amount_of_cheese + 100, amount_of_crackers + 1000)
