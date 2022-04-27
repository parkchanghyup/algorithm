from collections import deque
from copy import deepcopy


def combination(comb, idx):
    if len(comb) == M:
        candidate.append(comb)
        return
    if idx >= len(virus):
        return

    for i in range(idx, len(virus)):
        combination(comb + [virus[i]], i + 1)


def check(array):
    for i in range(N):
        for j in range(N):
            if array[i][j] == 0:
                return -1
    return 0


def bfs(start, arr):
    array = deepcopy(arr)
    visited = [[0 for _ in range(len(array))] for _ in range(len(array))]

    queue = deque()

    queue.extend(start)

    result = 0

    while queue:
        y, x, cnt = queue.popleft()
        visited[y][x] = 1

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < N and 0 <= ny < N and not visited[ny][nx] and array[ny][nx] != 1:
                visited[ny][nx] = 1
                if array[ny][nx] == 0:
                    array[ny][nx] = 2
                    result = cnt + 1
                queue.append((ny, nx, cnt + 1))
    flag = check(array)
    if flag == 0:
        return result
    return -1


N, M = map(int, input().split())
virus = []
arr = []
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
for i in range(N):
    temp = list(map(int, input().split()))
    for j in range(N):
        if temp[j] == 2:
            virus.append((i, j, 0))
    arr.append(temp)

candidate = []

combination([], 0)
mins = int(1e9)
for cand in candidate:
    result = bfs(cand, arr)
    if mins > result and result != -1:
        mins = result
if mins == int(1e9):
    print(-1)
else:
    print(mins)
