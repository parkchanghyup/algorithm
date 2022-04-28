# 마법사 상어와 토네이도
def wind(s_y, s_x, d):
    '''
    현재 좌표에서 d방향으로 바람이 불때 모래를 이동 시킴.
    '''
    global ans
    if s_x < 0:
        return
    total = 0  # 밖으로 나가는 모래의 양

    for dy, dx, ratio in d:
        nx = s_x + dx
        ny = s_y + dy
        if ratio == 0:
            new_sand = sand[s_y][s_x]- total
        else:
            new_sand = int(sand[s_y][s_x] * ratio)
            total += new_sand

        if 0 <= nx < N and 0 <= ny < N:
            sand[ny][nx] += new_sand
        else:
            ans += new_sand
    sand[s_y][s_x] = 0


N = int(input())
sand = [list(map(int, input().split())) for _ in range(N)]

# 방향별 모래 비율
left = [(1, 1, 0.01), (-1, 1, 0.01), (1, 0, 0.07), (-1, 0, 0.07), (1, -1, 0.1),
        (-1, -1, 0.1), (2, 0, 0.02), (-2, 0, 0.02), (0, -2, 0.05), (0, -1, 0)]
right = [(y, -x, z) for y, x, z in left]
down = [(-x, y, z) for y, x, z in left]
up = [(x, y, z) for y, x, z in left]

s_x, s_y = N // 2, N // 2
ans = 0
dy = [0, 1, 0, -1]
dx = [-1, 0, 1, 0]

wind_dir = [left, down, right, up]
time = 0

for i in range(2*N-1):
    dir = i % 4
    if dir == 0 or dir == 2:
        time += 1
    for _ in range(time):
        nx = s_x + dx[dir]
        ny = s_y + dy[dir]
        wind(ny, nx, wind_dir[dir])

        s_x, s_y = nx, ny


print(ans)

