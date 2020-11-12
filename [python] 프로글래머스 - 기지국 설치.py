# 기지국 설치
import math


def solution(N, stations, W):
    answer = 0

    install_length = []
    left = 0
    for idx, s in enumerate(stations):
        install_length.append((s-W) - left-1)
        left = s+W
        
        # 마지막이면 오른쪽도
        if idx == len(stations) - 1:
            install_length.append(N - (s+W))
    print(install_length)
    
    
    install_length = [x for x in install_length if x >= 0]
    
    W = W*2 + 1
    result = 0

    for install in install_length:
        Size = math.ceil(install / W)
        answer += Size
    return answer