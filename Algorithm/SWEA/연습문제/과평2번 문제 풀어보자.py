import sys
sys.stdin = open('input_prob_2.txt')
T = int(input())

for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]

    max_sum1, max_sum2 = 0, 0

    for r in range(N):
        for c in range(N):
            each_sum = 0
            d_row = [-1, -1, -1, 0, 0, 0, 1, 1, 1]
            d_col = [-1, 0, 1, -1, 0, 1, -1, 0, 1]

            for i in range(len(d_row)):
                rr, cc = r + d_row[i], c + d_col[i]
                if 0 <= rr < N and 0 <= cc < N:
                    each_sum += arr[rr][cc]
                else:
                    each_sum = 0
                    break
            if max_sum1 <each_sum:
                max_sum1 = each_sum
    for r in range(N):
        for c in range(N):
            each_sum = 0
            d_row = [-1, 1, 0, 0]
            d_col = [0, 0, -1, 1]

            power = arr[r][c]
            each_sum += power

            for i in range(4):
                for p in range(1, power):
                    rr, cc = r+ d_row[i] * p, c + d_col[i] * p
                    if 0 <= rr < N and 0 <= cc < N:
                        each_sum = arr[rr][cc]

            if max_sum2 < each_sum:
                max_sum2 = each_sum

    if max_sum1 > max_sum2:
        result = max_sum1
    elif max_sum2 > max_sum1:
        result = max_sum2

    print(f'{tc} {result}')
