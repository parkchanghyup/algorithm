class Node:
    def __init__(self,data,left_node, right_node):
        self.data = data
        self.left_node = left_node
        self.right_node = right_node

# 전위 순회
def pre_order(node):
    print(node.data, end = '')
    if node.left_node != None:
        pre_order(tree[node.left_node])
    if node.right_node != None:
        pre_order(tree[node.right_node])

# 중위 순회
def in_order(node):
    
    if node.left_node != None:
        in_order(tree[node.left_node])
    print(node.data, end = '')
    if node.right_node != None:
        in_order(tree[node.right_node])
        
#후위 순회
def post_order(node):
    
    if node.left_node != None:
        post_order(tree[node.left_node])
    if node.right_node != None:
        post_order(tree[node.right_node])
    print(node.data, end = '')
    
n = int(input())
tree ={}


for i in range(n):
    data, left_node, right_node = input().split()
    # '.' 으로 입력받은값을 None로 바꿔줌
    if left_node == '.':
        left_node = None
        
    if right_node =='.':
        right_node = None
    # 트리생성
    tree[data] = Node(data, left_node, right_node)

#전위순회
pre_order(tree['A'])
print()
#중위순회
in_order(tree['A'])
print()
#후위순회
post_order(tree['A'])

