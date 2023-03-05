from math import inf


def get_max_vertex(k, graph, past_vert):
    m = 0   # наименьшее допустимое значение
    v = -1
    for i, w in enumerate(graph[k]):
        if i in past_vert:
            continue

        if w[2] == 1:   # движение по стрелке
            if m < w[0]:
                m = w[0]
                v = i
        else:           # движение против стрелки
            if m < w[1]:
                m = w[1]
                v = i

    return v


def get_max_flow(tag):
    w = [x[0] for x in tag]
    return min(*w)


def update_graph(graph, tags, f):
    for tag in tags:
        if tag[1] == -1:  # это исток
            continue

        route_dir = graph[tag[2]][tag[1]][2]  # направление движения

        # меняем веса в таблице для (i,j) и (j,i)
        graph[tag[1]][tag[2]][0] -= f * route_dir
        graph[tag[1]][tag[2]][1] += f * route_dir

        graph[tag[2]][tag[1]][0] -= f * route_dir
        graph[tag[2]][tag[1]][1] += f * route_dir

def ford_fulkerson(graph, start, end):
    Tinit = (inf, -1, start)      # первая метка маршруто (a, from, vertex)
    max_flow = []      # максимальные потоки найденных маршрутов

    j = start
    while j != -1:
        k = start  # стартовая вершина (нумерация с нуля)
        tags = [Tinit]  # метки маршрута
        past_vert = {start}  # множество просмотренных вершин

        while k != end:     # пока не дошли до стока
            j = get_max_vertex(k, graph, past_vert)  # выбираем вершину с наибольшей пропускной способностью
            if j == -1:         # если следующих вершин нет
                if k == start:      # и мы на истоке, то
                    break          # завершаем поиск маршрутов
                else:           # иначе, переходим к предыдущей вершине
                    k = tags.pop()[2]
                    continue

            c = graph[k][j][0] if graph[k][j][2] == 1 else graph[k][j][1]   # определяем текущий поток
            tags.append((c, j, k))    # добавляем метку маршрута
            past_vert.add(j)            # запоминаем вершину как просмотренную

            if j == end:    # если дошди до стока
                max_flow.append(get_max_flow(tags))     # находим максимальную пропускную способность маршрута
                update_graph(graph, tags, max_flow[-1])        # обновляем веса дуг
                break

            k = j

    total = sum(max_flow)
    return total


def main():
    graph = [[[0, 0, 1], [20, 0, 1], [30, 0, 1], [10, 0, 1], [0, 0, 1]],
             [[20, 0, -1], [0, 0, 1], [40, 0, 1], [0, 0, 1], [30, 0, 1]],
             [[30, 0, -1], [40, 0, -1], [0, 0, 1], [10, 0, 1], [20, 0, 1]],
             [[10, 0, -1], [0, 0, 1], [10, 0, -1], [0, 0, 1], [20, 0, 1]],
             [[0, 0, 1], [30, 0, -1], [20, 0, -1], [20, 0, -1], [0, 0, 1]],
             ]

    res = ford_fulkerson(graph, 0, 4)
    print(f"Максимальный поток равен: {res}")


if __name__ == '__main__':
    main()