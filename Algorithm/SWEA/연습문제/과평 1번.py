import sys
sys.stdin = open('algo1_sample_in.txt')
T = int(input())
for tc in range(1, T+1):
    N, K = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    max_sum = 0
    for i in range(len(arr)):
        row_sum = 0
        for k in range(K):
            if 0 <= i+k < N:
                row_sum += arr[i][i+k]

        if max_sum < row_sum:
            max_sum = row_sum
    print(f'#{tc} {max_sum}')