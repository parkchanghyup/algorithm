from collections import deque

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]


def func(visited, start, target, maps):
    q = deque()
    q.append((start[0], start[1]))

    while q:

        now_y, now_x = q.popleft()

        for i in range(4):
            next_y = now_y + dy[i]
            next_x = now_x + dx[i]
            # 맵을 벗어나면 탐색 x
            if next_y < 0 or next_y >= len(maps) or next_x < 0 or next_x >= len(maps[0]):
                continue
            # 원하는 타겟을 찾으면 바로 return
            if maps[next_y][next_x] == target:
                visited[next_y][next_x] = visited[now_y][now_x] + 1
                return visited[next_y][next_x]

            # 해당 위치까지 거리 업데이트
            if (visited[next_y][next_x] == 0) and (maps[next_y][next_x] != 'X'):
                q.append((next_y, next_x))
                visited[next_y][next_x] = visited[now_y][now_x] + 1

    return -1


def solution(maps):
    answer = 0
    visited = [[0] * (len(maps[0])) for _ in range(len(maps))]
    start, lever = (0, 0), (0, 0)

    for i in range(len(maps)):
        for j in range(len(maps[0])):

            if maps[i][j] == 'S':
                start = (i, j)
            elif maps[i][j] == 'L':
                lever = (i, j)

    # 레버까지 거리 계산
    dist = func(visited, start, 'L', maps)
    # 탐색 불가 일시 -1 return
    if dist == -1:
        return -1
    answer += dist

    # 레버에서 출구까지 거리 계산
    visited = [[0] * (len(maps[0])) for _ in range(len(maps))]
    dist = func(visited, lever, 'E', maps)
    # 탐색 불가 일시 -1 return
    if dist == -1:
        return -1
    answer += dist

    return answer
