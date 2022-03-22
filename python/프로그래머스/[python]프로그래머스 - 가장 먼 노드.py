import heapq
from collections import defaultdict


def solution(n, vertex):

    q = [(0, 1)]
    distance = [int(1e9)] * (n+1)
    distance[0], distance[1] = 0, 0

    arr = defaultdict(list)

    for a, b in vertex:
        arr[a].append(b)
        arr[b].append(a)

    while q:
        dist, now = heapq.heappop(q)

        if distance[now] < dist:
            continue

        for node in arr[now]:
            if 1 + dist < distance[node]:
                distance[node] = 1+dist
                heapq.heappush(q, (1+dist, node))

    max_length = max(distance)

    cnt = 0

    for i in range(n+1):
        if distance[i] == max_length:
            cnt += 1

    return cnt


solution(6, [[3, 6], [4, 3], [3, 2], [1, 3], [1, 2], [2, 4], [5, 2]])
