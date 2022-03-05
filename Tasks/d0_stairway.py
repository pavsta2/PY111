from typing import Union, Sequence


def stairway_path(stairway: Sequence[Union[float, int]]) -> Union[float, int]:
    """
    Calculate min cost of getting to the top of stairway if agent can go on next or through one step.

    :param stairway: list of ints, where each int is a cost of appropriate step
    :return: minimal cost of getting to the top
    """
    total_coast = {}

    def lazy_stairway_path(stair_number: int) -> Union[float, int]:
        if stair_number in total_coast:  # мемоизация
            return total_coast[stair_number]
        if stair_number == 0:
            total_coast[stair_number] = stairway[stair_number]
            return total_coast[stair_number]
        if stair_number == 1:
            total_coast[stair_number] = stairway[stair_number]
            return total_coast[stair_number]
        total_coast[stair_number] = stairway[stair_number] + min(lazy_stairway_path(stair_number - 1),
                                                                 lazy_stairway_path(stair_number - 2))
        return total_coast[stair_number]

    return lazy_stairway_path(len(stairway) - 1)


def direct_stairway_path(stairway: Sequence[Union[float, int]]) -> Union[float, int]:
    ...
    # stairway - цена ступени
    count_stairs = len(stairway)
    total_cost = [float("inf")] * count_stairs
    # изначальное условие 1 и 2 ступень
    # прямой метод обхода i-стоимость = i-цена + min (i-1-стоимость, i-2-стоимость)
    for i in range(count_stairs):
        if i == 0:
            total_cost[0] = stairway[0]
        elif i == 1:
            total_cost[1] = min(stairway[1], (stairway[0] + stairway[1]))
        else:
            total_cost[i] = stairway[i] + min(total_cost[i - 1], total_cost[i - 2])
    return total_cost[-1]


def reverse_stairway_path(stairway: Sequence[Union[float, int]]) -> Union[float, int]:
    ...
    # stairway - цена ступени
    count_stairs = len(stairway)
    total_cost = [float("inf")] * count_stairs
    #
    total_cost[0] = stairway[0]
    total_cost[1] = min(stairway[1], (stairway[0] + stairway[1]))
    for i in range(count_stairs - 2):
        total_cost[i + 1] = min(total_cost[i + 1], (total_cost[i] + stairway[i + 1]))
        total_cost[i + 2] = min(total_cost[i + 2], (total_cost[i] + stairway[i + 2]))

    total_cost[-1] = min(total_cost[-2] + stairway[-1], (total_cost[-1]))
    return total_cost[-1]
