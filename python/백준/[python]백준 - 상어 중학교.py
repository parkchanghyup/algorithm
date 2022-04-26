# 상어 중학교(https://www.acmicpc.net/problem/21609)

from collections import deque


def bfs(y, x, color):
    q = deque()
    dy = [-1, 0, 1, 0]
    dx = [0, 1, 0, -1]

    q.append((y, x))
    visited = [[False] * N for _ in range(N)]
    visited[y][x] = True
    block_cnt, rainbow_cnt = 1, 0  # 블록 갯수

    blocks, rainbows = [[y, x]], []  # 블록 좌표 넣을리스트, 무지개 좌표 넣을 리스트

    while q:
        y, x = q.popleft()
        for d in range(4):
            ny = y + dy[d]
            nx = x + dx[d]

            # 범위 안이면서 방문 안한 일반 블록일 경우
            if 0 <= nx < N and 0 <= ny < N and not visited[ny][nx] and arr[ny][nx] == color:
                visited[ny][nx] = 1
                q.append([ny, nx])
                block_cnt += 1
                blocks.append([ny, nx])
            # 범위 안이면서 방문 안한 무지개 블록인 경우
            if 0 <= nx < N and 0 <= ny < N and not visited[ny][nx] and arr[ny][nx] == 0:
                visited[ny][nx] = 1
                q.append([ny, nx])
                block_cnt += 1
                rainbow_cnt += 1
                rainbows.append([ny, nx])
    # 무지개블록은 방문 해제
    for y, x in rainbows:
        visited[y][x] = 0
    return [block_cnt, rainbow_cnt, blocks+rainbows]

# 블록 제거 함수


def remove(block):
    for y, x in block:
        arr[y][x] = -2


# 중력 함수
def gravity(arr):
    for i in range(N-2, -1, -1):  # 밑에서 부터 체크
        for j in range(N):
            if arr[i][j] > -1:  # -1이 아니면 아래로 다운
                r = i
                while True:
                    # 다음행이 인덱스 범위 안이면서 -2 이면 아래로 다운
                    if 0 <= r+1 < N and arr[r+1][j] == -2:
                        arr[r+1][j] = arr[r][j]
                        arr[r][j] = -2
                        r += 1
                    else:
                        break
# 반시계 회전 함수


def rot90(arr):
    new_arr = [[0] * N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            new_arr[N-1-j][i] = arr[i][j]
    return new_arr


N, M = map(int, input().split())

arr = [list(map(int, input().split())) for _ in range(N)]

score = 0

while True:
    '''
    오토플레이
    1. 크기가 가장 큰 블록 찾기
    2. 블록제거 + 점수더하기
    3. 중력
    4. 90도 회전
    5. 중력
    '''
    visited = [[0] * N for _ in range(N)]  # 방문 체크
    blocks = []  # 가능한 블록 그룹들 넣을 리스트
    for i in range(N):
        for j in range(N):
            if arr[i][j] > 0 and not visited[i][j]:  # 일반블록 and 방문 x
                visited[i][j] = 1  # 방문
                block_info = bfs(i, j, arr[i][j])
                if block_info[0] >= 2:
                    blocks.append(block_info)
    blocks.sort(reverse=True)

    # 블록제거
    if not blocks:
        break
    remove(blocks[0][2])
    score += blocks[0][0] ** 2

    gravity(arr)

    arr = rot90(arr)
    gravity(arr)

print(score)
