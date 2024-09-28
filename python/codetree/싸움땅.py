from collections import deque
from typing import List, Tuple, Dict

# 방향 상수 (상, 우, 하, 좌)
DX = [0, 1, 0, -1]
DY = [-1, 0, 1, 0]


def read_input() -> Tuple[int, int, int, List[List[int]], List[List[int]]]:
    """입력을 받아 배열의 크기, 플레이어 정보를 반환하는 함수"""
    n, m, k = map(int, input().split())  # n: 격자 크기, m: 플레이어 수, k: 턴 수
    arr = [list(map(int, input().split())) for _ in range(n)]  # 격자 상태
    player = [list(map(int, input().split())) for _ in range(m)]  # 플레이어 상태
    return n, m, k, arr, player


def check_user(player: Dict[int, List[int]], x: int, y: int, u_idx: int) -> int:
    """같은 위치에 있는 다른 플레이어가 있는지 확인하는 함수"""
    for idx, (xx, yy, d, s, g) in player.items():
        if idx == u_idx:
            continue
        if (xx, yy) == (x, y):
            return idx
    return -1


def move_player(arr: List[List[List[int]]], player: Dict[int, List[int]], results: List[int]) -> Tuple[List[List[List[int]]], Dict[int, List[int]], List[int]]:
    """플레이어를 이동시키는 함수"""
    n = len(arr)

    for idx, (x, y, d, s, g) in player.items():
        # 한 칸 이동
        nx, ny = x + DX[d], y + DY[d]

        # 이동 가능한 경우
        if 0 <= nx < n and 0 <= ny < n:
            player[idx] = [nx, ny, d, s, g]
        # 이동 불가능한 경우 반대 방향으로 이동
        else:
            d = (d + 2) % 4
            nx, ny = x + DX[d], y + DY[d]
            player[idx] = [nx, ny, d, s, g]

        # 다른 플레이어 확인 및 싸움 처리
        user_idx = check_user(player, nx, ny, idx)
        if user_idx != -1:
            player, arr, results = fight_player(player, idx, user_idx, arr, results)
        else:
            # 총을 줍는 처리
            player[idx], arr = get_gun(player[idx], arr)

    return arr, player, results


def end_game(idx_1: int, idx_2: int, arr: List[List[List[int]]], player: Dict[int, List[int]]) -> Tuple[Dict[int, List[int]], List[List[List[int]]]]:
    """게임에서 승자와 패자를 처리하는 함수"""
    winner = player[idx_1]
    loser = player[idx_2]
    x, y = winner[0], winner[1]
    n = len(arr)

    # 패배자는 총을 내려둠
    loser_gun = loser[4]
    loser[4] = 0
    guns = arr[y][x]

    if loser_gun:
        guns.append(loser_gun)

    arr[y][x] = sorted(guns, reverse=True)

    def check_user(nx: int, ny: int) -> bool:
        """해당 좌표에 다른 플레이어가 있는지 확인"""
        for idx, (xx, yy, _, _, _) in player.items():
            if idx == idx_2:
                continue
            if (xx, yy) == (nx, ny):
                return False
        return True

    # 패배자 이동 처리
    x, y, d, s, g = loser
    while True:
        nx, ny = x + DX[d], y + DY[d]
        if 0 <= nx < n and 0 <= ny < n:
            if check_user(nx, ny):
                loser = [nx, ny, d, s, arr[ny][nx][0]] if arr[ny][nx] else [nx, ny, d, s, 0]
                arr[ny][nx] = arr[ny][nx][1:] if arr[ny][nx] else []
                break
        d = (d + 1) % 4

    # 승리자 총 줍기
    winner, arr = get_gun(winner, arr)

    player[idx_1], player[idx_2] = winner, loser
    return player, arr


def fight_player(player: Dict[int, List[int]], idx_1: int, idx_2: int, arr: List[List[List[int]]], results: List[int]) -> Tuple[Dict[int, List[int]], List[List[List[int]]], List[int]]:
    """플레이어 간 싸움 처리"""
    user_1 = player[idx_1]
    user_2 = player[idx_2]

    user_1_power = user_1[3] + user_1[4]  # 사용자 1의 총합 전투력
    user_2_power = user_2[3] + user_2[4]  # 사용자 2의 총합 전투력

    if user_1_power > user_2_power:
        results[idx_1] += (user_1_power - user_2_power)
        player, arr = end_game(idx_1, idx_2, arr, player)
    elif user_1_power < user_2_power:
        results[idx_2] += (user_2_power - user_1_power)
        player, arr = end_game(idx_2, idx_1, arr, player)
    else:
        if user_1[3] > user_2[3]:
            player, arr = end_game(idx_1, idx_2, arr, player)
        else:
            player, arr = end_game(idx_2, idx_1, arr, player)

    return player, arr, results


def get_gun(user: List[int], arr: List[List[List[int]]]) -> Tuple[List[int], List[List[List[int]]]]:
    """플레이어가 해당 위치에서 총을 줍는 함수"""
    x, y, d, s, g = user

    if arr[y][x] and g < arr[y][x][0]:
        temp_ = arr[y][x]
        if g != 0:
            temp_.append(g)
        g = arr[y][x][0]
        arr[y][x] = sorted(temp_[1:], reverse=True)
        user = [x, y, d, s, g]

    return user, arr


def main() -> None:
    """메인 함수: 시뮬레이션 실행 및 결과 출력"""
    n, m, k, temp_arr, temp_player = read_input()
    results = [0] * m

    # 총이 여러 개 있을 수 있으므로 arr 배열을 다차원 리스트로 변환
    arr = [[[num] for num in row] for row in temp_arr]

    # 플레이어를 dict로 관리
    player = {idx: [y - 1, x - 1, d, s, 0] for idx, (x, y, d, s) in enumerate(temp_player)}

    # k번의 턴 동안 플레이어 이동 및 처리
    for _ in range(k):
        arr, player, results = move_player(arr, player, results)

    print(" ".join(map(str, results)))


if __name__ == "__main__":
    main()
