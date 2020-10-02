# Write a script similar to the last exercise that uses read and argv to read the file you just created.

from sys import argv

script, filename = argv

lamb = open(filename)

print(f"Here is the file you created {filename}:")
print(lamb.read())

lamb.close()
