"""
You can do it either with networkx ('cause tree is a graph)
or with dicts (smth like {'key': 0, value: 123, 'left': {...}, 'right':{...}})
"""
from typing import Any, Optional, Tuple
from queue import Queue


# import networkx as nx

# Node: TypeAlias = "BinarySearchTree.Node"


class BinarySearchTree:
    class Node:
        def __init__(self, key: int, value: Any, level: int = 1, left: Optional["BinarySearchTree.Node"] = None,
                     right: Optional["BinarySearchTree.Node"] = None):
            self.level = level
            self.key = key
            self.value = value
            self.left = left
            self.right = right

        def __str__(self) -> str:
            return f"узел:{self.key},значение:{self.value}, level:{self.level}"

    # @staticmethod
    # def _create_node(key, value: Any, left: Optional[dict] = None, right: Optional[dict] = None) -> dict:
    #     """Фабрика узлов"""
    #     return {
    #         "key": key,
    #         "value": value,
    #         "left": left,
    #         "right": right
    #     }

    def __init__(self, root: Optional["BinarySearchTree.Node"] = None):
        self.root = root

    def create_node(self, key: int, value: Any):
        """
        Метод создает объект класса Node
        :param key: ключ
        :param value: значение
        :return: node object
        """
        self.is_valid_key(key)
        return BinarySearchTree.Node(key, value)

    def insert(self, key: int, value: Any) -> None:
        """
        Insert (key, value) pair to binary search tree
        :param data: class Node object as a node of the tree
        :return: None
        """
        self.is_valid_key(key)
        new_node = self.create_node(key, value)  # fixed именно здесь сделать новый узел вместо аргумента
        if self.root is None:
            self.root = new_node
        else:
            current_root = self.root
            root_key = new_node.key
            level = 2

            while True:
                if root_key > current_root.key:
                    if current_root.right is not None:
                        current_root = current_root.right
                        level += 1
                    else:
                        current_root.right = new_node
                        new_node.level = level
                        break
                if root_key < current_root.key:
                    if current_root.left is not None:
                        current_root = current_root.left
                        level += 1
                    else:
                        current_root.left = new_node
                        new_node.level = level
                        break

    def str_rek(self, node: Optional["BinarySearchTree.Node"]) -> list:
        """
        рекурсивная функция для магич метода __str__
        :param node: текущий узел
        :return:
        """
        if node.left is None and node.right is None:
            return [[node.level, node.key, node.value]]
        if node.left is not None and node.right is not None:
            return [[node.level, node.key, node.value]] + self.str_rek(node.left) + self.str_rek(node.right)
        elif node.left is None and node.right is not None:
            return [[node.level, node.key, node.value]] + self.str_rek(node.right)
        elif node.left is not None and node.right is None:
            return [[node.level, node.key, node.value]] + self.str_rek(node.left)

    def __str__(self):
        if self.root is None:
            return "дерево бинарного поиска пустое"

        current_node = self.root

        return f"{sorted(self.str_rek(current_node))}"

    def __bool__(self):
        if self.root is None:
            return False
        else:
            return True

    def is_valid_key(self, key) -> None:
        if not isinstance(key, int):
            raise TypeError("Значение ключа только целочисленное")
        # if key < 0:
        #     raise ValueError("Значение ключа не должно быть отрицательным")


    def remove(self, key: int) -> Optional[Tuple[int, Any]]:
        """
        Remove key and associated value from the BST if exists

        :param key: key to be removed
        :return: deleted (key, value) pair or None
        """
        self.is_valid_key(key)
        node_to_remove = self.find_node(key)




        print(key)
        return None

    def find_node(self, key: int) -> Optional[Any]:
        """
        Find node by given key in the BST

        :param key: key for search in the BST
        :return: node associated with the corresponding key
        """
        if self.root is None:
            return "Дерево бинарного поиска пустое"
        self.is_valid_key(key)

        current_node = self.root

        while current_node:
            if current_node.key == key:
                return current_node
            elif key > current_node.key:
                current_node = current_node.right
            elif key < current_node.key:
                current_node = current_node.left
        else:
            return "Такой ключ не найден"

    def find(self, key: int) -> Optional[Any]:
        """
        Find value by given key in the BST

        :param key: key for search in the BST
        :return: value associated with the corresponding key
        """
        result_node = self.find_node(key)

        return result_node.value


    def clear(self) -> None:
        """
        Clear the tree

        :return: None
        """
        self.root = None
        return None


if __name__ == "__main__":
    a = BinarySearchTree()
    # b = BinarySearchTree.Node(34, "корень")
    # c = BinarySearchTree.Node(36, "второй")
    # d = BinarySearchTree.Node(30, "третий")
    a.insert(34, "корень")
    a.insert(36, "второй")
    a.insert(30, "третий")
    a.insert(102, "четвертый")
    a.insert(32, "пятый")
    a.insert(31, "шестой")
    a.insert(35, "седьмой")
    print(a)

    print(a.find(35))

