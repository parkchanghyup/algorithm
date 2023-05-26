import heapq, collections
        

def dijkstra(paths, n,  gates, summits):
    
    '''
    다익스트라
    '''
    
    nodes = []
    
    nodes = collections.defaultdict(list)
    
    for a, b, w in paths: 
        
        nodes[a].append((b,w))
        nodes[b].append((a,w))

    # 큐 변수 : [(소요시간, 노드)]
    dist = collections.defaultdict(int)
    Q = []
    for gate in gates:
        Q.append((0,gate))
    answer = [0,int(1e9)]

    while Q:
        time, node = heapq.heappop(Q)
        
        # 정상을 한번 방문 한 후 , 해당 경로보다 오래 걸리는 경로를 탐색할 필요는 없기 때문에
        # continue
        if time > answer[1]:
            continue
        
        # answer 업데이트
        if node in summits:
            if time < answer[1]:
                answer = [node, time]
            elif time == answer[1] and node < answer[0]:
                answer = [node, time]
            continue
        
        
        if node not in dist:
            dist[node] = time
            for v, w in nodes[node]:
                if v in dist:
                    continue
                heapq.heappush(Q,  (max(w,time), v))
                
    return answer

def solution(n, paths, gates, summits):
    candidate = []
    # 입구별 정상별 최단 경로 

    candidate = dijkstra(paths,n,gates,summits)

    return candidate