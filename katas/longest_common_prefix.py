"""Longest shared prefix of two strings."""


def longest_common_prefix(left, right):
    str = None
    counter = min(len(left),len(right))
    index = 0
    for i in range(counter):
        if left[i] != right[i]:
            break
        else:
            index += 1
    return left[:index]


if __name__ == '__main__':
    print(longest_common_prefix("interspecies", "interstellar"))  # inters
    print(longest_common_prefix("dog", "cat"))                    # empty
    print(longest_common_prefix("flow","flower"))
