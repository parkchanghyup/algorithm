from collections import deque


def bfs(graph, start, target):
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]
    queue = deque()
    queue.append(start)
    visited = [[-1] * (101) for _ in range(101)]
    visited[start[0]][start[1]] = 0

    while queue:
        y, x = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx >= 0 and ny >= 0 and nx <= 100 and ny <= 100:
                if graph[ny][nx] == 1 and visited[ny][nx] == -1:
                    visited[ny][nx] = visited[y][x] + 1
                    queue.append((ny, nx))

    return visited[target[1]][target[0]]


def solution(rectangle, characterX, characterY, itemX, itemY):
    answer = 0

    graph = [[-1] * (101) for _ in range(101)]

    for x0, y0, x1, y1 in rectangle:

        x0, y0, x1, y1 = x0 * 2, y0 * 2, x1 * 2, y1 * 2
        for x in range(x0, x1 + 1):
            for y in range(y0, y1 + 1):
                if x0 < x < x1 and y0 < y < y1:
                    graph[y][x] = 0
                elif graph[y][x] != 0:
                    graph[y][x] = 1

    answer = bfs(graph, (characterY * 2, characterX * 2), (itemX * 2, itemY * 2))

    return answer // 2