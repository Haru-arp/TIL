import sys

sys.stdin = open('input.txt')

T = int(input())


for tc in range(1, T + 1):
    N, M = map(int, input().split())
    matrix = [list(map(int, input().split())) for _ in range(N)]
    total = 0
    for i in range(N-M+1):
        for j in range(N-M+1):
            sum_v = 0
            for di in range(M):
                for dj in range(M):
                    sum_v += matrix[i+di][j+dj]
            if sum_v > total:
                total = sum_v

    print(f'#{tc} {total}')

