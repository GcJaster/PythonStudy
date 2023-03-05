def heuristic(node, x: (int, int) = None, y: (int, int) = None):
    # there should be a function that calculates
    # heuristic distance according to the formula and returns it

    # like this: return abs(x[0] - y[0]) + abs(x[1] + y[1])

    # for example, here is a dictionary with heuristic distances for each
    # point that emulates the calculated distance using the formula

    heuristic_dist = {
        'A': 11,
        'B': 6,
        'C': 99,
        'D': 1,
        'E': 7,
        'G': 0
    }
    return heuristic_dist[node]


def get_neighbors(v, graph: dict):
    # define function to return neighbor and its distance
    # from the passed node
    if v in graph:
        return graph[v]
    else:
        return None


def a_star(start_node, stop_node, graph):
    open_set = set(start_node)
    closed_set = set()
    g = dict()  # store distance from starting node
    parents = dict()  # parents contains an adjacency map of all nodes

    # distance of staring node from itself is zero
    g[start_node] = 0
    # start_node is root node i.e. it has no parent nodes
    # so start_node is set to its own  parent node
    parents[start_node] = stop_node

    while len(open_set) > 0:
        n = None

        # node with Lowest f() is found
        for v in open_set:
            if n is None or g[v] + heuristic(v) < g[n] + heuristic(n):
                n = v

        if n is stop_node or graph[n] is None:
            pass
        else:
            for (m, weight) in get_neighbors(n, graph):
                # nodes 'm' not in first and last set are added to first
                # n is set its parent
                if m not in open_set and m not in closed_set:
                    open_set.add(m)
                    parents[m] = n
                    g[m] = g[n] + weight

                # for each node m, compare its distance from
                # start i.e. g(m) to the from start through n node
                else:
                    if g[m] > g[n] + weight:
                        # update g(m)
                        g[m] = g[n] + weight
                        # change parent of m to n
                        parents[m] = n

                        # if m in closed set, remove and add to open
                        if m in closed_set:
                            closed_set.remove(m)
                            open_set.add(m)

        if n is None:
            print('Path does not exists')
            return None

        # if the current node is the stop_node
        # then we begin reconstruction the path from it to the start node
        if n is stop_node:
            path = []

            while parents[n] != stop_node:
                path.append(n)
                n = parents[n]

            path.append(start_node)
            path.reverse()
            print(f"Path found: {path}")
            return path

        # remove n from the open_list, and add it to closed_list
        # because all of his neighbors were inspected
        open_set.remove(n)
        closed_set.add(n)

    print("Path does not exists!")
    return None


def main():
    graph = {
        'A': [('B', 2), ('E', 3)],
        'B': [('C', 1), ('G', 9), ('D', 2)],
        'C': None,
        'E': [('D', 6)],
        'D': [('G', 1)]
    }

    a = a_star('A', 'G', graph)
    print(a)


if __name__ == '__main__':
    main()
