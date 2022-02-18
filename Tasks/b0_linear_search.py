"""
This module implements some functions based on linear search algo
"""
from typing import Sequence


def min_search(arr: Sequence) -> int:
    """
    Function that find minimal element in array

    :param arr: Array containing numbers
    :return: index of first occurrence of minimal element in array
    """
    min_el = arr[0]
    for el in arr:
        if el < min_el:
            min_el = el
    print(arr)
    return arr.index(min_el)


if __name__ == "__main__":
    print(min_search([2, 4, 7, 9, 1, 6, 9, 1]))