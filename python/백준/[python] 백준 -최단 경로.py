'''
다익스트라 알고리즘을 이용하여 각 노드의 최단 거리를 구해주면 된다.
'''


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

#최단거리 처리 리스트
dist = collections.defaultdict(int)

# 다익스트라

while Q:
    time,node = heapq.heappop(Q)
    # 해당 노드에 처음 방문한다면 dist 업데이트 (최단거리 이므로)
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

    
    
