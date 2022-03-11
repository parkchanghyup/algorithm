def solution(rows, columns, queries):
    answer = []
    arr = []
    for i in range(columns):
        tmp=[]
        for j in range(1,rows+1):
            tmp.append(j+i*rows)
        arr.append(tmp)
    
    for a,b,c,d in queries:
        # 5 1 6 3
        a -=1
        b -=1
        c -=1
        d -=1
        tmp = arr[a][d]
        small = tmp

        for i in range(a+1,c+1):
            arr[i-1][b] = arr[i][b]
            small = min(small, arr[i][b])

        for i in range(b+1,d+1):
            arr[c][i-1] = arr[c][i]
            small = min(small, arr[c][i])
        
        for i in range(c-1,a,-1):
            arr[i+1][b] = arr[i][b]
            small = min(small, arr[i][b])
                     

            
        for i in range(d-1, b-1 ,-1):
            arr[a][i+1] = arr[a][i]
            small = min(small, arr[a][i])
            
        
        arr[a][b+1] = tmp

        print(arr)
        break
        
        answer.append(small)
    print(answer)
        
    return answer

solution(6,6 ,[[2,2,5,4],[3,3,6,6],[5,1,6,3]])