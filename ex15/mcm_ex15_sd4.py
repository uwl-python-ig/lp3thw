# Get rid of lines 10–15 where you use input and run the script again.

from sys import argv

script, filename = argv

txt = open(filename)

print(f"Here's your file {filename}:")
print(txt.read())
