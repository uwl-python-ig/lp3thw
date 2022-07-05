#comments from lp3thw

# I start with the usual command line argument handling that you already know.
import sys
script, encoding, error = sys.argv

#I start the main meat of this code in a function conveniently called main.
# This will be called at the end of this script to get things going.
def main(language_file, encoding, errors):
    # The first thing this function does is read one line from the languages file it is given. You have done this before so nothing new here.
    # Just readline as before when dealing with text files.
    line = language_file.readline()

    # This is an if-statement, and it lets you make decisions in your Python code.
    # You can test the truth of a variable and, based on that truth, run a piece of code or not run it.
    # In this case I’m testing whether line has something in it.
    # The readline function will return an empty string when it reaches the end of the file and if line simply tests for this empty string.
    # As long as readline gives us something, this will be true, and the code under will run.
    # When this is false, Python will skip these lines.
    if line:
        # I call a separate function to do the actual printing of this line.
        # This simplifies my code and makes it easier for me to understand it.
        print_line(line, encoding, errors)
        # This looks like I am calling the function inside itself, which seems like it should be illegal to do.
        # There’s no technical reason why I can’t call any function I want right there.
        # If a function is simply a jump to the top where I’ve named it main, then calling this function at the end of itself would . . . jump back to the top and run it again.
        # That would make it loop.
        # The if-statement keeps this function from looping forever.
        return main(language_file, encoding, errors)

# The print_line function does the actual encoding of each line from the languages.txt file.
def print_line(line, encoding, errors):
    # This is a simple stripping of the trailing \n on the line string.
    next_lang = line.strip()
    # I finally take the language I’ve received from the languages.txt file and encode it into the raw bytes.
    # Remember the DBES mnemonic: Decode bytes, encode strings.
    # The next_lang variable is a string, so to get the raw bytes I must call .encode() on it to encode strings.
    # I pass to encode() the encoding I want and how to handle errors.
    raw_bytes = next_lang.encode(encoding, errors=errors)
    # I do the extra step of showing the inverse of line 15 by creating a cooked_string variable from the raw_bytes.
    # raw_bytes is bytes, so I call .decode() on it to get a Python string.
    cooked_string = raw_bytes.decode(encoding, errors=errors)

    # I simply print them both out to show you what they look like.
    print(raw_bytes, "<===>", cooked_string)

# I’m done defining functions, so now I want to open the languages.txt file.
languages = open("languages.txt", encoding="utf-8")

# The end of the script simply runs the main function with all the correct parameters to get everything going and kick-start the loop.
# Remember that this then jumps to where the main function is defined on line 5, and on line 10 main is called again, causing this to keep looping.
# The if line: on line 8 will prevent our loop from going forever.
main(languages, encoding, error)
