import sys
sys.stdin = open('input.txt')
from collections import deque

T = int(input())
dx = [-1, 1, 0, 0]
dy = [0, 0, 1, -1]

def bfs(start):
    que.append(start)
    global result
    while que:
        x, y = que.popleft()

        for k in range(4):
            xx = x + dx[k]
            yy = y + dy[k]

            if 0 <= xx < N and 0 <= yy < N:
                if visit_level[xx][yy] == 0 and maze[xx][yy] != 1:
                    visit_level[xx][yy] = visit_level[x][y] + 1
                    if maze[xx][yy] == 3:
                        result = visit_level[xx][yy] - 1
                        return result
                    que.append((xx,yy))
    return result


for tc in range(1, T+1):
    N = int(input())
    maze = [list(map(int , input())) for _ in range(N)]
    visit_level = [[0 for _ in range(N)] for _ in range(N)]
    result = 0
    que = deque()

    for i in range(N):
        for j in range(N):
            if maze[i][j] == 2:
                start = (i, j)

    print(f'#{tc} {bfs(start)}')