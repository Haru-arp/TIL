"""
13 (노드의 개수)
1 2 1 3 2 4 3 5 3 6 4 7 5 8 5 9 6 10 6 11 7 12 11 13
"""
"""
트리 순회
:트리 순회는 root 노드를 기준으로 생각하면 쉽습니다.
"""
#1. 전위 순회 (preorder)
def preorder(node):
    """
    전위순회를 하는 함수입니다.
    root => 왼쪽 서브트리의 root => 오른쪽 서브트리의 root
    :param node: 노드의 번호입니다. 현재 방문하는 노드입니다.
    :return: 없습니다.
    """
    if node:
        #1. root 방문
        print(node)
        #2. 왼쪽 방문
        preorder(tree[node][0])
        #3. 오른쪽 방문
        preorder(tree[node][1])

#2. 중위 순회 (inorder)
def inorder(node):
    """
    중위 순회 함수입니다.
    왼쪽 서브트리의 root => root => 오른쪽 서브트리의 root
    :param node: 현재 방문하는 노드입니다.
    :return: 없습니다.
    """
    if node:
        inorder(tree[node][0])
        print(node) #현재노드 방문
        inorder(tree[node][1])
#3. 후위 순회 (postorder)
def postorder(node):
    """
    후위 순회 함수입니다.
    왼쪽 서브트리의 root => 오른쪽 서브트리의 root => root
    :param node: 현재 방문하는 노드입니다.
    :return: 없습니다.
    """
    if node:
        postorder(tree[node][0])
        postorder(tree[node][1])
        print(node)



V = int(input())
edges = list(map(int, input().split()))

tree = [[0 for _ in range(3)] for _ in range(V+1)]


#2칸씩 건너 뛰면서 입력값 반복
for i in range(0, len(edges)-1, 2):
    parent_node = edges[i] #부모 노드 (현재 노드)
    child_node = edges[i+1] #자식 노드

    #만약 왼쪽 자식이 비어있으면 넣고
    if tree[parent_node][0] == 0:
        tree[parent_node][0] = child_node

    #그렇지 않으면 오른쪽 자식에 삽입
    else:
        tree[parent_node][1] = child_node

    #자식 노드의 부모 설정
    tree[child_node][2] = parent_node

#tree 출력
for i in range(V+1):
    print(tree[i])

print('=== 전위 순회===')
start_node = 1
preorder(start_node)
print('=== 전위 순회 끝===')

print('=== 중위 순회 ===')
inorder(start_node)
print('=== 중위 순회 끝 ===')

print(' === 후위 순회 ===')
postorder(start_node)
print('=== 후위 순회 끝 ===')