import sys
from pprint import pprint
sys.stdin = open('input.txt')

T = 10


for tc in range(1, T + 1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(100)]

    sum_row = []
    sum_col = []
    for i in range(100):
        sum_r = 0
        sum_c = 0
        for j in range(100):
            sum_r += arr[i][j]
            sum_c += arr[j][i]
        sum_row.append(sum_r)
        sum_col.append(sum_c)
    max_row = 0
    max_col = 0
    for m in range(100):
        if max_row < sum_row[m]:
            max_row = sum_row[m]
        if max_col < sum_col[m]:
            max_col = sum_col[m]
    sum3, sum4 = 0, 0
    for n in range(100):
        sum3 += arr[n][n]
        sum4 += arr[n][99-n]
    max_cross = sum3
    if max_cross < sum4:
        max_cross = sum4

    ans=0
    if max_row >= max_col and max_row >= max_cross:
        ans = max_row

    if max_col >= max_row and max_col >= max_cross:
        ans = max_col

    if max_cross >= max_row and max_cross >= max_col:
        ans = max_cross
    print(f'#{tc} {ans}')

