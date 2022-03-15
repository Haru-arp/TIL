import sys
from collections import deque
sys.stdin = open('input.txt')

T = int(input())

#bfs 선언
def BFS(start):
    que.append(start)
    global result
    while que:
        x, y = que.popleft()

        for k in range(4):
            xx = x + dx[k]
            yy = y + dy[k]
            #범위 체크
            if 0 <= xx < N and 0 <= yy < N:
                # 길이 있고 방문하지 않았다면
                if visit_level[xx][yy] == 0 and maze[xx][yy] != 1:
                    # 방문거리 기록
                    visit_level[xx][yy] = visit_level[x][y] + 1
                    if maze[xx][yy] == 3:
                        #마지막 도착했을 때 더해준 값 1 빼주기
                        result = visit_level[xx][yy] - 1
                        return result
                    que.append([xx, yy])
    return result

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

for tc in range(1, T+1):
    N = int(input())
    maze = [list(map(int, input())) for _ in range(N)]
    #방문을 안했다면 0 , 방문을 했다면 그 숫자는 거리(level)
    visit_level = [[0 for _ in range(N)] for _ in range(N)]
    result = 0
    que = deque()

    for i in range(N):
        for j in range(N):
            if maze[i][j] == 2:
                start = [i, j]

    print(f'#{tc} {BFS(start)}')
