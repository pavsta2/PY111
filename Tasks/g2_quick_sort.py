from typing import List
from random import choice

def sort(container: List[int]) -> List[int]:
    """
    Sort input container with quick sort

    :param container: container of elements to be sorted
    :return: container sorted in ascending order
    """

    if not container:
        return container

    med_element = choice(container)

    med_element_list = [value for value in container if value == med_element]
    left_list = [value for value in container if value < med_element]
    right_list = [value for value in container if value > med_element]

    return sort(left_list) + med_element_list + sort(right_list)
