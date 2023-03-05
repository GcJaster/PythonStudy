from typing import Union, List


class Vertex:
    """Class describing the vertex of the graph"""

    def __init__(self) -> None:
        self._links = []
        self._index = None

    @property
    def links(self) -> list:
        return self._links

    @property
    def index(self):
        return self._index

    @index.setter
    def index(self, new_index):
        self._index = new_index


class Station(Vertex):
    def __init__(self, name):
        super().__init__()
        self.name = name

    def __str__(self):
        return self.name

    def __repr__(self):
        return self.name


class Link:
    """Class to describe the connection between the official nodes of the graph"""

    def __init__(self, v1: Vertex, v2: Vertex, dist: int = 1) -> None:
        self._v1 = v1
        self._v2 = v2
        self._dist = dist

    @property
    def v1(self) -> Vertex:
        return self._v1

    @property
    def v2(self) -> Vertex:
        return self._v2

    @property
    def dist(self) -> Union[int, float]:
        return self._dist

    @dist.setter
    def dist(self, value: Union[int, float]) -> None:
        self._dist = value

    def get_v(self):
        return self.v1, self.v2

    def __eq__(self, other) -> bool:
        return {self.v1, self.v2} == {other.v1, other.v2}


class LinkMetro(Link):
    def __init__(self, v1, v2, dist):
        super().__init__(v1, v2, dist)


class LinkedGraph:
    """Class to represent the connected graph as a whole"""

    def __init__(self) -> None:
        self._links = []
        self._vertex = []

    def add_vertex(self, v: Vertex) -> None:
        """To add a new vertex to the vertex list if it is not there"""

        if v not in self._vertex:
            self._vertex.append(v)

    def add_link(self, link: Link) -> None:
        """To add a new link to the _links if there is no link with the specified vertices"""

        if len(self._links) == 0:
            self._links.append(link)
        else:
            for i in self._links:
                if link != i:
                    self._links.append(link)
                    break

        self.add_vertex(link.v1)
        self.add_vertex(link.v2)
        link.v1.links.append(v2)
        link.v2.links.append(v1)

    def find_path(self, start_v=None, stop_v=None):
        self.__set_indexes()

        length = len(self._vertex)
        matrix = [[0] * length for _ in range(length)]

        for i, link in enumerate(self._links):
            vertex1, vertex2, weight = link.v1.index, link.v2.index, link.dist
            matrix[vertex1][vertex2] = matrix[vertex2][vertex1] = weight

        best_path = []



        # print('  ', *[f"{i}".rjust(2, " ") for i in range(1, length + 1)])
        # for i in range(1, length + 1):
        #     print(f"{i}".rjust(2, " "), end=' ')
        #     for j in matrix[i - 1]:
        #         print(str(j).rjust(2, " "), end=' ')
        #     print()

    def __set_indexes(self):
        for i, node in enumerate(self._vertex):
            node.index = i

    def print_matrix(self):
        pass








if __name__ == '__main__':
    map_metro = LinkedGraph()
    v1 = Station("Сретенский бульвар")
    v2 = Station("Тургеневская")
    v3 = Station("Чистые пруды")
    v4 = Station("Лубянка")
    v5 = Station("Кузнецкий мост")
    v6 = Station("Китай-город 1")
    v7 = Station("Китай-город 2")

    map_metro.add_link(LinkMetro(v1, v2, 1))
    map_metro.add_link(LinkMetro(v2, v3, 1))
    map_metro.add_link(LinkMetro(v1, v3, 1))

    map_metro.add_link(LinkMetro(v4, v5, 1))
    map_metro.add_link(LinkMetro(v6, v7, 1))

    map_metro.add_link(LinkMetro(v2, v7, 5))
    map_metro.add_link(LinkMetro(v3, v4, 3))
    map_metro.add_link(LinkMetro(v5, v6, 3))

    map_metro.find_path(v1)

    # print(len(map_metro._links))
    # print(len(map_metro._vertex))
    # path = map_metro.find_path(v1, v6)  # от сретенского бульвара до китай-город 1
    # print(path[0])  # [Сретенский бульвар, Тургеневская, Китай-город 2, Китай-город 1]
    # print(sum([x.dist for x in path[1]]))  # 7

