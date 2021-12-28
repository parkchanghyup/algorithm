
class Solution:
    
    def canFinish(self,numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = collections.defaultdict(list)
        # 그래프 생성
        for a, b in prerequisites:
            graph[a].append(b)
        # 방문 체크
        trace = set()
        visited = set()
        def dfs(num):

            if num in trace:

                return False
            if num in visited:
                return True
            
            trace.add(num)
            visited.add(num)
            for i in graph[num]:
                if not dfs(i):
                    return False



            trace.remove(num)

            return True

        for i in list(graph):
            if not dfs(i):

                return False

        return True