import sys

sys.stdin = open('input.txt')

pipe = [[0, 0, 0, 0], [1, 1, 1, 1], [1, 1, 0, 0], [0, 0, 1, 1], [1, 0, 0, 1], [0, 1, 0, 1], [0, 1, 1, 0], [1, 0, 1, 0]]
di, dj = (-1, 1, 0, 0), (0, 0, -1, 1)
opp = [1, 0, 3, 2]


def BFS(N, M, si, sj, L):
    q = []
    v = [[0] * M for _ in range(N)]

    q.append((si, sj))
    v[si][sj] = 1
    cnt = 1

    while q:
        ci, cj = q.pop(0)

        if v[ci][cj] == L:
            return cnt

        for k in range(4):
            ni, nj = ci + di[k], cj + dj[k]
            if 0 <= ni < N and 0 <= nj < M and v[ni][nj] == 0 and\
                pipe[arr[ci][cj]][k] and pipe[arr[ni][nj]][opp[k]]:
                q.append((ni, nj))
                v[ni][nj] = v[ci][cj] + 1
                cnt += 1
    return cnt

T = int(input())
for tc in range(1, T + 1):
    N, M, R, C, L = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    ans = BFS(N, M, R, C, L)

    print(f'#{tc} {ans}')
