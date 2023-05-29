import collections


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


n, m = 7, 12

parent = [0] * (n + 1)

for i in range(1, n + 1):
    parent[i] = i

nodes = [(1, 2, 3), (1, 3, 2), (3, 2, 1), (2, 5, 2), (3, 4, 4), (7, 3, 6), (5, 1, 5), (1, 6, 2), (6, 4, 1), (6, 5, 3),
         (4, 5, 3), (6, 7, 4)]
nodes.sort(key=lambda x: x[2])

graph = collections.defaultdict(list)

result = 0
for node in nodes:
    u, v, w = node

    if find_parent(parent, u) != find_parent(parent, v):
        union_parent(parent, u, v)
        result += w
print(result)