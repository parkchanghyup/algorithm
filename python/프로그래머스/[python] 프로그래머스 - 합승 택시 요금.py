import heapq, collections


answer = int(1e9)

def dijkstra_2(graph, N, start,a,b):
    '''
    중간 지점에서 A, B까지 최대 거리 계산 
    '''

    # 큐 변수 : [(소요시간, 노드)]
    QQ = [(0, start)]
    dist_2 = collections.defaultdict(int)
    result = 0
    while QQ:
        time, node = heapq.heappop(QQ)

        if node not in dist_2:
            
            if node == a or node == b:

                result+=time
            dist_2[node] = time
            for v, w in graph[node]:
                heapq.heappush(QQ, (w + time, v))

    return result


def dijkstra(nodes, N, start,a,b):
    '''
    다익스트라 알고리즘으로 거리가 가까운 순으로 중간지점을 이동시키고
    해당 지점에서 A,B까지 거리를 계산 하여 최솟 값 갱신
    '''
    global answer
    graph = collections.defaultdict(list)

    # 그래프 인접 리스트 구성
    for u, v, w in nodes:
        graph[u].append((v, w))
        graph[v].append((u, w))

    # 큐 변수 : [(소요시간, 노드)]
    Q = [(0, start)]
    dist = collections.defaultdict(int)

    while Q:
        time, node = heapq.heappop(Q)

        if node not in dist:
            # 해당 노드에서 A와 B의 집까지 최소 거리 업데이트
            answer = min(answer,time + dijkstra_2(graph,N,node,a,b))

            dist[node] = time
            for v, w in graph[node]:
                heapq.heappush(Q, (w + time, v))


    return dist
    
    

def solution(n, s, a, b, fares):
    global answer
    dijkstra(fares, n,s,a,b)
    
    return answer

