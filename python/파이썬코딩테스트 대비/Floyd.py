def solution(n, roads, sources, destination):
    result = []
    INF = int(1e9)
    graph = [[INF] * (n + 1) for _ in range(n + 1)]

    for i in range(n + 1):
        graph[i][i] = 0
    for u, v in roads:
        graph[u][v] = 1
        graph[v][u] = 1

    for k in range(1, n + 1):
        for i in range(1, n + 1):
            for j in range(1, n + 1):
                graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])

    for source in sources:

        if graph[source][destination] == int(1e9):
            result.append(-1)
        else:
            result.append(graph[source][destination])
    return result


n = 3
roads = [[1, 2], [2, 3]]
sources = [2, 3]
destination = 1
result = [1, 2]

solution(n, roads, sources, destination)