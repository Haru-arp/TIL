import sys
sys.stdin = open('input.txt')
T = int(input())

def count_arr(N):
    ret = 0
    for i in range(N + 1):
        cnt = 0
        for j in range(N + 1):
            if arr[i][j] == 1:
                cnt += 1
            else:
                if cnt == K:
                    ret += 1
                cnt = 0
    return ret
for tc in range(1, T+1):
    N, K = map(int, input().split())

    arr = [list(map(int, input().split())) + [0] for _ in range(N)]
    arr.append([0] * (N+1))
    #행방향 체크

    sol = count_arr(N)
    arr = list(map(list, zip(*arr)))
    sol += count_arr(N)
    print(f'#{tc} {sol}')