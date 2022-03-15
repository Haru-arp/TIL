from collections import deque
import sys
sys.stdin = open('input.txt')

def bfs(start, end):
    # 시작점설정
    Q.append(start)
    visited[start] = 1
    while Q:
        v = Q.popleft()
        for w in G[v]:
            # 방문하지않았다면
            if not visited[w]:
                # 방문처리
                visited[w] = 1
                # 거리설정
                distance[w] = distance[v] + 1
                Q.append(w)
                # 도착지점에 도착했으면
                if w == end:
                    # 거리를 반환
                    return distance[w]
    return 0


for tc in range(1, int(input()) + 1):
    V, E = map(int, input().split())

    G = [[] for _ in range(V + 1)]

    # 방향이 없는 그래프이므로 쌍방향 설정해주기
    for i in range(E):
        u, v = map(int, input().split())
        G[u].append(v)
        G[v].append(u)
    start, end = map(int, input().split())

    visited = [0] * (V + 1)
    distance = [0] * (V + 1)

    Q = deque()

    print('#{} {}'.format(tc, bfs(start, end)))