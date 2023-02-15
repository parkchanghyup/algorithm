from collections import deque, defaultdict


def bfs(graph, start, n):
    visited = [False] * (n + 1)

    queue = deque([start])

    # 현재 노드 방문 처리
    visited[start] = True
    dist = [-1] * (n + 1)

    dist[start] = 0

    while queue:
        v = queue.popleft()

        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True
                dist[i] = dist[v] + 1

    return dist


def solution(n, roads, sources, destination):
    result = []
    graph = defaultdict(list)
    for u, v in roads:
        graph[u].append(v)
        graph[v].append(u)

    dist = bfs(graph, destination, n)

    for source in sources:
        result.append(dist[source])

    return result