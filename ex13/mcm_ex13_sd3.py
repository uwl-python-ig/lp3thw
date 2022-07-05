#Combine input with argv to make a script that gets more input from a user

from sys import argv

script, first, second, third = argv

print("The script is called:", script)
input("Is this correct? ")
print("Your first variable is:", first)
input("Is this correct? ")
print("Your second variable is:", second)
input("Is this correct? ")
print("Your third variable is:", third)
