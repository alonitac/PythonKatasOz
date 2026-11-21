"""Check whether every character in a string appears once."""


def is_unique_str(text):
    """
    Returns True when no character appears more than once.

    Comparison is case-sensitive, so "A" and "a" are different characters.
    An empty string is unique.

    Args:
        text: the string to check

    Returns:
        True if every character is unique, otherwise False
    """
   
    letters_dict = {}
    for letter in text:
        if letter in letters_dict:
            return False
        letters_dict[letter] = True
    return True


if __name__ == '__main__':
    print(is_unique_str("abc"))  # True
    print(is_unique_str("aab"))  # False
