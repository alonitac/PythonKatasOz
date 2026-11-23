"""Count the words in a sentence."""


def word_count(sentence):
    """
    Counts words by looking for the beginning of each word.

    A word begins with a letter at the start of the sentence,
    or with a letter that comes after a space, tab, or newline.
    """
    count = 0

    for i in range(len(sentence)):
        is_letter = (
            "a" <= sentence[i] <= "z"
            or "A" <= sentence[i] <= "Z"
        )

        if is_letter:
            if i == 0:
                count += 1
            elif sentence[i - 1] == " " or sentence[i - 1] == "\t" or sentence[i - 1] == "\n":
                count += 1

    return count


if __name__ == '__main__':
    print(word_count("hello world"))          # 2
    print(word_count("  one   two three "))   # 3
