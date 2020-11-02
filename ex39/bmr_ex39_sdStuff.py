rule = '-' * 20

# Let's create the dictionary on the command line;
    # I don't want to do states/cities so I'll do food/ingredient

# For when I want to make the list as I go:
"""
fi = {}

for n in range(0,5):
    food = input("Enter a food you like: ")
    ingredient = input("Enter an ingredient in that food: ")
    fi[food] = ingredient
"""

# For when I don't:

fi = {
'sushi': 'rice',
'nachos': 'cheese',
'pizza': 'sauce',
'burgers': 'buns',
'sammies': 'bread',
'oatmeal': 'oats'
}

print("From the dictionary you created:", "\n", rule)
for f, i in list(fi.items()):
    print(f"{f} has/have {i} in it/them.")

print(rule)

test = input("Enter the name of a food, and I'll give you an ingredient in it: ")
ingredient = fi.get(test, "Oh, dang, sorry. That food isn't on my list.")
print(ingredient)

print(rule)

"""
print("OK, let's make another dictionary.")

sc = {}

for i in range(0,5):
    state = input("Enter the name of a state: ")
    # ... pick up here.
    # The goal is to create a dict with 'state': ['city', 'city2', 'city3']
    # (as many cities as the user wants to enter)
"""
