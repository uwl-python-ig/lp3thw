# Above each line, comment out in English what that line does.

# Invoking the argument variable module
from sys import argv

# Setting our variables (the values of which are entered in the command line)
script, filename = argv

# Sets the variable "txt" to the "open" command, which opens the argv variable "filename" which the user entered in the command line
txt = open(filename)

# Prints the filename for the reader before printing out the contents of the file using the "read" command
print(f"Here's your file {filename}:")
print(txt.read())

# Asks for input from the user for the name of the file
print("Type the filename again:")
# Sets the user's input to the variable file_again
file_again = input("> ")

# Sets the variable txt_again to the open command with the variable file_again, which is the user's input
txt_again = open(file_again)

# Prints out the text of the user input file using the "read" function
print(txt_again.read())
