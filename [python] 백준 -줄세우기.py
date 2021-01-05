# 위상정렬


from collections import deque
import collections

v, e = map(int,input().split())

indegree = [0] *(v+1)

graph = collections.defaultdict(list)

for i in range(e):
    
    a,b= map(int,input().split())
    graph[a].append(b)
    
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
        
        if indegree[a] == 0:
            q.append(a)

for num in result:
    print(num,end = ' ')


