from collections import deque,Counter


N, K = list(map(int,input().split()))
belt = deque(map(int,input().split()))
robot = deque([0] * len(belt))

result = 0
while True:
    # 회전
    robot.appendleft(robot.pop())
    belt.appendleft(belt.pop())

    robot[N-1] = 0

    # 강아지 이동
    for i in range(N-2, -1, -1):

        if robot[i+1] == 0 and belt[i+1] > 0 and robot[i] == 1:

            robot[i+1] = 1
            robot[i] = 0
            belt[i+1] -= 1
    robot[N-1] = 0

    if belt[0] > 0 :
        robot[0] = 1
        # 내구도 감소
        belt[0] -= 1

    result += 1

    if belt.count(0) >= K:
        break

print(result)


