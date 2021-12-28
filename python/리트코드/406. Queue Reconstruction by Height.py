class Solution:

    def reconstructQueue( self,people: List[List[int]]) -> List[List[int]]:



        q = []
        result= []

        for height , num in people:
            heapq.heappush(q,(-height,num))



        while q:
            person = heapq.heappop(q)
            result.insert(person[1],[-person[0],person[1]])

        return result