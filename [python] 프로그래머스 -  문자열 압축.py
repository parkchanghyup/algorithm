#문자열과 압출할 문자수
def func(s:str,n:int)->int:
    result=[]
    for i in range(n,len(s)+1,n):

        result.append(s[i-n:i])
    cnt = 0
    for i in range(len(result)):
        cnt +=len(result[i])
    result.append(s[cnt:])
    cnt = 1
    ans = ''

    
    for i in range(1,len(result)):
        if result[i-1]==result[i]  :
            cnt +=1
        else :
            if cnt ==1 :
                ans+=result[i-1]
            else :
                ans += str(cnt)+result[i-1]
            cnt=1
    
    
    if cnt ==1 :
        ans+=result[i]
    else :
        ans += str(cnt)+result[i]

    return len(ans)
    
    
def solution(s):
    answer = 0
    min_num = len(s)
    for i in range(1,int(len(s)/2)+1):
        min_num =min(min_num , func(s,i))
    return  min_num