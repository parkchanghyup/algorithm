from collections import deque
from typing import List, Tuple, Set

# 방향 상수 (우, 하, 좌, 상)
DX = [1, 0, -1, 0]
DY = [0, 1, 0, -1]


def read_input() -> Tuple[int, int, int, List[List[int]], List[List[int]]]:
    """입력을 읽어 배열의 크기와 배열을 반환합니다."""
    n, m, k = list(map(int, input().split()))
    arr = []
    player = []

    for _ in range(n):
        arr.append(list(map(int, input().split())))

    for _ in range(m):
        player.append(list(map(int, input().split())))

    return n, m, k, arr, player


def move_player():
    pass

def get_gun():
    pass

def fight_player():
    pass


def main():
    """메인 함수: 시뮬레이션을 실행하고 결과를 출력합니다."""
    n, m, k, arr, player = read_input()
    results = []
    for _ in range(k):
        pass

    for result in results:
        print(result, end = ' ')


if __name__ == "__main__":
    main()

