'''
bin 함수를 통해 지도를 생성해주고
zfill 함수를 통해 지도의 크기에 맞춰준다.
그리고 1을 # 으로 0을 ' '으로 변환해준다.
'''


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