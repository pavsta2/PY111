from typing import List
from operator import lt, gt


def sort(container: List[int], asc: bool = True, inplace=True) -> List[int]:
    """
    Sort input container with bubble sort

    :param container: container of elements to be sorted
    :param asc: сортировать ли по возрастанию
    :return: container sorted in ascending order
    """

    # for _ in range(len(container)):
    #     for i in range(len(container)-1):
    #         if container[i] > container[i+1]:
    #             container[i], container[i+1] = container[i+1], container[i]

    if not inplace:
        container = container.copy()

    len_dynamic = len(container)
    compare_operator = gt if asc else lt

    for _ in range(len_dynamic):
        is_change = False  # не было замены элемента

        for i in range(len_dynamic - 1):
            if compare_operator(container[i], container[i + 1]):
                container[i], container[i + 1] = container[i + 1], container[i]
                is_change = True

        if not is_change:
            break
        len_dynamic -= 1

    return container

    # это сортировка устойчивая и inplace


if __name__ == '__main__':
    print(sort([1, 2, 3], False))

    list_ = [1, 2, 3]
    a = sort(list_,inplace=False)
    print(a)
