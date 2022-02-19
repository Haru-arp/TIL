import sys

sys.stdin = open('input.txt')

T = int(input())
def count_blank(arr, N, K):
    result = 0
    for i in range(0, N+1):
        cnt = 0
        for j in range(0, N+1):
            if arr[i][j] == 1:
                cnt += 1
            else:
                if cnt == K:
                    result += 1
                cnt = 0
    return result

for tc in range(1, T + 1):
    N, K = map(int, input().split())
    arr = [list(map(int, input().split()))+[0] for _ in range(N)]
    arr.append([0] * (N+1))

    #가로
    row_cnt = count_blank(arr, N, K)

    #세로
    trans_arr = list(map(list, zip(*arr)))
    column_cnt = count_blank(trans_arr, N, K)
    print(f'#{tc} {row_cnt + column_cnt}')

