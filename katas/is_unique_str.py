"""Check whether every character in a string appears once."""


def is_unique_str(text):
    """Returns True when no character appears more than once."""
    seen = set()
    for char in text:
        if char in seen:
            return False
        seen.add(char)
    return True


# Solution 1: sort the word first, then compare neighboring characters.
def is_unique_str_sorted(text):
    sorted_text = sorted(text)

    for i in range(1, len(sorted_text)):
        if sorted_text[i] == sorted_text[i - 1]:
            return False

    return True


# Solution 2: receive a word in random/unsorted order.
# No sorting is used. Each character is compared with all characters after it
# using two nested loops.
def is_unique_str_nested_loops(text):
    for i in range(len(text)):
        for j in range(i + 1, len(text)):
            if text[i] == text[j]:
                return False

    return True


if __name__ == '__main__':
    print(is_unique_str("abc"))  # True
    print(is_unique_str("aab"))  # False

    print(is_unique_str_sorted("cadb"))  # True
    print(is_unique_str_sorted("cadba"))  # False

    print(is_unique_str_nested_loops("cadb"))  # True
    print(is_unique_str_nested_loops("cadba"))  # False
