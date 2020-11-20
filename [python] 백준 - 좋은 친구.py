
from collections import deque
import collections
N,K = map(int,input().split())

names = []

for i in range(N):
    names.append(input())
    
result = 0
dic = collections.defaultdict(int)
Q = deque()

for idx,name in enumerate(names):
    
    # K 등수 이내만 좋은친구 .
    if len(Q) == K+1 :
        name_len = len(Q.popleft())
        dic[name_len] -=1
        result += dic[name_len] 
    
    Q.append(name)
    dic[len(name)]+=1
    

# Q내에 남아있는 사람들 처리.
while Q:
    name_len = len(Q.popleft())
    dic[name_len] -=1
    result += dic[name_len] 
    
    
print(result)