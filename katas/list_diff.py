"""Consecutive differences of a list."""


def list_diff(values):
    if values == []:
        return []
    temp = values.copy()
    for i in range(values.index(values[-1])+1):
        values[i] -= temp[i-1]
    values[0] = None
    return values


if __name__ == '__main__':
    print(list_diff([10, 7, 12]))  # [None, -3, 5]
