import random
from urllib.request import urlopen
import sys

WORD_URL = "http://learncodethehardway.org/words.txt"
WORDS = []

# BMR1
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
# BMR2
# IF there are two args given in the CLI and the second (the one at position '1' is 'english,'
    # set the PHRASE_FIRST var to boolean true)
if len(sys.argv) == 2 and sys.argv[1] == "english":
    PHRASE_FIRST = True
else:
    # otherwise it's boolean false
    PHRASE_FIRST = False

# ZS: load up the words from the website
# BMR3
# OK here we are doing some stuff--
# use the readlines() method on the data which is retrieved using the urlopen method from urllib.request
for word in urlopen(WORD_URL).readlines():
    # readlines returns a list, and we've said above that WORDS is a list, so for each list item that readlines() gives us,
    # append to the WORDS list, as a string in utf-8 encoding (str()), after stripping leading and trailing whitespace (strip())
    WORDS.append(str(word.strip(), encoding="utf-8"))

# define function 'convert' with arts 'snippet' and 'phrase'
def convert(snippet, phrase):
# There's lots here so I'll comment on chunks individually...

    # BMR4
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
                    # OK I'll look for where snippet gets set...
    class_names = [w.capitalize() for w in
                    random.sample(WORDS, snippet.count("%%%"))]

    # BMR7
    # Setting the values of some other vars here...
        # other_names
            # as for class_names, use the random libs sample function
            # cont the number of '***' in value of var snippet, that is,
                # in a key taken from the PHRASES dict above
            # [?] Why doesn't the value of other_names need to be set as a list??
    other_names = random.sample(WORDS, snippet.count("***"))
    # BMR8
    # Set results var to a list, set param_names var to a list
    results = []
    param_names = []

    # BMR9 stopping commenting here ...
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


# ZS: keep going until they hit CTRL-D
# So essentially an infinite loop; have we seen the use of try up to now?
try:
    while True:
        # BMR5
        # set snippetS to the keys in the PHRASES dict
            # [?] BUT why list()??--because the list() constructor returns a list. That list will the the keys() from the PHRASES dictionary
            # See https://www.programiz.com/python-programming/methods/built-in/list
                # the list takes a single argument, which is an iterable
                # here we create an iterable using the keys() method for dictionaries
                # See https://www.programiz.com/python-programming/methods/dictionary/keys
        snippets = list(PHRASES.keys())
        # OK but this line seems funny to me...
            # This line further acts on the snippets var (shuffles it)
            # So now the order of the list items has been changed
        random.shuffle(snippets)

        # BMR6
        # now to set snippeT
        # OK so snippetS is a list, so for each item (snippet) in the list,
            # set var phrase to the value corresponding with each key
        for snippet in snippets:
            phrase = PHRASES[snippet]
            # So at this point we have snippet = the keys from the PHRASES dict, and phrase = the values

            # Can't find documentation for convert()
                # I'm guessing that it assigns var question as snippet and var answer as phrase...
            question, answer = convert(snippet, phrase)
            if PHRASE_FIRST:
                question, answer = answer, question

            print(question)

            input("> ")
            print(f"ANSWER: {answer}\n\n")
except EOFError:
    print("\nBye")
