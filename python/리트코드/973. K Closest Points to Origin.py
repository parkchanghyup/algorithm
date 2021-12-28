class Solution:
    def kClosest( self,points: List[List[int]], K: int) -> List[List[int]]:
        Q=[]
        for x,y in points:
            heapq.heappush(Q,(x**2+y**2,x,y))
        result = []
        for _ in range(K):
            dist,x,y=heapq.heappop(Q)
            result.append([x,y])

        return result