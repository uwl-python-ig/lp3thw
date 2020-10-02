# Setting the value for variable types_of_people
types_of_people = 10
# Setting the value for variable x with a formatted string, inserting variable types_of_people
x = f"There are {types_of_people} types of people."

# Setting the value for variable binary
binary = "binary"
# Setting the value for variable do_not
do_not = "don't"
# Setting the value for variable y with a formatted string, inserting variables binary and do_not
y = f"Those who know {binary} and those who {do_not}."

# Display variable x
print(x)
# Display variable y
print(y)
# Display formatted string with variable x
print(f"I said: {x}")
# Display formatted string with variable y
print(f"I also said: '{y}'")

# Setting the value for variable hilarious
hilarious = False
# Setting the value for variable joke_evaluation with an empty format
joke_evaluation = "Isn't that joke so funny?! {}"

# Display variable joke_evaluation, filling in the empty format with variable hilarious
print(joke_evaluation.format(hilarious))

# Setting a value for variable w
w = "This is the left side of ..."
# Setting a value for variable e
e = "a string with a right side."

# Display variable w plus variable e
print(w + e)
