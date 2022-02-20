from typing import Sequence, Optional


def binary_search(elem: int, arr: Sequence, low: Optional[int] = None, high: Optional[int] = None) -> Optional[int]:
    """
    Performs binary search of given element inside of array (using recursive way)

    :param elem: element to be found
    :param arr: array where element is to be found
    :param low: left border of searching
    :param high: right border of searching
    :return: Index of element if it's presented in the arr, None otherwise
    """
    sorted_arr = sorted(arr)
    if low is None:
        low = 0
    if high is None:
        high = len(sorted_arr) - 1
    if low > high:
        return None
    mid = (low + high) // 2
    if sorted_arr[mid] == elem:
        index_elem = arr.index(elem)
        return index_elem
    elif sorted_arr[mid] > elem:
        high = mid - 1
        return binary_search(elem, arr, low, high)
    elif sorted_arr[mid] < elem:
        low = mid + 1
        return binary_search(elem, arr, low, high)


if __name__ == "__main__":
    print(binary_search(9, [1, 2, 2, 4, 6, 9, 3, 3]))
