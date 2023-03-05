from math import inf


class Graph:
    def __init__(self, vertices):
        self.vertices = vertices
        self.graph = [[0 for column in range(vertices)]
                      for row in range(vertices)]

    def printMST(self, parent):
        print("Edge \tWeight")
        for i in range(1, self.vertices):
            print(parent[i], "-", i, "\t", self.graph[i][parent[i]])

    def minKey(self, key, mstSet):
        min = inf
        min_index = 0
        for v in range(self.vertices):
            if key[v] < min and mstSet[v] is False:
                min = key[v]
                min_index = v

        return min_index

    def primMST(self):
        key = [inf] * self.vertices
        parent = [None] * self.vertices
        key[0] = 0
        mstSet = [False] * self.vertices
        parent[0] = -1

        for cout in range(self.vertices):
            u = self.minKey(key, mstSet)
            mstSet[u] = True
            for v in range(self.vertices):
                if 0 < self.graph[u][v] < key[v] and mstSet[v] is False:
                    key[v] = self.graph[u][v]
                    parent[v] = u

        self.printMST(parent)


def prims_algorithm(graph):
    def get_min(graph, con_vert: set):
        rm = (inf, -1, -1)
        for v in con_vert:
            rr = min(graph, key=lambda x: x[2] if (x[0] == v or x[1] == v) and
                                                  (x[0] not in con_vert or x[1] not in con_vert) else inf)
            if rm[0] > rr[0]:
                rm = rr

        return rm

    graph = graph
    vert_count = 6     # число вершин в графе
    con_vert = {1}   # множество соединенных вершин
    skeleton_vert = []    # список ребер остова

    while len(con_vert) < vert_count:
        r = get_min(graph, con_vert)       # ребро с минимальным весом
        if r[2] == inf:    # если ребер нет, то остов построен
            break

        skeleton_vert.append(r)             # добавляем ребро в остов
        con_vert.add(r[0])             # добавляем вершины в множество U
        con_vert.add(r[1])

    print(skeleton_vert)


def main():
    # список ребер графа (вершина 1, вершина 2, длина)
    # первое значение возвращается, если нет минимальных ребер
    graph = [(1, 2, 13), (1, 3, 18), (1, 4, 17), (1, 5, 14), (1, 6, 22),
             (2, 3, 26), (2, 5, 22), (3, 4, 3), (4, 6, 19)]

    prims_algorithm(graph)

    g = Graph(5)
    g.graph = [[0, 2, 0, 6, 0],
               [2, 0, 3, 8, 5],
               [0, 3, 0, 0, 7],
               [6, 8, 0, 0, 9],
               [0, 5, 7, 9, 0]]

    g.primMST()


if __name__ == '__main__':
    main()