from collections import deque

def bfs(graph, visited, x,y):
    q = deque()
    q.append((y,x))

    visited[y][x] = 1

    dx = [0,0,1,-1]
    dy = [1,-1,0,0]

    while q:
        y,x = q.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <=  nx < M and 0<= ny < N:
                if graph[ny][nx] == 1 and visited[ny][nx] == 0 :
                    q.append((ny,nx))
                    visited[ny][nx] = 1
                



T = int(input())
# 가로, 세로, 배추


for _ in range(T):
    M,N,K = map(int,input().split())

    graph = [[0] * M for _ in range(N)]
    visited = [[0] * M for _ in range(N)]
    for _ in range(K):
        a,b  = map(int,input().split())
        graph[b][a] = 1
    count = 0
    for i in range(N):
        for j in range(M):
            if graph[i][j] == 1 and visited[i][j] ==0:
                bfs(graph,visited, j,i)
                count +=1

    
    print(count)



