import sys

sys.stdin = open('input.txt')

T = int(input())


for tc in range(1, T + 1):
    N, M = map(int, input().split())
    flies = [list(map(int, input().split())) for _ in range(N)]
    max_kill = 0

    for i in range(N-M+1):
        for j in range(N-M+1):
            sum_kill = 0
            for x in range(M):
                for y in range(M):
                    sum_kill += flies[i+x][j+y]
            if max_kill < sum_kill:
                max_kill = sum_kill
    print(f'#{tc} {max_kill}')

