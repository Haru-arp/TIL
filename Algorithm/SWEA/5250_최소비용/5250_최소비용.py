import sys
sys.stdin = open('sample_input (1).txt')

def find():
    dr = [-1, 0, 1, 0]
    dc = [0, 1, 0, -1]
    INF = 1000000000 #큰 값
    dist = [[INF]*N for i in range(N)] # 최단거리 배열(2차원)
    dist[0][0] = 0 # 시작 값을 0으로
    # 시작점에서 상하좌우로 탐색 -> 또 거기서 상하좌우 탐색 : bfs탐색
    q = [] # 큐 템플릿 시작
    q.append((0, 0)) #시작점 큐에 넣기
    while q:
        t = q.pop(0)
        for k in range(4):
            nr = t[0] + dr[k]
            nc = t[1] + dc[k]
            if nr >= 0 and nr < N and nc >= 0 and nc < N:
                diff = 0 #높이 차이
                if Map[nr][nc] > Map[t[0]][t[1]]: # 높이 차이가 나면
                    diff = Map[nr][nc] - Map[t[0]][t[1]] # 그 높이 차이가 가중치
                    # 새롭게 갈 좌표의 최단 거리가 현 위치의 최단거리 + 현 위치 - 새 위치 가중치 + 1(기본적인 비용)
                if dist[nr][nc] > dist[t[0]][t[1]] + diff + 1:
                    dist[nr][nc] = dist[t[0]][t[1]] + diff + 1
                    q.append((nr, nc))
    return dist[N-1][N-1] #도착값 리턴


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    Map = [list(map(int, input().split())) for _ in range(N)]
    print(f'#{tc} {find()}')
