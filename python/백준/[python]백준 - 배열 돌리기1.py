# 배열 돌리기 시리즈
def rotate():
    '''
    '''
    max_depth = min(N,M) // 2
    depth = 0
    new_arr = [[0] * M for _ in range(N)]

    while depth < max_depth:
        temp = arr[depth][depth]
        
        # left
        for i in range(depth ,M - depth-1):
            new_arr[depth][i] = arr[depth][i+1]
        # up
        for i in range(depth, N-depth-1):
            new_arr[i][M-depth-1] = arr[i+1][M-depth-1]
        
        
        # right
        for i in range(M - depth - 2,-1+ depth, -1):
            new_arr[N - depth-1][i+1] = arr[N - depth-1][i] 

        # down
        for i in range(N - depth - 2,-1 + depth, -1):
            new_arr[i+1][depth] = arr[i][depth]

        depth +=1
        new_arr[depth+1][depth] = temp

    return new_arr
        

N, M, R = map(int,input().split())

arr =  []

for i in range(N):
    arr.append(list(map(int,input().split())))

for _ in range(R):
    arr = rotate()
    for row in arr:
        print(row)

    
