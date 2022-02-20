from typing import Sequence, Optional


def binary_search(elem: int, arr: Sequence) -> Optional[int]:
    """
    Performs binary search of given element inside of array (using recursive way)

    :param elem: element to be found
    :param arr: array where element is to be found
    :return: Index of element if it's presented in the arr, None otherwise
    """
    sorted_arr = sorted(arr)
    low = 0
    high = len(sorted_arr) - 1
    mid = (low + high) // 2
    if sorted_arr[mid] == elem:
        return mid
    if sorted_arr[mid] > elem:
        arr = sorted_arr[:(mid - 1)]
        return binary_search(elem, arr)
    if sorted_arr[mid] < elem:
        arr = sorted_arr[(mid+1):]
        return binary_search(elem, arr)


if __name__ == "__main__":
    print(binary_search(7, [1, 4, 5, 6, 7, 3, 4, 8, 2]))
