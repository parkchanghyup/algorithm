import sys
from collections import deque, defaultdict
from typing import List, Tuple

# 입력을 받는 함수
def read_input() -> Tuple[int, int, int, List[List[int]]]:
    n, m, k = list(map(int, sys.stdin.readline().split()))  # n, m, k 값 입력받기
    arr = [list(map(int, input().split())) for _ in range(n)]  # 2D 배열 입력받기
    return n, m, k, arr

# 그룹을 회전시키는 함수 (구현 필요)
def turn_group(groups):
    pass

# 특정 좌표에 대한 점수 계산 함수
def calculate_score(group, y, x):
    score = 0
    # 해당 좌표의 점수를 계산
    for idx, (yy, xx) in enumerate(group):
        if (yy, xx) == (y, x):
            score = (idx + 1) ** 2  # 점수는 인덱스의 제곱
            break
    group = group[::-1]  # 그룹을 역순으로 정렬
    return score, group

# 공을 던져 맞는 그룹을 찾고 점수를 계산하는 함수
def shoot_ball(arr, groups, turn):
    n = len(arr)
    line = turn % n
    direction = (turn % (4 * n)) // n  # 방향을 결정하는 변수

    def hit_check(i, j, is_vertical):
        # 공이 맞는지 확인하는 내부 함수
        if arr[i][j] > 4:
            group_num = arr[i][j]
            score, group = calculate_score(groups[group_num], i, j)
            groups[group_num] = group  # 그룹을 업데이트
            return score, groups
        return 0, groups

    if direction == 0:  # 우
        for j in range(n):
            score, groups = hit_check(line, j, False)
            if score > 0:
                return score, groups
    elif direction == 1:  # 상
        for i in range(n - 1, -1, -1):
            score, groups = hit_check(i, line, True)
            if score > 0:
                return score, groups
    elif direction == 2:  # 좌
        line = n - line - 1
        for j in range(n - 1, -1, -1):
            score, groups = hit_check(line, j, False)
            if score > 0:
                return score, groups
    elif direction == 3:  # 하
        line = n - line - 1
        for i in range(n):
            score, groups = hit_check(i, line, True)
            if score > 0:
                return score, groups

    return 0, groups  # 맞는 그룹이 없으면 0점 반환

# 그룹을 이동시키는 함수
def move_group(arr, groups):
    dx = [0, 1, -1, 0]  # x축 이동 방향
    dy = [1, 0, 0, -1]  # y축 이동 방향
    n = len(arr)

    for team_num in groups.keys():
        team = groups[team_num]

        # 꼬리 좌표를 미리 4로 변경
        ty, tx = team[-1]
        arr[ty][tx] = 4

        # 머리가 이동할 좌표 구하기
        y, x = team[0]
        for d in range(4):
            hy = y + dy[d]
            hx = x + dx[d]
            if 0 <= hy < n and 0 <= hx < n and arr[hy][hx] == 4:
                arr[hy][hx] = team_num  # 새로운 머리 좌표 설정
                break

        # 팀 좌표 업데이트 (머리 이동, 꼬리 제거)
        groups[team_num] = [(hy, hx)] + team[:-1]

    return arr, groups

# 특정 좌표에서 그룹을 추출하는 함수
def get_group(arr, i, j):
    n = len(arr)
    visited = [[0] * n for _ in range(n)]  # 방문 체크 배열

    dx = [0, 1, -1, 0]  # x축 이동 방향
    dy = [1, 0, 0, -1]  # y축 이동 방향

    group = [(i, j)]
    queue = deque([(i, j)])  # BFS 탐색을 위한 큐
    visited[i][j] = 1

    while queue:
        y, x = queue.popleft()

        for d in range(4):
            ny, nx = y + dy[d], x + dx[d]

            if 0 <= ny < n and 0 <= nx < n and not visited[ny][nx]:
                if arr[ny][nx] == 2 or (arr[y][x] == 2 and arr[ny][nx] == 3):
                    group.append((ny, nx))
                    queue.append((ny, nx))
                    visited[ny][nx] = 1

    return group

# 메인 실행 함수
def main():
    n, m, k, arr = read_input()  # 입력 데이터 받기

    answer = 0
    team_num = 5  # 그룹 번호는 5번부터 시작
    groups = defaultdict(list)

    # 그룹 탐색 및 팀 번호 부여
    for i in range(n):
        for j in range(n):
            if arr[i][j] == 1:
                group = get_group(arr, i, j)
                groups[team_num] = group
                team_num += 1

    # 기존 배열에 팀 번호 표시
    for team_num in groups.keys():
        for y, x in groups[team_num]:
            arr[y][x] = team_num

    # 턴마다 게임 진행
    for turn in range(k):
        arr, groups = move_group(arr, groups)  # 그룹 이동
        score, groups = shoot_ball(arr, groups, turn)  # 공 던지기 및 점수 계산
        answer += score  # 점수 누적

    print(answer)  # 최종 점수 출력

# 프로그램 실행
if __name__ == "__main__":
    main()
