import math
from heapq import heapify, heappush, heappop


def dijstra(graph: dict, start: str, finish: str = None):
    """
    Алгоритм Дейкстры для нахождения кратчайшего пути между стартовой вершиной и всеми остальными.

    Parameters
    ----------
    graph: dict
        Словарь описывающий граф и связи вершин в неё
    start: str
        Стартовая вершина графа
    finish: str
        Конечная вершина графа(для вывода пути между конкретной парой)

    Returns
    -------
    None
    """


    node_data = dict((key, {'cost': math.inf, 'pred': []}) for key in graph)
    node_data[start]['cost'] = 0
    visited = []
    temp = start
    for i in range(len(graph) - 1):
        if temp not in visited:
            visited.append(temp)
            min_heap = []
            for neigh_node in graph[temp]:
                if neigh_node not in visited:
                    cost = node_data[temp]['cost'] + graph[temp][neigh_node]
                    if cost < node_data[neigh_node]['cost']:
                        # priority = cost + heuristic(node_data[neigh_node], node_data[temp])
                        node_data[neigh_node]['cost'] = cost
                        node_data[neigh_node]['pred'] = node_data[temp]['pred'] + list(temp)

                    heappush(min_heap, (node_data[neigh_node]['cost'], neigh_node))

        heapify(min_heap)
        temp = min_heap[0][1]

    # print("Shortest Distance: " + str(node_data[finish]['cost']))
    # print("Shortest path: " + str(node_data[finish]['pred'] + list(finish)))

    print(*[f"Shortest Distance for {vert} = {node_data[vert]['cost']}. That is {node_data[vert]['pred']}"
            for vert in node_data.keys() if vert != 'A'], sep='\n')



def main():
    graph = {
        'A': {'B': 2, 'C': 4},
        'B': {'A': 2, 'C': 3, 'D': 8},
        'C': {'A': 4, 'B': 3, 'E': 5, 'D': 2},
        'D': {'B': 8, 'C': 2, 'E': 11, 'F': 22},
        'E': {'C': 5, 'D': 11, 'F': 1},
        'F': {'D': 22, 'E': 1}
    }
    start = 'A'
    finish = 'F'
    dijstra(graph, start, finish)


if __name__ == '__main__':
    main()