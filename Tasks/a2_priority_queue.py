"""
Priority Queue

Queue priorities are from 0 to 10
"""
from typing import Any


class PriorityQueue:
    def __init__(self):
        self.priority_queue = {}  # для очереди можно использовать python dict

    def enqueue(self, elem: Any, priority: int = 0) -> None:
        """
        Operation that add element to the end of the queue
        :param elem: element to be added
        :param priority: order of dequeueing
        :return: Nothing
        """
        queue = self.priority_queue.get(priority, [])
        queue.append(elem)
        self.priority_queue[priority] = queue
        return None

    def dequeue(self) -> Any:
        """
        Return element from the beginning of the queue. Should return None if not elements.
        :return: dequeued element
        """
        new_tuple = self.priority_queue.items()
        sorted_tuple = sorted(new_tuple, key=lambda x: x[0])
        sorted_priority_queue = dict(sorted_tuple)
        list_keys = list(sorted_priority_queue.keys())
        dequeue_elem = None
        for i in list_keys:
            if sorted_priority_queue[i]:
                dequeue_elem = sorted_priority_queue[i][0]
                del sorted_priority_queue[i][0]
                break
        return dequeue_elem

    def peek(self, ind: int = 0, priority: int = 0) -> Any:
        """
        Allow you to look at the element in the queue without dequeuing it
        :param ind: index of element (count from the beginning)
        :param priority: order of dequeueing
        :return: peeked element
        """
        return self.priority_queue[priority][ind]

    def clear(self) -> None:
        """
        Clear my queue

        :return: None
        """
        self.priority_queue.clear()
        return None

    def __str__(self):
        return f"{self.priority_queue}"


if __name__ == "__main__":
    d = PriorityQueue()
    d.enqueue(10, 5)
    print(d)
    d.enqueue(20, 1)
    d.enqueue(40, 1)
    d.enqueue(30, 9)
    print(d)
    print(d.dequeue())
    print(d)
    print(d.dequeue())
    print(d)
    print(d.peek(0, 1))
