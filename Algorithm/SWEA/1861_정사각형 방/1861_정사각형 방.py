import sys
sys.stdin = open('s_input.txt')

def BFS(si, sj):
    q = []
    s = []
    q.append((si, sj))
    v[si][sj] = 1
    s.append(arr[si][sj])

    while q:
        ci, cj = q.pop(0)
        for di, dj in ((-1,0), (1,0), (0,-1), (0,1)):
            ni, nj = ci+di, cj+dj
            if 0 <= ni < N and 0 <=nj <N and v[ni][nj] == 0 and\
                abs(arr[ci][cj] - arr[ni][nj]) == 1:
                q.append((ni,nj))
                v[ni][nj] = 1
                s.append(arr[ni][nj])
    return min(s), len(s)

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    v = [[0]*N for _ in range(N)]
    num = N*N
    cnt = 0
    for i in range(N):
        for j in range(N):
            if v[i][j] == 0:
                tn, tc = BFS(i, j)
                if cnt < tc or cnt == tc and num > tn:
                    cnt = tc
                    num = tn
    print(f'#{tc} {num} {cnt}')