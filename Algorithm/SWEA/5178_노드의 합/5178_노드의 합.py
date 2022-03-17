import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    N, M, L = map(int, input().split()) #노드의 계수, 리프 노드의 개수, 출력할 노드 번호
    tree = [0 for _ in range(N+1)]
    for _ in range(M):
        idx, data = map(int, input().split())
        tree[idx] = data

    for i in range(N, 0 , -1):
        if i // 2 > 0:
            tree[i // 2] += tree[i]

    print(f'#{tc} {tree[L]}')