'''
1. isdigit() 함수를 이용하여 HEAD를 구하고
2. HEAD가 아닌 부분에서 다시 isdigit() 함수를통해 NUMBER을구한다
3. 주어진 조건에따라정렬하여 RETURN
'''



def solution(files):
    answer=[]
    str=[]
    
    for s in files:
        # HEAD
        HEAD=''
        for char in s:
            if char.isdigit():
                break
            HEAD+=char
            
        # NUMBER
        NUMBER=''        
        for char in s[len(HEAD):]:
            if not char.isdigit():
                break
            NUMBER+=char
        
        #HEAD,NUMBER,문자원본
        str.append([HEAD.lower(),int(NUMBER),s])
        
    s_list = sorted(str, key=lambda x:(x[0],x[1]))
    for i in s_list:
        answer.append(i[2])
    return answer
