"""Longest shared prefix of two strings."""


def longest_common_prefix(left, right):
    """
    Returns the longest string that is a prefix of both inputs.
    """
    max_length = min(len(left), len(right))

    for i in range(max_length):
        if left[i] != right[i]:
            return left[:i]

    return left[:max_length]


if __name__ == '__main__':
    print(longest_common_prefix("interspecies", "interstellar"))  # inters
    print(longest_common_prefix("dog", "cat"))                    # empty
