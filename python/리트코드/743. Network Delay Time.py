class Solution:
    def networkDelayTime( self,times: List[List[int]], N: int, K: int) -> int:
        # 그래프 인접리스트 구성
        graph = collections.defaultdict(list)

        for u,v,w in times:
            graph[u].append((v,w))

        # 큐변수 : (소요시간,정점)
        Q = [(0,K)]
        dist = collections.defaultdict(int)

        while Q:
            time , node =heapq.heappop(Q)

            if node not in dist:
                dist[node] = time 
                for v,w in graph[node]:
                    heapq.heappush(Q,(w+time,v))
        if len(dist) < N:
            return -1

        return max(dist.values())    