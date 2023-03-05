class Graph:
    def __init__(self, vertices, graph=None):
        self.graph = [] if graph is None else graph
        self.vertices = vertices + 1

    def add_edge(self, v1, v2, weight):
        self.graph.append([v1, v2, weight])

    def search(self, parent, i):
        if parent[i] == i:
            return i
        return self.search(parent, parent[i])

    def apply_union(self, parent, rank, x, y):
        xroot = self.search(parent, x)
        yroot = self.search(parent, y)
        if rank[xroot] < rank[yroot]:
            parent[xroot] = yroot
        elif rank[xroot] > rank[yroot]:
            parent[yroot] = xroot
        else:
            parent[yroot] = xroot
            rank[xroot] += 1

    def kruskal(self):
        result = []
        i, e = 0, 1
        self.graph = sorted(self.graph, key=lambda item: item[2])
        parent = []
        rank = []
        for node in range(self.vertices):
            parent.append(node)
            rank.append(0)

        while e < self.vertices - 1:
            u, v, w = self.graph[i]
            i = i + 1
            x = self.search(parent, u)
            y = self.search(parent, v)
            if x != y:
                e = e + 1
                result.append([u, v, w])
                self.apply_union(parent, rank, x, y)

        return result


def algorithm2(graph):
    graph = graph
    sort_graph = sorted(graph, key=lambda x: x[2])
    con_vertex = set()   # список соединенных вершин
    isol_vert = {}      # словарь списка изолированных групп вершин
    skelet_edges = []      # список ребер остова

    for r in sort_graph:
        if r[0] not in con_vertex or r[1] not in con_vertex:  # проверка для исключения циклов в остове
            if r[0] not in con_vertex and r[1] not in con_vertex: # если обе вершины не соединены, то
                isol_vert[r[0]] = [r[0], r[1]]          # формируем в словаре ключ с номерами вершин
                isol_vert[r[1]] = isol_vert[r[0]]               # и связываем их с одним и тем же списком вершин
            else:                           # иначе
                if not isol_vert.get(r[0]):             # если в словаре нет первой вершины, то
                    isol_vert[r[1]].append(r[0])        # добавляем в список первую вершину
                    isol_vert[r[0]] = isol_vert[r[1]]           # и добавляем ключ с номером первой вершины
                else:
                    isol_vert[r[0]].append(r[1])        # иначе, все то же самое делаем со второй вершиной
                    isol_vert[r[1]] = isol_vert[r[0]]

            skelet_edges.append(r)             # добавляем ребро в остов
            con_vertex.add(r[0])             # добавляем вершины в множество U
            con_vertex.add(r[1])

    for r in sort_graph:    # проходим по ребрам второй раз и объединяем разрозненные группы вершин
        if r[1] not in isol_vert[r[0]]:     # если вершины принадлежат разным группам, то объединяем
            skelet_edges.append(r)             # добавляем ребро в остов
            gr1 = isol_vert[r[0]]
            isol_vert[r[0]] += isol_vert[r[1]]      # объединем списки двух групп вершин
            isol_vert[r[1]] += gr1

    return skelet_edges


def main():
    graph = [(1, 2, 13), (1, 3, 18), (1, 4, 17), (1, 5, 14), (1, 6, 22),
         (2, 3, 26), (2, 5, 22), (3, 4, 3), (4, 6, 19)]


    dubl = set()
    for v1, v2, weigth in graph:
        if v1 not in dubl:
            dubl.add(v1)
        if v2 not in dubl:
            dubl.add(v2)

    length = len(dubl)
    g = Graph(length, graph)

    print(g.kruskal())
    print(algorithm2(graph))


if __name__ == '__main__':
    main()