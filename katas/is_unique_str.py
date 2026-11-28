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
    letters = {}
    for char in text:
        if char in letters:
            return False
        letters[char] = True
    return True


if __name__ == '__main__':
    print(is_unique_str("abc"))  # True
    print(is_unique_str("aab"))  # False