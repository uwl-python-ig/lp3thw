# One simple English comment above each line

# Invoke the argument variable module
from sys import argv

# Set two variables for argv
script, filename = argv

# Tell the user what is going to happen and ask for their input to confirm or abort
print(f"We're going to erase {filename}.")
print("If you don't want that, hit CTRL-C (^C).")
print("If you do want that, hit RETURN.")

input("?")

# If the user does not abort, it continues and tells the user it is opening the file
print("Opening the file...")
# Not sure what this 'w' is doing
# JK, in the FAQ it says it stands for "open this file in 'write' mode"; without it it goes to default 'read' mode
#I don't get the "target" thing either -- why is it set to open(filename)? Why do subsequent commands use this? Are they essentially saying, like, open(filename).write? Do we need to open it everytime? Isn't it already open? And if not why do we have to close it!!
target = open(filename, 'w')

# Tells the user the file is being deleted
print("Truncating the file. Goodbye!")
target.truncate()

# User import for the three lines in the file
print("Now I'm going to ask you for three lines.")

# Collecting user input
line1 = input("line 1: ")
line2 = input("line 2: ")
line3 = input("line 3: ")

#Telling the user what is happening
print("I'm going to write these to the file.")

# These are writing the user input to the file
target.write(line1)
# These are starting new lines in between each line
target.write("\n")
target.write(line2)
target.write("\n")
target.write(line3)
target.write("\n")

print("And finally, we close it.")
target.close()
