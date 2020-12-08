import heapq
import collections

def solution(N, road, K)
    answer = 0
    
    graph = collections.defaultdict(list)
    
    # 그래프 생성
    for u,v,w in road
        graph[u].append((v,w))
        graph[v].append((u,w))
        
    Q = [(0,1)]
    
    dist = collections.defaultdict(int)
    
    while Q
        time,node = heapq.heappop(Q)
    
        if node not in dist 
            dist[node] = time            
            for v,w in graph[node]
                heapq.heappush(Q,(w+time,v))
    
    result = 0
    
    for key in dist.keys()
        if dist[key] =K
            result +=1
            
    return result