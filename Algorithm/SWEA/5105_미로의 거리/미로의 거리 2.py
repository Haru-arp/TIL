import sys
sys.stdin = open('input.txt')
from collections import deque


dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(start):
    Q.append(start)
    global result

    while Q:
        x, y = Q.popleft()
        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]

            if 0 <= nx < N and 0 <= ny < N:
                if visited[nx][ny] == 0 and maze[nx][ny] != 1:
                    visited[nx][ny] = visited[x][y] + 1

                    if maze[nx][ny] == 3:
                        result = visited[nx][ny] - 1
                        return result
                    Q.append((nx, ny))
    return result


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    maze = [list(map(int, input()) for _ in range(N))]
    visited = [[0 for _ in range(N)] for _ in range(N)]

    result = 0
    Q = deque()

    for i in range(N):
        for j in range(N):
            if maze[i][j] == 2:
                start = (i, j)

    print(f'#{tc} {bfs(start)}')
