class Solution:
    def findCheapestPrice( self,n: int, flights: List[List[int]], src: int, dst: int, K: int) -> int:
        #그래프 생성
        graph = collections.defaultdict(list)
        for u,v,w in flights:
            graph[u].append((v,w))
        Q = [(0,src,K)]
        
        while Q:
            weight , node ,k = heapq.heappop(Q)
            if node ==dst:
                return weight
        
         
            if k>=0:
                for v,w in graph[node]:
                    heapq.heappush(Q,(weight+w,v,k-1))
        



        return -1    