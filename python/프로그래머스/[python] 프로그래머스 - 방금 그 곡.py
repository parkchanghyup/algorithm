def sharp(m :str):
    re_m= ''

    for i in range(len(m)-1):
        if len(re_m) > i : continue
        if m[i+1] =='#':
            re_m+=m[i].lower()+'#'     
        else:
            re_m+=m[i]
    if len(re_m) != len(m):
        re_m+=m[-1]


    return re_m.replace('#','')
    
def solution(m, musicinfos):
    result = []
    
    if '#' in m:
        m = sharp(m)

        
    
    for s in musicinfos:
        s = s.split(',')
        s[0] = int(s[0][:2]) * 60 + int(s[0][3:])
        s[1] = int(s[1][:2]) * 60 + int(s[1][3:])
        if '#' in s[3]:
            s[3] = sharp(s[3])
        melody = s[3]

        while len(m) > len (melody):
            melody +=s[3]            
        melody+=s[3]

        if m in melody[:s[1]-s[0]] : 
            # 노래길이, 시작시간,노래제목
            result.append([-(s[1] - s[0]) , s[0] , s[2]])

    result = sorted(result)

    if not result:
        return "(None)"
    else :
        return result[0][2]
