import heapq, collections


def dijkstra(nodes, N, start):
    graph = collections.defaultdict(list)

    # 그래프 인접 리스트 구성
    for u, v, w in nodes:
        graph[u].append((v, w))

    # 큐 변수 : [(소요시간, 노드)]
    Q = [(0, start)]
    dist = collections.defaultdict(int)
    while Q:
        time, node = heapq.heappop(Q)
        if node not in dist:
            dist[node] = time
            for v, w in graph[node]:
                heapq.heappush(Q, (w + time, v))

    return dist


nodes = [[1, 2, 2], [1, 3, 5], [1, 4, 1], [2, 3, 3], [2, 4, 2], [3, 2, 3], [3, 6, 5], [4, 3, 3], [4, 5, 1], [5, 3, 1],
         [5, 6, 2]]
start = 1
result = dijkstra(nodes, 6, start)
for i in range(1, 7):
    if i == start:
        print(start, ':', 0)
    else:
        print(i, ': INF' if result[i] == 0 else ':', result[i])