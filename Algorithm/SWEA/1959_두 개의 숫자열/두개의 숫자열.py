import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))

    if n > m:
        n, m = m, n
        a, b = b, a
    max_sum = -987654321
    for i in range(m-n+1):
        sum_v = 0
        for j in range(n):
            sum_v += a[j] * b[j+i]
        if sum_v > max_sum:
            max_sum = sum_v

    print(f'#{tc} {max_sum}')

