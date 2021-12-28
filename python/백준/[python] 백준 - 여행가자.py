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


N = int(input())
M = int(input())
parent = [0] * (N + 1)

edges = []

for i in range(N):
    edges.append(list(map(int, input().split())))

for i in range(N + 1):
    parent[i] = i
    
for i in range(N):
    for j in range(N):
        if edges[i][j] == 1:
            union_parent(parent, i + 1, j + 1)

tour = list(map(int, input().split()))

pos = True
for idx in range(len(tour)-1):
    if parent[tour[idx]] != parent[tour[idx+1]]:
        pos = False
        break

if pos:
    print('YES')
else:
    print('NO')