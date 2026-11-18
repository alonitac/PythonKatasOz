"""Count the words in a sentence."""


def word_count(sentence):
    """
    Counts how many words are in a sentence.

    Words are separated by whitespace. Repeated spaces, tabs, and newlines
    count as a single break. 

    Args:
        sentence: the text to count

    Returns:
        the number of words. An empty or whitespace-only sentence returns 0.
    """
    raise NotImplementedError("word_count not implemented.")


if __name__ == '__main__':
    print(word_count("hello world"))          # 2
    print(word_count("  one   two three "))   # 3
