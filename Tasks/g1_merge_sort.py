from typing import List


def merge_func(sorted_left: list[int], sorted_right: list[int]):
    sorted_result = []
    current_left_ind = 0
    current_right_ind = 0

    while True:
        current_left_value = sorted_left[current_left_ind]
        current_right_value = sorted_right[current_right_ind]

        if current_left_value < current_right_value:
            sorted_result.append(current_left_value)
            current_left_ind += 1
        else:
            sorted_result.append(current_right_value)
            current_right_ind += 1

        if current_left_ind == len(sorted_left):
            sorted_result.extend(sorted_right[current_right_ind:])
            break
        elif current_right_ind == len(sorted_right):
            sorted_result.extend(sorted_left[current_left_ind:])
            break

    return sorted_result


def sort(container: List[int]) -> List[int]:
    """
    Sort input container with merge sort

    :param container: container of elements to be sorted
    :return: container sorted in ascending order
    """
    if len(container) == 1:
        return container

    middle_ind = len(container) // 2

    left_part = sort(container[:middle_ind])
    right_part = sort(container[middle_ind:])

    return merge_func(left_part, right_part)
