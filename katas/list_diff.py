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
    if(len(values) == 0):
        return []

    newList = [None]
    for i in range(1, len(values)):
        newList.append(values[i] - values[i - 1])
    return newList    


if __name__ == '__main__':
    print(list_diff([10, 7, 12]))  # [None, -3, 5]
