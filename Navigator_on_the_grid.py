import random
from typing import Hashable, Mapping, Union
import networkx as nx

#
def dijkstra_algo(g: nx.DiGraph, starting_node: Hashable) -> Mapping[Hashable, Union[int, float]]:
    """
    Функция с помощью алгоритма Дейкстры из модуля NetworkX находит кратчайшие пути до всех достижимых вершин графа.
    Если вершина не достижима, то стоимость пути до неё должна быть равно float("inf")

    :param g: Взвешенный направленный граф NetworkX, по которому надо рассчитать стоимости кратчайших путей
    :param starting_node: Стартовый узел, откуда нужно начать обход
    :return: словарь как {'node1': 0, 'node2': 10, '3': 33, ...} со стоимостью путей, где node1, node2 - это узлы из графа g
    """
    _, coasts = nx.dijkstra_predecessor_and_distance(g, starting_node)
    for node in g.nodes:
        if node not in coasts:
            coasts[node] = float("inf")

    return coasts


# if __name__ == '__main__':
#     graph = nx.DiGraph()
#     graph.add_weighted_edges_from([
#         (1, 2, 7),
#         (1, 3, 9),
#         (1, 6, 14),
#         (2, 3, 10),
#         (2, 4, 15),
#         (3, 4, 11),
#         (3, 6, 2),
#         (4, 5, 6),
#         (5, 6, 9),
#     ])
#
#     print(dijkstra_algo(graph, 1))  # {1: 0, 2: 7, 3: 9, 6: 11, 4: 20, 5: 26}






def wayy(table):
    wayyy = []
    n = len(table)
    m = len(table[0])
    #
    # Цикл по первому столбцу
    for row_index in range(n - 1):
        table[row_index + 1][0] += table[row_index][0]
    # Цикл по первой строке
    for col_index in range(m - 1):
        table[0][col_index + 1] += table[0][col_index]
    #
    for i in range(1, n):
        for j in range(1, m):
            table[i][j] += min(table[i - 1][j], table[i][j - 1])
            wayyy.append((i, j))
    print(table)
    print(wayyy)
    return table
#
if __name__ == "__main__":
    #list_ = [random.randint(1, 5) for _ in range(20)]
    row = 3
    col = 4
    list_ = [[0] * col for _ in range(row)]
    print(list_)
    for col_ in range(col):
        for row_ in range(row):
            list_[row_][col_] = random.randint(1, 5)
    print(list_)
    for i in range(len(list_)):
        print(list_[i])
    a = wayy(list_)
    for i in range(len(a)):
        print(a[i])

        graph = nx.DiGraph()
        graph.add_weighted_edges_from([
            (list_[0][0], list_[0][1], 7),
            (list_[0][1], list_[0][2], 9),
            (list_[0][2], list_[0][3], 4),
            (list_[1][0], list_[1][1], 3),
            (list_[1][1], list_[1][2], 4),
            (list_[1][2], list_[1][3], 6)
        ])

    print(dijkstra_algo(graph, list_[1][3]))
    print(wayy(list_))



