import sys
sys.stdin = open('input.txt')

def sol(root):
    global cnt
    if tree[root][0]:
        cnt += 1
        sol(tree[root][0])
    if tree[root][1]:
        cnt += 1
        sol(tree[root][1])

T = int(input())
for tc in range(1, T+1):

    E, N = map(int, input().split()) #간선 개수, root
    arr = list(map(int, input().split())) #부모 자식
    # 2 1 2 5 1 6 5 3 6 4
    tree = [[0] * 3 for _ in range(E+2)]
    for i in range(E):
        # [왼쪽 자식, 오른쪽 자식, 부모 노드]
        parent_node, child_node = arr[i*2], arr[i*2+1]
        tree[child_node][2] = parent_node
        if not tree[parent_node][0]:
            tree[parent_node][0] = child_node
        else:
            tree[parent_node][1] = child_node

    cnt = 1
    sol(N)

    print(f'#{tc} {cnt}')