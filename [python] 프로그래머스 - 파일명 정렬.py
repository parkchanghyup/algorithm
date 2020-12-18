def solution(files):
    answer=[]
    _list=[]
    for s in files:
        _s=''
        for char in s:
            if char.isdigit():
                break
            _s+=char
        _n=''
        for char in s[len(_s):]:
            if not char.isdigit():
                break
            _n+=char

        _list.append([_s.lower(),int(_n),s])
        
    s_list = sorted(_list, key=lambda x:(x[0],x[1]))
    for i in s_list:
        answer.append(i[2])
    return answer
