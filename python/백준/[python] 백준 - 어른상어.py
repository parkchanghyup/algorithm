import collections

N, M ,K = list(map(int, input().split()))

graph = []

for _ in range(N):
    graph.append(list(map(int, input().split())))

s_dir = list(map(int, input().split()))

s_rank = []
for i in range(M):
    temp = []
    for j in range(4):
        temp.append(list(map(int, input().split())))
    s_rank.append(temp)

shark_pos = collections.defaultdict(tuple)

for i in range(N):
    for j in  range(N):
        if graph[i][j] != 0 :
            shark_pos[graph[i][j]] = (i,j)
            graph[i][j] = [graph[i][j],graph[i][j],K]
        else:
            graph[i][j] = [0,0,0]


dx = [0,0,-1,1]
dy = [-1,1,0,0]

result = 0
delete_shark = []
while result < 1000:




    for shark in range(M,0,-1):
        if shark in delete_shark:
            continue
        dir = s_dir[shark-1] - 1
        priority_dir = s_rank[shark-1][dir]

        (y,x) = shark_pos[shark]
        temp_x, temp_y = -1, -1
        temp_d = -1
        move = False
        for d in priority_dir:

            nx = x+dx[d-1]
            ny = y+dy[d-1]

            # 맵 이탈 방지,
            if (0<= nx < N) and(0<= ny < N):
                # 향이 없다
                if graph[ny][nx][2] == 0:
                    graph[ny][nx] = [shark,shark,K+1]
                    graph[y][x][0] = 0
                    shark_pos[shark] = (ny,nx)
                    move = True
                    s_dir[shark - 1] = d
                    break

                elif graph[ny][nx][2] == K+1 and graph[ny][nx][0] > shark:
                    delete_shark.append(graph[ny][nx][0])
                    graph[ny][nx] = [shark, shark, K+1]
                    graph[y][x][0] = 0
                    shark_pos[shark] = (ny, nx)
                    move = True
                    s_dir[shark - 1] = d
                    break
                elif graph[ny][nx][1] == shark and temp_x == -1 :
                    temp_x, temp_y = nx, ny
                    temp_d= d

        if move is False:
            graph[temp_y][temp_x] = [shark,shark,K+1 +graph[temp_y][temp_x][2]]
            shark_pos[shark] = (temp_y, temp_x)
            graph[y][x][0] = 0
            s_dir[shark - 1] =temp_d



    check = True
    for i in range(N):
        for j in range(N):
            if graph[i][j][0] > 1 :
                check= False

    # 전체 -1
    for i in range(N):
        for j in range(N):
            graph[i][j][2] -= 1
            if graph[i][j][2] <= 0:
                graph[i][j] = [0,0,0]
            if graph[i][j][2] > K:
                graph[i][j][2] = K

    if check  :
        print(result+1)
        break
    result += 1
if result == 1000:
    print(-1)