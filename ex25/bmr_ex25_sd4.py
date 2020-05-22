def break_words(stuff):
    """This function will break up words for us."""
    words = stuff.split(' ', 4)
    return words

# When used with input "WELL JIMMY TRY SOME BISCUITS FOR GOODNESS' SAKE", break_words() as defined above returned:
    # ['WELL', 'JIMMY', 'TRY', 'SOME', "BISCUITS FOR GOODNESS' SAKE"]
# I was quite curious about why single-, the double-quotes, and if they would cause trouble, but I was able to use sort_words below on the output.

def sort_words(words):
    """Sorts the words."""
    return sorted(words)

# I was unable to use this function with the "True" argument for reverse order.
    # Error: Must use keyword argument for key function
    # But I didn't want to use the key function (which I believe would be specified between the 'iterable' and the reverse boolean), only the reverse option...

def print_first_word(words):
    """Prints the first word after popping it off."""
    word = words.pop(1)
    print(word)

# Shouldn't really be called print_first_word anymore because it pops then prints the second word.

def print_last_word(words):
    """Prints the last word after popping it off."""
    word = words.pop(-2)
    print(word)

# Again, pops then prints next to last word.

def sort_sentence(sentence):
    """Takes in a full sentence and returns the sorted words."""
    words = break_words(sentence)
    return sort_words(words)

def print_first_and_last(sentence):
    """Prints the first and last words of the sentence."""
    words = break_words(sentence)
    print_first_word(words)
    print_last_word(words)

def print_first_and_last_sorted(sentence):
    """Sorts the words then prints the first and last one."""
    words = sort_sentence(sentence)
    print_first_word(words)
    print_last_word(words)
