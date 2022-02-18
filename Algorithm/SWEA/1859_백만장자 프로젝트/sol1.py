import sys

sys.stdin = open('input.txt')

T = int(input())


for tc in range(1, T + 1):
    N = int(input())
    lst = list(map(int, input().split()))
    sol = s = maxI = 0
    while s < N:
        maxI = s
        for i in range(s, N):
            if lst[maxI] < lst[i]:
                maxI = i

        for i in range(s, maxI):
            sol += lst[maxI] - lst[i]

        s = maxI + 1

    print(f'#{tc} {sol}')

