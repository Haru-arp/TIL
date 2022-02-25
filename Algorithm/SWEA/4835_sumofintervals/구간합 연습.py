import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    ai = list(map(int, input().split()))
    sum_v = []
    for i in range(N-M+1):
        sum_M = 0
        for j in range(i,i+M):
            sum_M += ai[j]
        sum_v.append(sum_M)
    # print(sum_v)
    max_v = max(sum_v)
    min_v = min(sum_v)
    ans = max_v - min_v

    print(f'#{tc} {ans}')