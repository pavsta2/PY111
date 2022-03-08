from typing import Hashable, List
from collections import deque

import networkx as nx
from matplotlib import pyplot as plt


# def draw_graph(graph):
#     pos = nx.spring_layout(graph)
#     nx.draw_networkx_nodes(graph, pos)
#     nx.draw_networkx_labels(graph, pos)
#
#     for edge in graph.edges:
#         nx.draw_networkx_edges(
#             graph, pos,
#             edgelist=[(edge[0], edge[1])], connectionstyle="arc3,rad=0.2"
#             )
#
#     plt.show()


# def dfs(g: nx.Graph, start_node: Hashable) -> List[Hashable]:
#     """
#     Do an breadth-first search and returns list of nodes in the visited order
#
#     :param g: input graph
#     :param start_node: starting node for search
#     :return: list of nodes in the visited order
#     """
#     # draw_graph(g)
#     path_nodes = []
#     visited_nodes = {node: False for node in g.nodes}  # словарь из непосещенных узлов
#     wait_nodes = []  # stack
#     wait_nodes.append(start_node)
#     visited_nodes[start_node] = True
#
#     while wait_nodes:
#         current_node = wait_nodes.pop()  # достаем горящий узел, чтобы поджечь соседей, которые еще не горят
#         path_nodes.append(current_node)
#         neighbours = g[current_node]
#         for neighbour in neighbours:
#             if not visited_nodes[neighbour]:
#                 wait_nodes.append(neighbour)  # поджигаем соседей
#                 visited_nodes[neighbour] = True
#
#     return path_nodes

def dfs(g: nx.Graph, start_node: Hashable) -> List[Hashable]:
    """
    Do an breadth-first search and returns list of nodes in the visited order

    :param g: input graph
    :param start_node: starting node for search
    :return: list of nodes in the visited order
    """
    # draw_graph(g)
    path_nodes = []
    visited_nodes = {node: False for node in g.nodes}  # словарь из непосещенных узлов

    def recursion_dfs(current_node):
        if visited_nodes[current_node]:
            return None
        visited_nodes[current_node] = True
        path_nodes.append(current_node)

        neighbours = g[current_node]
        for neighbour in neighbours:
            recursion_dfs(neighbour)

        return path_nodes

    return recursion_dfs(start_node)

