

DX = [0,-1,1,0]
DY = [-1,0,0,1]

def read_input():
    n, m = list(map(int,input().split()))

    arr = []
    convs = {}

    for _ in range(n):
        arr.append(list(map(int, input().split())))

    for i in range(m):
        x, y = map(int, input().split())
        convs[i] = (y-1, x-1)

    return n, m, arr, convs

def get_base_camps(arr):
    n = len(arr)
    base_camps = []
    for i in range(n):
        for j in range(n):
            if arr[i][j] == 1:
                base_camps.append((i,j))

    return base_camps

def move_user(conv, arr, user):
    pass

def get_first_base_camp(base_camps, arr, conv):
    c_x, c_y = conv
    min_dist = int(1e9)
    first_base_camp = [-1, 1]
    for b_y, b_x in base_camps:

        # 접근 금지면 못감.
        if arr[b_y][b_x] == -1:
            continue
        dist = abs(b_y - c_y) + abs(b_x - c_x)
        if dist < min_dist:
            min_dist = dist
            first_base_camp = [b_y, b_x]

    return first_base_camp



def main():
    n, m, arr, convs = read_input()
    users = {}

    answer = 0

    base_camps = get_base_camps(arr)
    print(base_camps)
    while answer < m:
        no_access_pos = []

        for conv_num in convs.keys():
            conv = convs[conv_num]
            user = users[conv_num]

            # 이미 도착 하면 continue
            if conv == user:
                continue

            # 격자에 있는 사람들은 편의점 방향을 향해서 1칸 움직임
            move_user(conv, arr, user)

            # 편의점에 도착하면 해당 위치 no_access_pos 로 처리


            # 가장 가까운 베이스캠프로 진입
            y, x = get_first_base_camp(base_camps,arr, conv)
            users[conv_num] = [x, y]

            # 진입 후 no_access_pos 처리
            no_access_pos.append((x, y))
            # print(users, no_access_pos)
            # break

        # no_access_pos 처리
        for x, y in no_access_pos:
            arr[y][x] = -1
        # break

if __name__=='__main__':
    main()

