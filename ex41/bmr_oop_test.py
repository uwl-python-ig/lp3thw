import random
from urllib.request import urlopen
import sys

WORD_URL = "http://learncodethehardway.org/words.txt"
WORDS = []

# OK this is a dictionary
PHRASES = {
    "class %%%(%%%):":
        "Make a class names %%% that is-a %%%.",
    "class %%%(object):\n\tdef __init__(self, ***)":
        "class %%% has-a __init__ that takes self and *** params.",
    "class %%%(object):\n\tdef ***(self, @@@)":
        "class %%% has-a function *** that takes self and @@@ params.",
    "*** = %%%()":
        "Set *** to an instance of class %%%.",
    "***.***(@@@)":
        "From *** get the *** function, call it with params self, @@@.",
    "***.*** = '***'":
        "From *** get the *** attribute and set it to '***'."
}

# ZS: do they want to drill phrases first
# IF there are two args given in the CLI and the second (the one at position '1' is 'english,' set the PHRASE_FIRST var to boolean true)
if len(sys.argv) == 2 and sys.argv[1] == "english":
    PHRASE_FIRST = True
else:
    # otherwise it's boolean false
    PHRASE_FIRST = False

# ZS: load up the words from the website
# OK here we are doing some stuff--
# use the readlines() method on the data which is retrieved using the urlopen method from urllib.request
for word in urlopen(WORD_URL).readlines():
    # readlines returns a list, and we've said above that WORDS is a list, so for each list item that readlines() gives us,
    # append to the WORDS list, as a string in utf-8 encoding (str()), after stripping leading and trailing whitespace (strip())
    WORDS.append(str(word.strip(), encoding="utf-8"))

# define function 'convert' with arts 'snippet' and 'phrase'
def convert(snippet, phrase):
# There's lots here so I'll comment on chunks individually...

    # set var class_names
        # var class_names is a list, made up of
            # a *certain number of* items (w) in WORDS
            # capitalized (capitalize())
            # This *certain number of* items from WORDS is generated using the sample method from the random library
                # it is a random sample taken from WORDS (set above)
                # the number to take and put in the list should be equal to the number of %%%
    # QUESTIONS about setting class_names var:
            # [?] what does the 'for' do here? Why not just w.capitalize in random.sample...?
            # Args for the sample method (https://docs.python.org/3.6/library/random.html#random.sample) include:
                # population: first arg, this is WORDS, I get this
                # length of list of elements chosen from population sequence or set: second arg, I don't get this,
                    # because I don't understand exactly what the var snippet is at this point...

    class_names = [w.capitalize() for w in
                    random.sample(WORDS, snippet.count("%%%"))]
    other_names = random.sample(WORDS, snippet.count("***"))
    results = []
    param_names = []

    for i in range(0, snippet.count("@@@")):
        param_count = random.randint(1,3)
        param_names.append(', '.join(
            random.sample(WORDS, param_count)))

    for sentence in snippet, phrase:
        # What does syntax[:] mean?
        result = sentence[:]

        # fake class names
        for word in class_names:
            result = result.replace("%%%", word, 1)

        # fake other names
        for word in other_names:
            result = result.replace("***", word, 1)

        # fake parameter lists
        for word in param_names:
            result = result.replace("@@@", word, 1)

        results.append(result)

    return results


# keep going until they hit CTRL-D
try:
    while True:
        snippets = list(PHRASES.keys())
        random.shuffle(snippets)

        for snippet in snippets:
            phrase = PHRASES[snippet]
            question, answer = convert(snippet, phrase)
            if PHRASE_FIRST:
                question, answer = answer, question

            print(question)

            input("> ")
            print(f"ANSWER: {answer}\n\n")
except EOFError:
    print("\nBye")
