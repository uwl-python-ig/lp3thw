#invoking the module argument variables
from sys import argv

#defining argv variables
script, input_file = argv

#defining the function print_all
def print_all(f):
    #this function will print whatever file is put in the variable f
    print(f.read())

#defining the function rewind
def rewind(f):
    #this function will go to line 0 of the file set to variable f (i THINK)
    f.seek(0)

#defining the function print_a_line
def print_a_line(line_count, f):
    #this function will read and print the line number according to variable line_count, for the file set to variable f
    print(line_count, f.readline())

#sets the variable of current_file to the open version of input_file from argv
current_file = open(input_file)

# string with an escape for a new line at the end
print("First let's print the whole file:\n")

#executes function print_all, which opens the input file and prints it
print_all(current_file)

#string
print("Now let's rewind, kind of like a tape.")

#executes function rewind, which goes to line 0 of the open file
rewind(current_file)

#string
print("Let's print three lines:")

#sets variable current_line to 1
current_line = 1
#executes function print_a_line, which will go to the line number of current_line (which is 1), read that line, and print it
print_a_line(current_line, current_file)

#sets variable current_line to current_line (previously established as 1) + 1, making it now 2
current_line = current_line + 1
#executes function print_a_line, which will go to the line number of current_line (which is now 2), read that line, and print it
print_a_line(current_line, current_file)

#sets variable current_line to current_line (previously established as 2) + 1, making it now 3
current_line = current_line + 1
#executes function print_a_line, which will go to the line number of current_line (which is now 3), read that line, and print it
print_a_line(current_line, current_file)
