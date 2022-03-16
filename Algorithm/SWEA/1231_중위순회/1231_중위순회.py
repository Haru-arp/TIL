import sys
sys.stdin = open('input.txt')


def in_order(v):
    if v <= N:
        in_order(v*2)
        print(alp_lst[v], end='')
        in_order(v*2+1)

T = 10
for tc in range(1, T+1):
    N = int(input())
    alp_lst = [0] * (N+1)
    for i in range(N):
        li = list(input().split())
        alp_lst[i+1] = li[1]
    print(f'#{tc}', end=' ')
    in_order(1)
    print()

