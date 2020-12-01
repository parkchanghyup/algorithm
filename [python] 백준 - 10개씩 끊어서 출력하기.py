# 열 개씩 끊어서 출력하기

s =input()

for i in range(0,len(s),10):
    print(s[i:i+10])
    
