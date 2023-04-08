
import sys


def get_candidate(member):
    """
    수열
    """
    visited = [0] * len(member)
    result = []

    def permutate(cand, visited):
        if len(cand) == len(member):
            result.append(cand)
            return

        for idx, num in enumerate(member):
            if visited[idx] == 0:
                visited[idx] = 1
                permutate(cand+[num],visited)
                visited[idx] = 0

    permutate([],visited)
    return result

def play_game(member,game):
    """
    게임진행
    """
    cnt = 0
    score = 0
    for i in range(len(game)):
        out = 0

        b1, b2 ,b3 = 0 ,0 ,0
        while out < 3:
            if cnt > 8:
                cnt = 0

            type = game[i][member[cnt]]

            if type == 0:
                out += 1
            elif type == 1:
                score += b3
                b3, b2, b1 = b2, b1 ,1

            elif type == 2:
                score += b3 + b2
                b3, b2, b1 = b1, 1 ,0

            elif type == 3:
                score += b3+b2+b1
                b3, b2, b1 = 1, 0, 0
            else :
                score += b3+b2+b1 + 1
                b3, b2, b1 = 0,0,0
            cnt += 1

    return score


n = int(sys.stdin.readline())
game = [[] * n for _ in range(n)]
for i in range(n):
    game[i] = list(map(int, sys.stdin.readline().split()))

player_cands = get_candidate([1,2,4,3,5,6,7,8])
max_result = 0

for cand in player_cands:

    member = cand[:3] + [0] + cand[3:]

    score = play_game(member, game)
    max_result = max(max_result, score)

    # print(score)
print(max_result)
