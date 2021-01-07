'''
답이 여러개 이기때문에 위상정렬을 해주는 것 말고는 딱히 어려운 부분이 없다
'''


from collections import deque
import collections

v, e = map(int,input().split())

#진입차수 처리할 리스트
indegree = [0] *(v+1)

#그래프 생성
graph = collections.defaultdict(list)

for i in range(e):
    
    a,b= map(int,input().split())
    graph[a].append(b)
    
    # 키가 더큰 아이는 진입차수 +1
    indegree[b] +=1
    

# 위상정렬  

q = deque()

# 진입차수가 0인 노드 넣기
for i in range(1,v+1):
    if indegree[i] ==0 :
        q.append(i)
    

result = []    
while q :
    
    node= q.popleft()
    
    result.append(node)
    
    for a in graph[node]:
        indegree[a] -=1
        
        # 진입차수가 0이되면 q에 append
        if indegree[a] == 0:
            q.append(a)

for num in result:
    print(num,end = ' ')


