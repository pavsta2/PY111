"""
You can do it either with networkx ('cause tree is a graph)
or with dicts (smth like {'key': 0, value: 123, 'left': {...}, 'right':{...}})
"""
from typing import Any, Optional, Tuple

# import networkx as nx

# Node: TypeAlias = "BinarySearchTree.Node"


class BinarySearchTree:
    class Node:
        def __init__(self, key: int, value: Any, left: Optional["BinarySearchTree.Node"] = None,
                     right: Optional["BinarySearchTree.Node"] = None):
            self.key = key
            self.value = value
            self.left = left
            self.right = right

        def __str__(self) -> str:
            return f"узел {self.key} со значением {self.value}"

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

    @staticmethod
    def create_node(key: int, value: Any):
        """
        Метод создает объект класса Node
        :param key: ключ
        :param value: значение
        :return: node object
        """
        return BinarySearchTree.Node(key, value)

    def insert(self, key: int, value: Any) -> None:
        """
        Insert (key, value) pair to binary search tree
        :param data: class Node object as a node of the tree
        :return: None
        """
        new_node = self.create_node(key, value)  # fixed именно здесь сделать новый узел вместо аргумента
        if self.root is None:
            self.root = new_node
        else:
            current_root = self.root
            root_key = new_node.key

            while True:
                if root_key > current_root.key:
                    if current_root.right is not None:
                        current_root = current_root.right
                    else:
                        current_root.right = new_node
                        break
                if root_key < current_root.key:
                    if current_root.left is not None:
                        current_root = current_root.left
                    else:
                        current_root.left = new_node
                        break

    def str_rek(self, node: Optional["BinarySearchTree.Node"]):
        node = self.root
        if node.left and node.right is not None:
            return f"{self.str_rek(node.left)}{self.str_rek(node.right)}\n"



    def __str__(self):
        # if self.root is None:
        #     return "дерево бинарного поиска пустое"
        return f"{self.root}"

    def remove(self, key: int) -> Optional[Tuple[int, Any]]:
        """
        Remove key and associated value from the BST if exists

        :param key: key to be removed
        :return: deleted (key, value) pair or None
        """
        print(key)
        return None

    def find(self, key: int) -> Optional[Any]:
        """
        Find value by given key in the BST

        :param key: key for search in the BST
        :return: value associated with the corresponding key
        """
        print(key)
        return None

    def clear(self) -> None:
        """
        Clear the tree

        :return: None
        """
        return None


if __name__ == "__main__":
    a = BinarySearchTree()
    # b = BinarySearchTree.Node(34, "корень")
    # c = BinarySearchTree.Node(36, "второй")
    # d = BinarySearchTree.Node(30, "третий")
    a.insert(34, "корень")
    a.insert(36, "второй")
    a.insert(30, "третий")
    print(a)
