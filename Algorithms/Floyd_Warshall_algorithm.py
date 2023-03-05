from math import inf


def floydWarshall(graph):
    distance = graph
    length = len(distance)

    for k in range(length):
        for i in range(length):
            for j in range(length):
                distance[i][j] = min(distance[i][j], distance[i][k] + distance[k][j])

    return distance


def main():
    graph = [
        [0, 2, inf, 3, 1, inf, inf, 10],
        [2, 0, 4, inf, inf, inf, inf, inf],
        [inf, 4, 0, inf, inf, inf, inf, 3],
        [3, inf, inf, 0, inf, inf, inf, 8],
        [1, inf, inf, inf, 0, 2, inf, inf],
        [inf, inf, inf, inf, 2, 0, 3, inf],
        [inf, inf, inf, inf, inf, 3, 0, 1],
        [10, inf, 3, 8, inf, inf, 1, 0],
    ]

    res = floydWarshall(graph)
    for row in res:
        print(*row)


if __name__ == '__main__':
    main()
