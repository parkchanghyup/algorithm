def find_parent(parent,x):
    if parent[x] != x :
        parent[x] = find_parent(parent,parent[x])
    return parent[x]

def union_parent(parent,a,b):

    a = find_parent(parent,a)
    b = find_parent(parent,b)

    if a > b :
        parent[a] = b
    else :
        parent[b] = a

N, M = map(int,input().split())


parent = [0] * (N+1)

for i in range(N+1):
    parent[i] = i


edges = []

for _ in range(M):
    a,b,c = map(int,input().split())
    edges.append((c,a,b))

edges.sort()

answer = 0
for c,a,b in edges:
    if find_parent(parent,a) != find_parent(parent,b):
        union_parent(parent,a,b)
        answer += c
        last = c
    
print(answer- last)
