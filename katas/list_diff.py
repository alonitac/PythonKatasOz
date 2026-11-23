"""Consecutive differences of a list."""


def list_diff(values):
    """
    Builds a new list where each item is that value minus the one before it.
    The first item has no predecessor, so it is None.
    """
    if not values:
        return []

    result = [None]

    for i in range(1, len(values)):
        result.append(values[i] - values[i - 1])

    return result


if __name__ == '__main__':
    print(list_diff([10, 7, 12]))  # [None, -3, 5]
