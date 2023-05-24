answer = int(1e9)
def solution(board):
    # R: 처음위치, D : 장애물 위치, G : 목표지점
    # 그래프 정의


    graph = []
    
    for y,row in enumerate(board):
        row_temp  = []
        for x,temp in enumerate(row):
            
            # 처음 위치 정의
            if temp == 'R':
                now_x, now_y = x, y
                
            row_temp.append(temp)
        graph.append(row_temp)
        

    # 이동 방향 정의
    dx = [0,0,1,-1]
    dy = [1,-1,0,0]
    
    # 최대 이동 거리 
    max_move = len(graph) - 1
    
    # 방문체크용 리스트
    visited = [[-1] * len(graph[0]) for _ in range(len(graph))]
    def dfs(y,x,cnt):

        global answer
        
        
        if graph[y][x] == 'G':

            answer = min(answer,cnt)
            return
    
        # 방문한적이 있는데 이미 최단거리라면 return
        if visited[y][x]> 0 and visited[y][x] <= cnt:
            return
        visited[y][x] = cnt
        
        for i in range(4):
            for dist in range(1, 101):

                nx = x + dx[i] * dist
                ny = y + dy[i] * dist
                if nx < 0 or nx >= len(graph[0]) or ny < 0 or ny >= len(graph) or graph[ny][nx] == 'D':
                    # 이동 불가 위치면 움직인  방향의 뒤로 한칸
                    nx = nx - dx[i]
                    ny = ny - dy[i]

                    break

            dfs(ny,nx,cnt+1)

    dfs(now_y, now_x, 0)
   
    if answer == int(1e9):
        return -1
    return answer 