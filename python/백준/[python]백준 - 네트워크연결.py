import heapq


def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]


def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)

    if a < b:
        parent[b] = a
    else:
        parent[a] = b


n = int(input())

parent = [0] * (n+1)

for i in range(n+1):
    parent[i] = i

m = int(input())
edges = []
answer = 0
for i in range(m):
    v, w, cost = map(int, input().split())
    heapq.heappush(edges, (cost, v, w))

for _ in range(len(edges)):
    cost, v, w = heapq.heappop(edges)

    if find_parent(parent, v) != find_parent(parent, w):
        union_parent(parent, v, w)
        answer += cost
print(answer)
