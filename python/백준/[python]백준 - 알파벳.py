R, C = map(int, input().split())

arr = []
for i in range(R):
    temp = input()
    temp_ = []
    for j in temp:
        temp_.append(ord(j) - ord('A'))

    arr.append(temp_)


dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
answer = 0
visited = [0] * 26


def dfs(y, x, cnt):

    global answer
    answer = max(cnt, answer)

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if 0 <= nx < C and 0 <= ny < R:
            if visited[arr[ny][nx]] == 0:
                visited[arr[ny][nx]] = 1
                dfs(ny, nx, cnt+1)
                visited[arr[ny][nx]] = 0


visited[arr[0][0]] = 1
dfs(0, 0, 1)

print(answer)
