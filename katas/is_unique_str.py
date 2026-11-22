"""Check whether every character in a string appears once."""


def is_unique_str(text):
    for i in text:
        if text.count(i) > 1:
            return False
    return True

if __name__ == '__main__':
    print(is_unique_str("abc"))  # True
    print(is_unique_str("aab"))  # False
