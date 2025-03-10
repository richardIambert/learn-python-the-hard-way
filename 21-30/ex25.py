# ex25.py - Even More Practice


def break_sentence(sentence):
    """Break up a sentence into a list of its words."""
    return sentence.split(" ")


def sort_words(words):
    """Sort a list of words."""
    return sorted(words)


def print_first_word(words):
    """Pops the first word from a list of words and prints it."""
    print(words.pop(0))


def print_last_word(words):
    """Pops the last word from a list of words and prints it."""
    print(words.pop(-1))


def sort_sentence(sentence):
    """Sorts the words of a sentence."""
    return sort_words(break_sentence(sentence))


def print_first_and_last_words(sentence):
    """Prints the first and last words of a sentence."""
    words = break_sentence(sentence)
    print_first_word(words)
    print_last_word(words)


def print_first_and_last_words_sorted(sentence):
    """Prints the first and last words form a sorted sentence."""
    words = sort_sentence(sentence)
    print_first_word(words)
    print_last_word(words)
