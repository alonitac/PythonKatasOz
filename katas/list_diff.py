"""Consecutive differences of a list."""


def list_diff(values):
    """
    Builds a new list where each item is that value minus the one before it.
    The first item has no predecessor, so it is None.

    Example:
        list_diff([10, 7, 12]) -> [None, -3, 5]

    Args:
        values: a list of numbers

    Returns:
        a list of the same length. Empty input returns an empty list.
    """
    if not values:
        return []

    final_list = []

    final_list.insert(0,None)
    curr = 1

    while(curr < len(values)):
        final_list.insert(curr,(values[curr] - values[curr - 1]) )
        curr = curr + 1


    return final_list


if __name__ == '__main__':
    print(list_diff([10, 7, 12]))  # [None, -3, 5]
