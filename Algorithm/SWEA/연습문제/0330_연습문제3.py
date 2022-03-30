import sys
sys.stdin = open('0330_2.txt')

# 전위 순회
def preorder(start_node):
    if start_node:
        # 루트 방문
        print(start_node, end=' ')
        # 왼쪽 방문
        preorder(tree[start_node][0])
        # 오른쪽 방문
        preorder(tree[start_node][1])
# 중위 순회
def inorder(start_node):
    if start_node:
        inorder(tree[start_node][0])
        print(start_node, end=' ')
        inorder(tree[start_node][1])

# 후위 순회
def postorder(start_node):
    if start_node:
        postorder(tree[start_node][0])
        postorder(tree[start_node][1])
        print(start_node, end=' ')

V, E = map(int, input().split())
edges = list(map(int, input().split()))
tree = [[0 for _ in range(3)] for _ in range(V+1)]

# 2칸씩 건너 뛰면서 입력값 반복
for i in range(0, len(edges)-1, 2):
    parent_node = edges[i] # 부모노드 (현재노드)
    child_node = edges[i+1]
    # 만약 왼쪽 자식이 비어있으면 넣고.
    if tree[parent_node][0] == 0:
        tree[parent_node][0] = child_node

    # 그렇지 않으면 오른쪽 자식
    else:
        tree[parent_node][1] = child_node

    # 자식 노드의 부모 설정
    tree[child_node][2] = parent_node

# tree 출력
for i in range(V+1):
    print(tree[i])

print('전위순회 : ', end='')
start_node = 1
preorder(start_node)
print()

print('중위순회 : ', end='')
inorder(start_node)
print()

print('후위순회 : ', end='')
postorder(start_node)
