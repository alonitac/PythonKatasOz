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

    shared_len = 0
    i = 0
    border = min(len(left),len(right))
    while i < border and left[i] == right[i]:
            shared_len = shared_len + 1
            i = i + 1    
    if shared_len == 0:
        return ""
    else:
        return left[:shared_len]            

    


if __name__ == '__main__':
    print(longest_common_prefix("interspecies", "interstellar"))  # inters
    print(longest_common_prefix("dog", "cat"))                    # empty
