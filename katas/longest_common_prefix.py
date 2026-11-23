"""Longest shared prefix of two strings."""


def longest_common_prefix(left, right):
    """
    Returns the longest string that is a prefix of both inputs.

    Comparison is case-sensitive. When the strings share nothing, or either
    argument is empty, the result is an empty string.

    Args:
        left: first string
        right: second string

    Returns:
        the shared prefix

    Example:
        longest_common_prefix("interspecies", "interstellar") -> "inters"
    """

    index=0
    while index< min(len(left),len(right)) and left[index] == right[index] :
        index += 1

    return left[:index]

if __name__ == '__main__':
    print(longest_common_prefix("interspecies", "interstellar"))  # inters
    print(longest_common_prefix("dog", "cat"))                    # empty
