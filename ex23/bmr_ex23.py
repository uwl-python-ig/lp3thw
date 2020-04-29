import sys
script, input_encoding, error = sys.argv


def main(language_file, encoding, errors):
    line = language_file.readline()

    if line:
        print_line(line, encoding, errors)
        return main(language_file, encoding, errors)


def print_line(line, encoding, errors):
    next_lang = line.strip()
    raw_bytes = next_lang.encode(encoding, errors=errors)
    cooked_string = raw_bytes.decode(encoding, errors=errors)

    print(raw_bytes, "<===>", cooked_string)


languages = open("languages.txt", encoding="utf-8")

main(languages, input_encoding, error)

# I have so many questions about this script.

# Errors:
    # What are the options for the error var?
        # SEE https://docs.python.org/3.6/library/codecs.html#error-handlers
    # What do these various options do?
    # Where do we see the errors in the output that this script creates in the command line?

# What are all options for encodings?
    # SEE https://docs.python.org/3.6/library/codecs.html#standard-encodings

# My WSL terminal
    # How come it doesn't display Unicode?
    # (For that matter, neither does Atom on W10...)

# And more...
