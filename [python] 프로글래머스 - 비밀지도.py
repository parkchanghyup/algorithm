#2018 KAKAO BLIND RECRUITMENT #[1차] 비밀지도
from typing import List
def solution(n:int, arr1:List[int], arr2:List[int])->List[str]:
    answer = []
    for i in range(n):
        answer.append(bin(arr1[i]|arr2[i])[2:].
                      zfill(n).
                      replace('1','#').
                      replace('0',' ')
                     )
        
    return answer
solution(6, [46, 33, 33, 22, 31, 50], [27, 56, 19, 14, 14, 10])