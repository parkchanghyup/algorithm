from collections import deque

def bfs(maps, visited, y, x, cnt):

    q = deque([(y, x)])
    visited[y][x] = 1
    dx = [0, 0, 1, -1]
    dy = [1, -1, 0, 0]
    while q:
        y, x = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < len(maps[0]) and 0 <= ny < len(maps):
                if maps[ny][nx] == 1 and visited[ny][nx] == -1:
                    visited[ny][nx] = visited[y][x] + 1
                    q.append((ny, nx))
    return visited[len(maps)-1][len(maps[0])-1]


def solution(maps):

    visited = [[-1] * len(maps[0]) for _ in range(len(maps))]

    return bfs(maps, visited, 0, 0, 1)