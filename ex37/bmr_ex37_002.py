# Keywords from the list:
    # with

# to add next:
    # use a list, a range, etc., to add to the file

"""
Found a very simple use example for 'with'
https://www.geeksforgeeks.org/with-statement-in-python/
"""
a = "\nhey here's the text--I'm appending it, because I passed 'write' the 'a' param"
file = 'textFile.txt'

def addAgain(text):
    with open(file, 'a') as openFile:
        openFile.write(text)

addAgain(a)

"""
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
