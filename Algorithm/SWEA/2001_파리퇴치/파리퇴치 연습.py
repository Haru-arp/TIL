from pprint import pprint
import sys

sys.stdin = open('input.txt')
T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    total = 0
    for x in range(N - M + 1):
        for y in range(N - M + 1):
            sum_v = 0
            for i in range(M):
                for j in range(M):
                    sum_v += arr[i + x][j + y]
            if sum_v > total:
                total = sum_v

    print(f'{tc} {total}')
