from collections import deque
def bfs(y, x, num):

    dx = [0, 0, 1, -1]
    dy = [1, -1, 0, 0]

    q = deque()
    q.append((y, x))
    united[y][x] = num
    avg = graph[y][x]  # 현재 연합의 전체 인구수
    cnt = 1  # 현재 연합의 나라 수
    union = []
    union.append((y, x))
    while q:
        y, x = q.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < N and 0 <= ny < N and united[ny][nx] == -1:

                if Min <= abs(graph[ny][nx] - graph[y][x]) <= Max:
                    q.append((ny, nx))
                    united[ny][nx] = num
                    avg += graph[ny][nx]
                    cnt += 1
                    union.append((ny, nx))

    for i, j in union:
        graph[i][j] = avg // cnt
    return cnt


N, Min, Max = list(map(int, input().split()))

graph = []

for _ in range(N):
    graph.append(list(map(int, input().split())))

answer = 0
cnt = 0
while True:
    united = [[-1] * N for _ in range(N)]
    num = 0
    for i in range(N):
        for j in range(N):
            if united[i][j] == -1:
                bfs(i, j, num)
                num += 1

    if num == N*N:
        break
    answer += 1


print(answer)