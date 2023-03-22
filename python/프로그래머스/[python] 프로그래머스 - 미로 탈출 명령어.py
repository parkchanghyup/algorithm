from collections import deque

dx = [1,0,0,-1]
dy = [0,-1,1,0]
move = ['d', 'l', 'r', 'u']


def solution(n, m, x, y, r, c, k):
    graph = [[[] for _ in range(m) ] for _ in range(n)]
    

    queue = deque()
    queue.append((x,y,"",0))
    
    while queue:
        x,y,path,cnt = queue.popleft()

        if (x,y) == (r,c) and (cnt == k):
            return path
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            move_path = move[i]
            
            if abs(nx - r) + abs(ny - c) + cnt + 1 > k: continue
            if nx >= 1 and ny >= 1 and nx <= n and ny <= m:
                queue.append((nx, ny, path+move_path, cnt+1))
                break
    
    return 'impossible'
