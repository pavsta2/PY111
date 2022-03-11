from typing import List
from random import choice, randint


def sort(container: List[int]) -> List[int]:
    """
    Sort input container with quick sort

    :param container: container of elements to be sorted
    :return: container sorted in ascending order
    """

    def _sort(left_border, right_border) -> None:
        if left_border >= right_border:
            return

        random_index = randint(left_border, right_border)
        pivot = container[random_index]
        #  choice(container[left_border:right_border]) - не inplace

        i, j = left_border, right_border

        while i <= j:
            while container[i] < pivot:
                i += 1
            while container[j] > pivot:
                j -= 1
            if i <= j:
                container[i], container[j] = container[j], container[i]
                i += 1
                j -= 1
        _sort(left_border, j)
        _sort(i, right_border)

    _sort(0, len(container) - 1)
    return container

    # if not container:
    #     return container
    #
    # med_element = choice(container)
    #
    # med_element_list = [value for value in container if value == med_element]
    # left_list = [value for value in container if value < med_element]
    # right_list = [value for value in container if value > med_element]
    #
    # return sort(left_list) + med_element_list + sort(right_list)
