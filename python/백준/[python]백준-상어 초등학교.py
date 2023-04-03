dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]


def check_friend(graph, number):
    me = number[0]
    friend = number[1:]
    max_friend = []
    max_cnt = 0
    check_graph = [[0] * len(graph) for _ in range(len(graph))]

    for i in range(len(graph)):
        for j in range(len(graph)):
            cnt = 0
            if graph[i][j] == 0:
                for d in range(4):
                    nx = j + dx[d]
                    ny = i + dy[d]
                    if nx >= 0 and nx < len(graph) and ny >= 0 and ny < len(graph):
                        if graph[ny][nx] in friend:
                            cnt += 1
                if max_cnt == cnt:
                    max_friend.append((i, j))
                elif max_cnt < cnt:
                    max_cnt = cnt
                    max_friend = [(i, j)]

    return max_friend


def check_blank(graph, pos):
    max_blank = []
    max_cnt = 0
    for (y, x) in pos:
        cnt = 0
        if graph[y][x] == 0:
            for d in range(4):
                nx = x + dx[d]
                ny = y + dy[d]
                if nx >= 0 and nx < len(graph) and ny >= 0 and ny < len(graph) :
                    if graph[ny][nx] == 0:
                        cnt += 1
        if max_cnt == cnt:
            max_blank.append((y, x))
        elif max_cnt < cnt:
            max_cnt = cnt
            max_blank = [(y, x)]
    # print('max_blank : ', max_blank)
    return max_blank


n = int(input())
numbers = []
for i in range(n * n):
    temp = input().split()
    numbers.append([int(x) for x in temp])


graph = [[0] * n for _ in range(n)]
num_pos = []
for i in range(n * n):
    number = numbers[i]

    if graph[1][1] == 0:
        graph[1][1] = number[0]
        num_pos.append((1,1))

    else:
        # 1번 조건
        pos = check_friend(graph, number)
        if len(pos) == 1:
            # 1번 조건 만족
            y = pos[0][0]
            x = pos[0][1]
            graph[y][x] = number[0]
            num_pos.append((y,x))
        # 1번 조건 만족하지만 위치가 여러개.
        else:
            # 2번 조건
            pos = check_blank(graph, pos)
            # 2번조건 만족
            if len(pos) == 1:
                y = pos[0][0]
                x = pos[0][1]
                graph[y][x] = number[0]
                num_pos.append((y, x))
            else:
                # 3번 조건 & 4번조건

                #pos.sort()
                y = pos[0][0]
                x = pos[0][1]
                graph[y][x] = number[0]
                num_pos.append((y, x))


result = 0
score_dic ={0:0,1:1,2:10,3:100,4:1000}

# 점수 계산
for y in range(n):
    for x in range(n):
        for num in numbers:
            if num[0] == graph[y][x]:


        #number = numbers[i*3+j]
        #y, x = num_pos[i*3+j]
                friend = num[1:]

                cnt = 0
                for d in range(4):
                    nx =  x+ dx[d]
                    ny = y+ dy[d]

                    if nx >= 0 and nx < len(graph) and ny >= 0 and ny < len(graph):
                        temp = graph[ny][nx]
                        if graph[ny][nx] in friend:
                            cnt += 1



                result += score_dic[cnt]


print(result)