import collections



'''
3 3
1 2 1
2 3 2
1 3 3
'''

def find_parent(parent,x):
    if parent[x] != x:
        parent[x] = find_parent(parent,parent[x])
    return parent[x]

def union_parent(parent,a,b):
    
    a = find_parent(parent,a)
    b =find_parent(parent,b)
    
    if a < b:
        parent[b] = a
    else:
        parent[a] = b
        
        


V,E = map(int,input().split())

edges = []

for i in range(E):
    u,v,w = map(int,input().split())
    edges.append([u,v,w])


    
edges.sort(key = lambda x : x[2])


parent = [0] * (V+1)


for i in range(V+1):
    parent[i] = i
    
result = 0
for u,v,w in edges:
    if find_parent(parent,u) != find_parent(parent,v):
        result +=w
        union_parent(parent,u,v)
print(result)