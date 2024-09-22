import sys

# n: 격자의 크기, m: 도망자의 수, h: 나무의 수, k: 턴 수
n, m, h, k = map(int, sys.stdin.readline().split())

# 도망자(runner) 정보와 나무(tree) 정보를 저장할 리스트
runner = []
tree = []

# m개의 도망자 정보를 입력받음 (y 좌표, x 좌표, 이동 방향)
for _ in range(m):
    temp_ = list(map(int, sys.stdin.readline().split()))
    runner.append(temp_)

# h개의 나무 정보를 입력받음 (y 좌표, x 좌표)
for _ in range(h):
    temp_ = list(map(int, sys.stdin.readline().split()))
    tree.append(temp_)

# answer: 잡힌 도망자의 수 (초기값 0)
answer = 0

# 이동 방향 (상, 우, 하, 좌)
dx = [0, 1, 0, -1]
dy = [-1, 0, 1, 0]


# 도망자들의 움직임을 처리하는 함수
def runner_move(turn: int) -> None:
    """
    주어진 턴에 도망자들이 움직임을 처리함.

    Args:
        turn (int): 현재 턴 번호
    """
    global n, runner
    catcher_x, catcher_y, _ = catcher_path[turn]
    new_runner = []

    # 각 도망자마다 움직임 처리
    for idx, run in enumerate(runner):
        run_x, run_y, run_d = run
        # 술래와 거리가 3 이상이면 움직이지 않음
        dist = abs(catcher_x - run_x) + abs(catcher_y - run_y)
        if dist > 3:
            new_runner.append(run)
            continue

        # 도망자가 (-1, -1) 즉 이미 잡혔으면 넘어감
        if (run_x, run_y) == (-1, -1):
            continue

        # 도망자의 다음 위치
        ny = run_y + dy[run_d]
        nx = run_x + dx[run_d]

        # 움직이려는 위치에 술래가 있으면 이동하지 않음
        if (nx, ny) == (catcher_x, catcher_y):
            new_runner.append(run)
            continue

        # 격자 내에 있으면 이동
        if 0 <= nx < n and 0 <= ny < n:
            new_runner.append([nx, ny, run_d])
        # 격자 밖으로 나가면 방향을 바꿈
        else:
            if ny < 0:
                run_d = 2  # 하향
            elif nx < 0:
                run_d = 1  # 우향
            elif ny == n:
                run_d = 0  # 상향
            elif nx == n:
                run_d = 3  # 좌향

            ny = run_y + dy[run_d]
            nx = run_x + dx[run_d]

            # 움직이려는 위치에 술래가 있으면 방향만 바꾸고 제자리에
            if (nx, ny) == (catcher_x, catcher_y):
                new_runner.append([run_x, run_y, run_d])
            else:
                new_runner.append([nx, ny, run_d])

    # 도망자 리스트 업데이트
    runner = new_runner


# 술래가 도망자를 잡는 함수
def catcher_catch(turn: int, score: int) -> None:
    """
    술래가 주어진 턴에 도망자를 잡는 함수.

    Args:
        turn (int): 현재 턴 번호
        score (int): 현재 턴의 점수
    """
    global answer
    if turn == 47:
        turn = -1

    catcher_x, catcher_y, catcher_d = catcher_path[turn + 1]

    # 3칸까지 잡기 시도
    for i in range(3):
        nx = catcher_x + (dx[catcher_d] * i)
        ny = catcher_y + (dy[catcher_d] * i)

        # 격자 내에 있을 경우
        if 0 <= nx < n and 0 <= ny < n:
            for idx, run in enumerate(runner):
                # 나무가 있으면 잡을 수 없음
                if (nx, ny) in tree:
                    continue
                # 도망자를 잡았을 경우
                elif (nx, ny) == (run[0], run[1]):
                    answer = answer + score + 1
                    runner[idx] = [-1, -1, -1]  # 도망자를 잡았음을 표시


# 술래의 이동 경로를 계산하는 함수
def get_catcher_path() -> list[list[int]]:
    """
    술래의 이동 경로를 계산하여 반환하는 함수.

    Returns:
        list[list[int]]: 술래가 이동할 경로 (좌표와 방향)
    """
    path = []
    x, y = n // 2, n // 2  # 시작 위치 (격자 중앙)
    distance = 1  # 각 방향으로 이동할 거리
    direction = 0  # 현재 방향 (상, 우, 하, 좌)

    while len(path) < n * n:
        for _ in range(2):
            for __ in range(distance):
                path.append([x, y, direction])
                if len(path) == n * n:
                    return path
                x += dx[direction]
                y += dy[direction]
            direction = (direction + 1) % 4  # 방향 전환
        distance += 1  # 이동 거리 증가

    return path


# 술래의 역방향 이동 경로를 계산하는 함수
def get_catcher_reverse_path() -> list[list[int]]:
    """
    술래의 역방향 이동 경로를 계산하여 반환하는 함수.

    Returns:
        list[list[int]]: 술래의 역방향 이동 경로 (좌표와 방향)
    """
    path = []

    # 좌상단부터 우측으로 진행하는 경로
    for i in range(n - 1):
        path.append([0, i, 2])

    x, y = 0, n - 1  # 시작 위치
    distance = n - 1
    direction = 1  # 초기 방향 (우향)

    while len(path) < (n * n) - 1:
        for _ in range(2):
            for __ in range(distance):
                path.append([x, y, direction])
                if len(path) == (n * n) - 1:
                    return path
                x += dx[direction]
                y += dy[direction]
            direction = (direction - 1) % 4  # 방향 전환
        distance -= 1  # 이동 거리 감소

    return path


# 술래의 경로 설정
catcher_path = get_catcher_path()
catcher_reverse_path = get_catcher_reverse_path()
catcher_path = catcher_path[:-1] + catcher_reverse_path

# 도망자와 나무 좌표 조정 (1-indexed에서 0-indexed로 변환)
for i in range(len(runner)):
    runner[i] = [runner[i][1] - 1, runner[i][0] - 1, runner[i][2]]

for i in range(len(tree)):
    tree[i] = (tree[i][1] - 1, tree[i][0] - 1)

# 시뮬레이션 시작
for idx in range(k):
    runner_move(idx % 48)  # 도망자 이동
    catcher_catch(idx % 48, idx)  # 술래 잡기

# 최종 답안 출력
print(answer)
