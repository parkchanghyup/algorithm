from collections import deque

dx = [1,-1,0,0]
dy =  [0,0,1,-1]


def bfs(start, graph, visited):
    queue = deque()
    queue.append((start[0],start[1]))
    
    cnt = int(graph[start[0]][start[1]])
    visited[start[0]][start[1]] = True
    while queue:
        y, x = queue.popleft()
        
        for i in range(4):
            nx = x  + dx[i]
            ny = y + dy[i]
            
            if 0 <= nx and len(graph[0]) > nx and 0 <= ny and len(graph)> ny:
                if graph[ny][nx] != 'X' and visited[ny][nx] == False:
                    queue.append((ny,nx))
                    cnt += int(graph[ny][nx])

                    visited[ny][nx] = True
                
    return cnt
                
                
def solution(maps):
    visited = [[False] * len(maps[0]) for _ in range(len(maps))]            
    answer = []
    for i in range(len(maps)):
        for j in range(len(maps[0])):
                
                if visited[i][j] == False and maps[i][j] != 'X':

                    answer.append(bfs((i,j), maps, visited))
                
    if answer:
        answer.sort()
        return answer
    else :
        return [-1]

                   