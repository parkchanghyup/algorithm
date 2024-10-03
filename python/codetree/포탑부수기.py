import sys
from collections import deque
from typing import List, Tuple, Dict


def read_input() -> Tuple[int, int, int, List[List[int]]]:
    """
    표준 입력으로부터 게임 설정과 초기 포탑 상태를 읽어옵니다.

    Returns:
        Tuple[int, int, int, List[List[int]]]: 행의 수, 열의 수, 턴 수, 초기 포탑 배열
    """
    n, m, k = map(int, sys.stdin.readline().split())
    arr = []
    for _ in range(n):
        arr.append(list(map(int, sys.stdin.readline().split())))

    return n, m, k, arr


def get_weak_tower(arr: List[List[int]], tower_last_attack: Dict[Tuple[int, int], int]) -> Tuple[int, int]:
    """
    가장 약한 포탑을 선정합니다.

    Args:
        arr (List[List[int]]): 현재 포탑 배열
        tower_last_attack (Dict[Tuple[int, int], int]): 각 포탑의 마지막 공격 턴

    Returns:
        Tuple[int, int]: 가장 약한 포탑의 좌표
    """
    n = len(arr)
    m = len(arr[0])

    weak_tower = []
    weak_attack = int(1e9)
    for i in range(n):
        for j in range(m):
            if arr[i][j] == 0:
                continue
            if arr[i][j] == weak_attack:
                weak_tower.append((i, j))
            elif arr[i][j] < weak_attack:
                weak_attack = arr[i][j]
                weak_tower = [(i, j)]

    if len(weak_tower) == 1:
        return weak_tower[0]

    last_attack = 0
    weak_tower_2 = []
    for (i, j) in weak_tower:
        if tower_last_attack[(i, j)] == last_attack:
            weak_tower_2.append((i, j))
        elif tower_last_attack[(i, j)] > last_attack:
            weak_tower_2 = [(i, j)]
            last_attack = tower_last_attack[(i, j)]

    weak_tower_2 = sorted(weak_tower_2, key=lambda x: (-(x[0] + x[1]), -x[1]))

    return weak_tower_2[0]


def get_target_tower(arr: List[List[int]], tower_last_attack: Dict[Tuple[int, int], int],
                     weak_tower: Tuple[int, int]) -> Tuple[int, int]:
    """
    가장 강한 포탑(공격 대상)을 선정합니다.

    Args:
        arr (List[List[int]]): 현재 포탑 배열
        tower_last_attack (Dict[Tuple[int, int], int]): 각 포탑의 마지막 공격 턴
        weak_tower (Tuple[int, int]): 가장 약한 포탑의 좌표

    Returns:
        Tuple[int, int]: 가장 강한 포탑의 좌표
    """
    n = len(arr)
    m = len(arr[0])

    target_tower = []
    strong_tower = 0

    for i in range(n):
        for j in range(m):
            if (i, j) == weak_tower or arr[i][j] == 0:
                continue
            if strong_tower == arr[i][j]:
                target_tower.append((i, j))
            elif strong_tower < arr[i][j]:
                strong_tower = arr[i][j]
                target_tower = [(i, j)]

    if len(target_tower) == 1:
        return target_tower[0]

    last_attack = int(1e9)
    strong_tower_2 = []
    for (i, j) in target_tower:
        if tower_last_attack[(i, j)] == last_attack:
            strong_tower_2.append((i, j))
        elif tower_last_attack[(i, j)] < last_attack:
            strong_tower_2 = [(i, j)]
            last_attack = tower_last_attack[(i, j)]

    strong_tower_2 = sorted(strong_tower_2, key=lambda x: (x[0] + x[1], x[1]))
    if len(strong_tower_2) == 0:
        return ''
    return strong_tower_2[0]


def get_razer_path(arr: List[List[int]], weak_tower: Tuple[int, int], target_tower: Tuple[int, int]) -> List[Tuple[int, int]]:
    """
    레이저 공격 경로를 찾습니다.

    Args:
        arr (List[List[int]]): 현재 포탑 배열
        weak_tower (Tuple[int, int]): 공격하는 포탑의 좌표
        target_tower (Tuple[int, int]): 공격 대상 포탑의 좌표

    Returns:
        List[Tuple[int, int]]: 레이저 공격 경로
    """
    dx = [1, 0, -1, 0]
    dy = [0, 1, 0, -1]

    n = len(arr)
    m = len(arr[0])
    visited = [[0] * m for _ in range(n)]

    q = deque()
    q.append((weak_tower[0], weak_tower[1], []))
    visited[weak_tower[0]][weak_tower[1]] = 1

    while q:
        y, x, path = q.popleft()
        if (y, x) == target_tower:
            return path
        for d in range(4):
            ny = y + dy[d]
            nx = x + dx[d]

            # 격자 밖으로 나가면 반대로가기
            if ny == n:
                ny = 0
            elif nx == m:
                nx = 0
            elif ny < 0:
                ny = n - 1
            elif nx < 0:
                nx = m - 1

            if arr[ny][nx] > 0 and visited[ny][nx] == 0:
                visited[ny][nx] = 1
                q.append((ny, nx, path + [(ny, nx)]))

    return []


def get_bomb_path(arr: List[List[int]], target_tower: Tuple[int, int]) -> List[Tuple[int, int]]:
    """
    포탄 공격 경로를 찾습니다.

    Args:
        arr (List[List[int]]): 현재 포탑 배열
        target_tower (Tuple[int, int]): 공격 대상 포탑의 좌표

    Returns:
        List[Tuple[int, int]]: 포탄 공격 영향을 받는 좌표 목록
    """
    dx = [1, 1, 1, -1, -1, -1, 0, 0]
    dy = [1, -1, 0, 1, -1, 0, 1, -1]

    y, x = target_tower
    n = len(arr)
    m = len(arr[0])
    path = []
    for d in range(8):
        ny = y + dy[d]
        nx = x + dx[d]

        if ny == n:
            ny = 0
        elif ny < 0:
            ny = n - 1

        if nx == m:
            nx = 0
        elif nx < 0:
            nx = m - 1

        path.append((ny, nx))
    return path


def main():
    """
    메인 함수: 게임 로직을 실행합니다.
    """
    n, m, k, arr = read_input()
    tower_last_attack: Dict[Tuple[int, int], int] = {}

    for i in range(n):
        for j in range(m):
            tower_last_attack[(i, j)] = 0

    for t in range(k):
        # 가장 약한 포탑 선정
        weak_tower = get_weak_tower(arr, tower_last_attack)
        # 가장 약한 포탑 강화
        arr[weak_tower[0]][weak_tower[1]] += n + m
        tower_last_attack[weak_tower] = t + 1

        # 가장 강한 포탑 선정
        target_tower = get_target_tower(arr, tower_last_attack, weak_tower)
        if len(target_tower) == 0:
            arr[weak_tower[0]][weak_tower[1]] -= n + m
            break

        razer_path = get_razer_path(arr, weak_tower, target_tower)

        weak_tower_power = arr[weak_tower[0]][weak_tower[1]]

        # 레이저 공격
        if razer_path:
            for (y, x) in razer_path[:-1]:
                arr[y][x] -= weak_tower_power // 2

        # 포탄 공격
        else:
            bomb_attack = get_bomb_path(arr, target_tower)
            for (y, x) in bomb_attack:
                if (y, x) != weak_tower:
                    arr[y][x] -= weak_tower_power // 2

            razer_path = bomb_attack

        arr[target_tower[0]][target_tower[1]] -= weak_tower_power

        razer_path.append(weak_tower)
        razer_path.append(target_tower)

        # check
        check = 0
        for i in range(n):
            for j in range(m):
                if arr[i][j] > 0:
                    check = 1
        if check == 0:
            break

        # 포탑 부서짐 & 정비
        for i in range(n):
            for j in range(m):
                # 포탑 부서짐
                if arr[i][j] <= 0:
                    arr[i][j] = 0
                # 포탑 정비
                elif (i, j) not in razer_path:
                    arr[i][j] += 1

    answer = 0
    for i in range(n):
        for j in range(m):
            if arr[i][j] > answer:
                answer = arr[i][j]

    print(answer)


if __name__ == '__main__':
    main()