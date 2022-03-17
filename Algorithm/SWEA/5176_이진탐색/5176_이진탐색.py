import sys
sys.stdin = open('input.txt')

def inorder(v):
    global cnt
    # 배열 크기 넘어가지 않도록 범위 정해주기
    if v <= N:
        # 왼쪽 노드는 현재 인덱스의 2배
        inorder(2*v)
        # 더이상 못 가면 값 넣어주기
        tree[v] = cnt
        # 값 넣었으면 증가
        cnt += 1
        # 우측 노드는 인덱스 2배 + 1
        inorder(2*v+1)


T = int(input())
for tc in range(1, T+1):

    N = int(input())
    tree = [0 for _ in range(N+1)]
    cnt = 1
    inorder(1)

    print(f'#{tc} {tree[1]} {tree[N//2]}')