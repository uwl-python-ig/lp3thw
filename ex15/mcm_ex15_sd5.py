# Use only input and try the script that way. Why is one way of getting the filename better than another?

print("Type the filename:")
filename = input("> ")

txt = open(filename)

print(f"Here's your file {filename}:")
print(txt.read())
