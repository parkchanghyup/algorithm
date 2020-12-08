from typing import List
#프렌즈4블록


# m : 세로 , n : 가로
def solution(m: int, n: int, board: List[str]) -> int:
    board = [list(x) for x in board]
    answer = 0
    index = True
    while index:
        index = []
        #매칭 되는 블록
        for i in range(m - 1):
            for j in range(n - 1):
                if board[i][j] == board[i][j + 1] == board[i + 1][j] == board[
                        i + 1][j + 1] and board[i][j] != '#':
                    index.append([i, j])

        # 매칭 되는 블록 삭제
        for i, j in index:
            board[i][j] = '#'
            board[i][j + 1] = '#'
            board[i + 1][j] = '#'
            board[i + 1][j + 1] = '#'
        for _ in range(m-1):
            for i in range(m - 1):
                for j in range(n):
                    if board[i + 1][j] == '#':
                        board[i + 1][j], board[i][j] = board[i][j], '#'
    
    
    for i in range(m):
        for j in range(n):
            if board[i][j] == '#':
                answer += 1

    return answer