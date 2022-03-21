import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

N = int(input())

# 트리
Tree = [[] for _ in range(N+1)]

# 부모 노드 저장
parent = [0] * (N+1)

# 트리 구조 입력
for _ in range(N-1):
    a, b = map(int, input().split())
    Tree[a].append(b)
    Tree[b].append(a)


def DFS(start, tree, parent):
    # 연결 된 노드들부터 parents[i]의 부모가 없으면 부모 설정 해주고, DFS에 넣는다.
    for i in tree[start]:
        if parent[i] == 0:
            parent[i] = start
            DFS(i, tree, parent)


DFS(1, Tree, parent)

for i in range(2, N+1):
    print(parent[i])
