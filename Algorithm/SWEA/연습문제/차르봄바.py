from pprint import pprint
import sys
sys.stdin = open('bomber.txt')


T = int(input())

dr = [-1, 1, 0, 0] #상하좌우
dc = [0, 0, -1, 1]

drr = [-1, -1, 1, 1]
dcc = [-1, 1, 1, -1]

def bomb(r, c):
    cross = arr[r][c]
    diag = arr[r][c]
    #상하좌우
    for i in range(4):
        for j in range(1, P+1):
            rr, cc = r + dr[i] * j, c + dc[i] * j
            if 0 <= rr < N and 0 <= cc < N:
                cross += arr[rr][cc]
    #대각선
    for i in range(4):
        for j in range(1, P+1):
            rr, cc = r + drr[i] * j, c + dcc[i] * j
            if 0 <= rr < N and 0 <= cc < N:
                diag += arr[rr][cc]
    return max(cross, diag)


for tc in range(1, T+1):
    N, P = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]

    max_bomb = 0
    for i in range(N):
        for j in range(N):
            if bomb(i,j) > max_bomb:
                max_bomb = bomb(i, j)

    print(f'#{tc} {max_bomb}')