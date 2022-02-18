import sys

sys.stdin = open('input.txt')

T = int(input())


for tc in range(1, T + 1):
    N, Q = map(int, input().split())
    lst = [0]*(N+1)
    for q in range(1, Q+1):
        L, R = map(int, input().split())
        for i in range(L, R+1):
            lst[i] = q

    print(f'#{tc}', *lst[1:])

