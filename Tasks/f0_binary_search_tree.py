"""
You can do it either with networkx ('cause tree is a graph)
or with dicts (smth like {'key': 0, value: 123, 'left': {...}, 'right':{...}})
"""

from typing import Any, Optional, Tuple, TypeAlias


# import networkx as nx

Node: TypeAlias = "BinarySearchTree.Node"


class BinarySearchTree:
    class Node:
        def __init__(self, key: int, value: Any, left: Optional[Node] = None, right: Optional[Node] = None):
            self.key = key
            self.value = value
            self.left = left
            self.right = right

        def __str__(self) -> str:
            return str(f"узел {self.key} со значением {self.value}")

    # @staticmethod
    # def _create_node(key, value: Any, left: Optional[dict] = None, right: Optional[dict] = None) -> dict:
    #     """Фабрика узлов"""
    #     return {
    #         "key": key,
    #         "value": value,
    #         "left": left,
    #         "right": right
    #     }

    def __init__(self, root: Optional[Node] = None):
        self.root = root
        #  self.root: Optional[Node] = None - так не работает?

    def insert(self, data: Node) -> None:
        """
        Insert (key, value) pair to binary search tree
        :param data: class Node object as a node of the tree
        :return: None
        """
        data = ...  # fixme именно здесь сделать новый узел вместо аргумента
        if self.root is None:
            self.root = data
        else:
            current_root = self.root
            root_key = data.key

            while True:
                if root_key > current_root.key:
                    if current_root.left is not None:
                        current_root = current_root.left
                    else:
                        current_root.left = data
                        break
                if root_key < current_root.key:
                    while current_root.right is not None:
                        current_root = current_root.right
                    current_root.right = data


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
    b = BinarySearchTree.Node(34, "корень")
    c = BinarySearchTree.Node(36, "второй")
    d = BinarySearchTree.Node(30, "третий")
    a.insert(b)
    a.insert(c)
    a.insert(d)
    print(b)
    print(c)
    print(d)
    print(b.left)
    print(b.right)
    print(c.left)
    print(c.right)