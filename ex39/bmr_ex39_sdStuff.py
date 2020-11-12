rule = '-' * 20

fi = {}

"""
# For when I want to make the list as I go:
    # Let's create the dictionary on the command line;
    # I don't want to do states/cities so I'll do food/ingredient

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

"""
# For retrieving values:

test = input("Enter the name of a food, and I'll give you an ingredient in it: ")
ingredient = fi.get(test, "Oh, dang, sorry. That food isn't on my list.")
print(ingredient)

print(rule)
"""

print("""OK, let's make another dictionary.
This one will provide names in Japanese for the foods you listed earlier.""")

fej = {}
"""
# For creating the dict in the CLI:

for f, i in list(fi.items()):
    print(f"Here's a food in English: {f}.")
    jpn = input(f"Enter the Japanese word for {f}: ")
    fej[f] = jpn
"""
# For my purposes trying to code below, I'll make it ahead of time:

fej = {
'sushi': '寿司',
'nachos': 'ナチョス',
'pizza': 'ピザ',
'burgers': 'ハンバーガー',
'sammies': 'サンドイッチ',
'oatmeal': 'オーツミール',
}

for eng, jpn in list(fej.items()):
    print(f"English: {eng}")
    print(f"Japanese: {jpn}")

"""
# This does not work
    # The following may be a place to start:
    # https://www.programiz.com/python-programming/methods/dictionary/items

print("OK, now we can list foods in English and Japanese, and ingredients in English:")

for f, i in list(fi.items()):
    print(f"The food {f}, in Japanese, is", fej[fi[f]])

# Traceback (most recent call last):
#  File "bmr_ex39_sdStuff.py", line 53, in <module>
#    print(f"The food {f}, in Japanese, is", fej[fi[f]])
# KeyError: 'rice'
"""

# I'd still like to try something with one key, multiple values
    # 'food': ['ingred1', 'ingred2', 'ingred3']
