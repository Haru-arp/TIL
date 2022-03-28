import sys
from collections import deque

sys.stdin = open('input.txt')


def bfs(start):
    Q = deque()
    Q.append(start)

    visited[start[0]][start[1]] = 1

    while Q:
        w = Q.popleft()

        for i in range(4):
            ni = w[0] + di[i]
            nj = w[1] + dj[i]

            if 0 <= ni < N and 0 <= nj < N:
                if maze[ni][nj] == 1:
                    continue
                elif maze[ni][nj] == 0 and visited[ni][nj] == 0:
                    Q.append((ni,nj))
                    visited[ni][nj] = 1
                    visited[ni][nj] = visited[w[0]][w[1]] + 1
                elif maze[ni][nj] == 3:
                    return visited[w[0]][w[1]]-1
    return 0




T = int(input())
for tc in range(1, T+1):
    N = int(input())
    maze = [list(map(int, input())) for _ in range(N)]

    for i in range(N):
        for j in range(N):
            if maze[i][j] == 2:
                start = (i, j)

    di = [0, 0, -1, 1]
    dj = [-1, 1, 0, 0]

    visited = [[0] * N for _ in range(N)]

    print(f'#{tc} {bfs(start)}')

