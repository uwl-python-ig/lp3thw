# Keywords from the list:
    # with
    # for
    # print

file = "textFile.txt"
list = []
length = int(input("""First, please enter an integer that is the number of lines you'd like your poem to be.
(You'll write the lines in a moment.)
> """)) + 1

for n in range(0, length - 1):
    item = input(f"Line {n + 1} of your poem: ")
    list.append(item)
    # I fear this won't work. Somehow seems like the var 'item' won't be able to be reassigned as I need here?

print("\nAnd now, your poem:\n")

# I'd like to add something to count and label the poems, so that you could end up
    # with a collection of numbered poems...

with open(file, 'a') as openFile:
    for line in list:
        print(line)
        openFile.write(line + "\n")
    openFile.write("\n\n")

print(f"""\nThanks for playing along!
Don't forget to take a look at {file}, which is in this directory
--you shall find your work there as well!""")

"""
Prior to writing above, found a very simple use example for 'with'
https://www.geeksforgeeks.org/with-statement-in-python/
implemented this example, more or less, as follows:

a = "\nhey here's the text--I'm appending it, because I passed 'write' the 'a' param"

def addAgain(text):
    with open(file, 'a') as openFile:
        openFile.write(text)
addAgain(a)

More notes on 'with':
Per the reference (URL above), the basic structure of the 'with' statement I used here is equal to either of the following:

# 1) without using with statement
file = open('file_path', 'w')
file.write('hello world !')
file.close()

# 2) without using with statement
file = open('file_path', 'w')
try:
    file.write('hello world')
finally:
    file.close()

? So, then, using the 'with' statement, the file is closed when the statement ends?
"""
