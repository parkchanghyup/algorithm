import collections
import heapq


V,E = map(int,input().split())
K = int(input())

# 그래프 생성

graph = collections.defaultdict(list)

for _ in range(E):
    u,v,w = map(int,input().split())
    graph[u] .append((v,w))
    
Q = [(0,K)]

dist = collections.defaultdict(int)

# 다익스트라
while Q:
    time,node = heapq.heappop(Q)
    
    if node not in dist:
        dist[node] = time
        for v,w  in graph[node]:
            heapq.heappush(Q,((time+w),v))

for i in range(1,V+1):
    if i==K:
        print('0')
    elif dist[i] ==0:
        print('INF')
    else:
        print(dist[i])

    
    
