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
        def __init__(self, key: int, value: Any, prev: Optional["BinarySearchTree.Node"] = None,
                     left: Optional["BinarySearchTree.Node"] = None,
                     right: Optional["BinarySearchTree.Node"] = None):
            self.key = key
            self.value = value
            self.prev = prev
            self.left = left
            self.right = right

        def __str__(self) -> str:
            return f"(узел:{self.key},знач:{self.value})"

        def __repr__(self):
            return f"({self.key}, {self.value},{self.prev}, {self.left}, {self.right})\n"

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

    def link_nodes(self, up_node: "BinarySearchTree.Node", down_node: "BinarySearchTree.Node") -> None:
        down_node.prev = up_node
        if up_node.key > down_node.key:
            up_node.left = down_node
        elif up_node.key < down_node.key:
            up_node.right = down_node

    def insert(self, key: int, value: Any) -> None:
        """
        Insert (key, value) pair to binary search tree
        :param key:
        :param value:
        :return: None
        """
        self.is_valid_key(key)
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
                        self.link_nodes(current_root, new_node)
                        break
                if root_key < current_root.key:
                    if current_root.left is not None:
                        current_root = current_root.left
                    else:
                        self.link_nodes(current_root, new_node)
                        break

    def bst_nodes_list(self, node: "BinarySearchTree.Node") -> list:
        """
        создает список всех узлов дерева
        :param node: текущий узел
        :return:
        """
        if node.left is None and node.right is None:
            return [node]
        if node.left is not None and node.right is not None:
            return [node] + self.bst_nodes_list(node.left) + self.bst_nodes_list(node.right)
        elif node.left is None and node.right is not None:
            return [node] + self.bst_nodes_list(node.right)
        elif node.left is not None and node.right is None:
            return [node] + self.bst_nodes_list(node.left)

    def __str__(self):
        if self.root is None:
            return "дерево бинарного поиска пустое"

        current_node = self.root

        return f"{self.bst_nodes_list(current_node)}"

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

    def find_min(self, start_node: "BinarySearchTree.Node") -> "BinarySearchTree.Node":
        current_node = start_node.right
        while current_node.left is not None:
            current_node = current_node.left
        return current_node

    def remove(self, key: int) -> Optional[Tuple[int, Any]]:
        """
        Remove key and associated value from the BST if exists

        :param key: key to be removed
        :return: deleted (key, value) pair or None
        """
        self.is_valid_key(key)
        node_to_remove = self.find_node(key)
        current_node = self.root

        if node_to_remove.left is None and node_to_remove.right is None:
            if node_to_remove.prev.left == node_to_remove:
                node_to_remove.prev.left = None
            else:
                node_to_remove.prev.right = None

        if node_to_remove.left is not None and node_to_remove.right is None:
            if node_to_remove.prev.left == node_to_remove:
                node_to_remove.prev.left = node_to_remove.left
            else:
                node_to_remove.prev.right = node_to_remove.left

            # while True:
            #     if current_node.right == node_to_remove:
            #         current_node.right = node_to_remove.left
            #         break
            #     elif current_node.left == node_to_remove:
            #         current_node.left = node_to_remove.left
            #         break
            #     else:
            #         if node_to_remove.key > current_node.key:
            #             current_node = current_node.right
            #             if current_node is None:
            #                 break
            #         else:
            #             current_node = current_node.left
            #             if current_node is None:
            #                 break

        if node_to_remove.left is None and node_to_remove.right is not None:
            if node_to_remove.prev.left == node_to_remove:
                node_to_remove.prev.left = node_to_remove.right
            else:
                node_to_remove.prev.right = node_to_remove.right
            # while True:
            #     if current_node.right == node_to_remove:
            #         current_node.right = node_to_remove.right
            #         break
            #     elif current_node.left == node_to_remove:
            #         current_node.left = node_to_remove.right
            #         break
            #     else:
            #         if node_to_remove.key > current_node.key:
            #             current_node = current_node.right
            #             if current_node is None:
            #                 break
            #         else:
            #             current_node = current_node.left
            #             if current_node is None:
            #                 break
        if node_to_remove.left is not None and node_to_remove.right is not None:
            new_node = self.find_min(node_to_remove)
            node_to_remove.key = new_node.key

            if new_node.prev.left == new_node:
                new_node.prev.left = None
            else:
                new_node.prev.right = None

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
            raise KeyError("Такой ключ не найден")

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
    a.remove(36)
    print(a)

    # print(a.find(35), type(a.find(35)))
