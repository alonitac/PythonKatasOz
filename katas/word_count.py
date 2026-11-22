"""Count the words in a sentence."""


def word_count(sentence):
    count = 0
    in_word = False
    for i in sentence:
        if i.isalpha():
            in_word = True
            continue
        elif i.isspace():
            if in_word:
                count += 1
                in_word = False
    if in_word:
        count += 1
    return count


if __name__ == '__main__':
    print(word_count("hello world"))          # 2
    print(word_count("  one   two three "))   # 3
