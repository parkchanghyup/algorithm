from collections import defaultdict
import copy

dx = [0,0,-1,-1,-1,0,1,1,1]
dy = [0,-1,-1,0,1,1,1,0,-1]


arr = [[0] * 4 for _ in range(4)]

pos_dic = defaultdict(tuple)

for i in range(4):
    temp_ = list(map(int, input().split()))
    for j in range(4):
        num, dir = temp_[j*2], temp_[j*2+1]
        pos_dic[num] = (i,j)
        arr[i][j] = [num,dir]


def dfs(sx, sy, score,arr):
    global max_score
    score += arr[sy][sx][0]
    max_score = max(max_score, score)
    arr[sy][sx][0] = 0

    for num in range(1,17):
        f_x, f_y = -1,-1
        for y in range(4):
            for x in range(4):
                if arr[y][x][0] == num:

                    f_x, f_y = x, y

        if f_x == -1:
            continue

        f_d = arr[f_y][f_x][1]
        for i in range(8):
            dir = (f_d + i)
            if dir > 8:
                f_d -= 8
                dir -= 8


            nx = f_x+dx[dir]
            ny = f_y+dy[dir]


            if not (0 <= nx < 4 and 0 <= ny < 4) or (nx == sx and ny == sy):
                continue
            arr[f_y][f_x][1] = dir
            arr[f_y][f_x], arr[ny][nx] = arr[ny][nx], arr[f_y][f_x]


            break


    s_d = arr[sy][sx][1]
    for i in range(1,4):
        nx = sx + dx[s_d]*i
        ny = sy + dy[s_d]*i
        if (0<= nx < 4 and 0<= ny < 4) and arr[ny][nx][0] > 0:
            dfs(nx, ny, score, copy.deepcopy(arr))


max_score = 0
dfs(0, 0, 0, arr)
print(max_score)

