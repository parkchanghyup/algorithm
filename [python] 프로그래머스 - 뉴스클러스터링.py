import re
import collections
# 뉴스 클러스터링
def solution(str1: str, str2: str) -> int:
    answer = 0
    A =  [str1[i:i+2].lower() for i  in range(len(str1)-1)\
         if re.findall('[a-z]{2}',str1[i:i+2].lower())]
    
    B = [str2[i:i+2].lower() for i in range(len(str2)-1)\
        if re.findall('[a-z]{2}',str2[i:i+2].lower())]
    
    cnt_A = collections.Counter(A)
    cnt_B = collections.Counter(B)

    gyo = sum((cnt_A & cnt_B).values())
    hap = sum((cnt_A | cnt_B).values())
    
    if hap == 0:
        if gyo ==0 : return 65536
        return 0
    return int(gyo / hap * 65536)