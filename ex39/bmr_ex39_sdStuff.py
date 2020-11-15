rule = '-' * 20


# For when I want to make the list as I go:
    # Let's create the dictionary on the command line;
    # I don't want to do states/cities so I'll do food/ingredient
wfl = {}
for n in range(0,3):
    word = input("Enter a word: ")
    firstLetter = input("Enter the first letter (lowercase) in that word: ")
    # Below I use a "subscript operator" to add a key/value:
        # dict_name[key_name] = key_value
    wfl[word] = firstLetter

print(rule)

print("Here's the dictionary you created:")
# Below I use the items() method to retrieve the key and corresponding value at the same time
    # See https://docs.python.org/3.6/tutorial/datastructures.html#looping-techniques
for key, value in list(wfl.items()):
    print(f"{key}: {value}")

print(rule)

# Retrieving values for a given key

test = input("Enter a word in the dictionary, and I'll return the letter it starts with: ")
# "The method get() returns a value for the given key. If key is not available then returns default method None."
letter = wfl.get(test, "That word isn't in the dictionary.")
print(letter)

print(rule)

# -----
# Q/To-do: Could I retrieve the key for a given value?
# ----

# Create a related list
wll = {}
for key, value in list(wfl.items()):
    print(f"Here's a word in the dictionary you created: {key}.")
    ll = input(f"Enter the last letter in that word: ")
    wll[key] = ll

print(rule)

print("Here's your second dictionary:")
for key, value in list(wll.items()):
    print(f"{key}: {value}")

print(rule)

print("Let's see here... Can I list as word / first letter / last letter?")

for key, value in list(wfl.items()):
    print(f"{key} / {value} / {wll[key]}")

print("Yes, that worked.")

print(rule)

print("Some review on dictionary methods. We'll use the second dictionary for this.")
print(f"print wll.keys(): -->", wll.keys(), "<--")
print(f"print wll.values(): -->", wll.values(), "<--")

print("Now let's see if I can get keys from values.")

ll = input("Enter the last letter of a word in the dictionaries:")
# This actually works! Do I *fully* understand this...?...?
    # Interesting to note, with multiple matches, the first matching key is used
print(list(wll.keys())[list(wll.values()).index(ll)])
