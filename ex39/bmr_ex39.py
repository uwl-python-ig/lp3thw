rule = '-' * 10

# create a mapping of state to abbreviation
states = {
    'Oregon': 'OR',
    'Florida': 'FL',
    'California': 'CA',
    'New York': 'NY',
    'Michigan': 'MI'
}

# create a basic set of states and some cities in them
cities = {
    'CA': 'San Francisco',
    'MI': 'Detroit',
    'FL': 'Jacksonville'
}

# add some more cities
# Syntax used here for adding key + value pairs to dictionaries:
    # dictName['key'] = 'valueForKey'
cities['NY'] = 'New York'
cities['OR'] = 'Portland'

# print out some cities
print(rule)
# Syntax used here for retrieving a value:
    # dictName['key']
print("NY State has: ", cities['NY'])
print("OR State has: ", cities['OR'])

# print some states
print(rule)
print("Michigan's abbreviation is: ", states['Michigan'])
print("Florida's abbreviation is: ", states['Florida'])

# do it using the state then cities dict
print('-' * 10)
# Syntax here for retrieving a value:
    # dictA[keyName needed for dictA may be found as value of --> dictB['key']]
print("Michigan has: ", cities[states['Michigan']])
print("Florida has: ", cities[states['Florida']])

# print every state abbreviation
print(rule)
# syntax below:
    # for <var for keys in dict>, <var for values in dict> in list(<nameOfDict>.items()):
        # print(f"{<var for keys>} is abbreviated {<var for values>}")

# So list() must be a method for dictionaries?
# list is a built-in method in Python:
    # The list() constructor returns a list in Python.
    # The syntax of list() is:
    # list([iterable])
    # iterable (optional) - an object that could be a sequence (string, tuples) or collection (set, dictionary) or any iterator object
    # From : https://www.programiz.com/python-programming/methods/built-in/list

# How about items()?
    # It returns the dictionary's key-value pairs

for state, abbrev in list(states.items()):
    print(f"{state} is abbreviated {abbrev}")

# print every city in state
print(rule)
for abbrev, city in list(cities.items()):
    print(f"{abbrev} has the city {city}")

# now do both at the same time
print(rule)
for state, abbrev in list(states.items()):
    print(f"{state} state is abbreviated {abbrev}")
    print(f"and has city {cities[abbrev]}")

print(rule)
# safely get an abbreviation by state that might not be there
# Another method for dictionaries here--get()
    # get the value of the 'x' item (where x = key name)
state = states.get('Texas')

# if not is a new one on me
if not state:
    print("Sorry, no Texas.")

# get a city with a default value
"""
more on get()
Syntax
    dictionary.get(keyname, value)
Parameter | Description
    keyname | Required. The keyname of the item you want to return the value from
    value | Optional. A value to return if the specified key does not exist. Default value None

https://www.w3schools.com/python/ref_dictionary_get.asp
"""

city = cities.get('TX', 'Does Not Exist')
print(f"The city for the state 'TX' is: {city}'")
