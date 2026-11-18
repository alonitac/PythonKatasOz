"""Check whether every character in a string appears once."""


def is_unique_str(text):
    chrs = {}
    for ch in text:
        chrs[ch] = chrs.get(ch, 0) + 1
    return not any(occur > 1 for occur in chrs.values() )


if __name__ == '__main__':
    print(is_unique_str("abc"))  # True
    print(is_unique_str("aab"))  # False
