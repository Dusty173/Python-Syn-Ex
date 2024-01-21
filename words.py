def print_upper_words(list):
    """Takes in a list of words and returns a str of matching words, 
    each on a new line, while also uppercasing each matching word.
        
        >>> print_upper_words(['prints', 'like', 'this'])
        PRINTS
        LIKE
        THIS
    """

    for word in list:
        print(word.upper())


def print_upper_includes_e(list):
    """Takes in a list of words and returns uppercase version of words,
    each on a new line, ONLY IF they start with an 'e' or 'E'.
    
    >>> print_upper_includes_e(['ellen', 'eagle', 'noE'])
    ELLEN
    EAGLE
    EYE
    """
    for word in list:
        if word.startswith('e') or word.startswith('E'):
            print(word.upper())


def print_only_with(list, starts_with):
    """Takes a list of words and only prints any word in the list that starts
    with the value passed into starts_with, uppercased, each on a new line.
    
    >>> print_only_with(['Every', 'even', 'Exactly', 'printed'], starts_with=['E'])
    EVERY
    EXACTLY
    """

    for word in list:
        for letter in starts_with:
            if word.startswith(letter):
                print(word.upper())
                break
                