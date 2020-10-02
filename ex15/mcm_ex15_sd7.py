# Have your script also call close() on the txt and txt_again variables. It’s important to close files when you are done with them.

from sys import argv

script, filename = argv

txt = open(filename)

print(f"Here's your file {filename}:")
print(txt.read())

print("Type the filename again to close the file:")
file_again = input("> ")

txt_again = open(file_again)

txt_again.close()
