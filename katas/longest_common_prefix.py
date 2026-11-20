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
    result=""
    if len(left)==0 or len(right)==0:
        return result
    small=min(len(left),len(right))
    for i in range (0,small):
        if left[i]==right[i]:
            result=result+left[i]
        else:
            return result
    return result


if __name__ == '__main__':
    print(longest_common_prefix("interspecies", "interstellar"))  # inters
    print(longest_common_prefix("dog", "cat"))                    # empty
