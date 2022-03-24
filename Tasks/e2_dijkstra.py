from typing import Hashable, Mapping, Union
import networkx as nx
from matplotlib import pyplot as plt


def draw_graph(graph):
    pos = nx.spring_layout(graph)
    nx.draw_networkx_nodes(graph, pos)
    nx.draw_networkx_labels(graph, pos)

    for edge in graph.edges:
        nx.draw_networkx_edges(
            graph, pos,
            edgelist=[(edge[0], edge[1])], connectionstyle="arc3,rad=0.2"
        )

    plt.show()


def dijkstra_algo(g: nx.DiGraph, starting_node: Hashable) -> Mapping[Hashable, Union[int, float]]:
    """
    Count shortest paths from starting node to all nodes of graph g
    :param g: Graph from NetworkX
    :param starting_node: starting node from g
    :return: dict like {'node1': 0, 'node2': 10, '3': 33, ...} with path costs, where nodes are nodes from g
    """
    # draw_graph(g)
    path_coasts = {node: (float('inf')) for node in g.nodes}
    path_coasts[starting_node] = 0
    visited_nodes = {node: False for node in g.nodes}
    current_node = starting_node

    while True:
        visited_nodes[current_node] = True
        neighbours = g[current_node]

        for neighbour in neighbours:
            if path_coasts[neighbour] == float('inf'):
                path_coasts[neighbour] = path_coasts[current_node] + g[current_node][neighbour]["weight"]
            else:
                if path_coasts[current_node] + g[current_node][neighbour]["weight"] < path_coasts[neighbour]:
                    path_coasts[neighbour] = path_coasts[current_node] + g[current_node][neighbour]["weight"]

        not_visited = {node: path_coasts[node] for node in g.nodes if not visited_nodes[node]}
        if not not_visited:
            break
        # current_node = min(not_visited, key=not_visited.get)
        current_node, _ = min(
            not_visited.items(),
            key=lambda item: item[1]
        )

    return path_coasts

    # visited = {node: False for node in g.nodes}
    # total_costs = {node: float("inf") for node in g.nodes}
    # current_node = starting_node
    # total_costs[current_node] = 0
    #
    # while True:
    #     visited[current_node] = True
    #     # обновляем стоимости всех соседей
    #     for neighbour_node in g[current_node]:
    #         edge = g[current_node][neighbour_node]
    #         weight = edge['weight']
    #         total_costs[neighbour_node] = min(
    #             total_costs[neighbour_node],
    #             total_costs[current_node] + weight)
    #
    #     # выбрать новый current_node
    #     not_visited_total_costs = {node: cost for node, cost in total_costs.items() if not visited[node]}
    #     if not not_visited_total_costs:
    #         break
    #     current_node = min(
    #         not_visited_total_costs.items(),
    #         key=lambda item: item[0]
    #     )
    #     print(not_visited_total_costs.items())
    # return total_costs

if __name__ == "__main__":
    G = nx.DiGraph()
    G.add_nodes_from("ABCDEFG")
    G.add_weighted_edges_from([
        ("A", "B", 1),
        ("B", "C", 3),
        ("C", "E", 4),
        ("E", "F", 3),
        ("B", "E", 8),
        ("C", "D", 1),
        ("D", "E", 2),
        ("B", "D", 2),
        ("G", "D", 1),
        ("D", "A", 2),
    ])

    print(dijkstra_algo(G, "D"))

