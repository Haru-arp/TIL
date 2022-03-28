import sys
sys.stdin = open('input.txt')
from collections import deque

def bfs(start, end):
    Q.append(start)
    visited[start] = 1
    while Q:
        v = Q.popleft()
        for i in graph[v]:
            if not visited[i]:
                visited[i] = 1

                # 거리 갱신
                distance[i] = distance[v] + 1
                Q.append(i)

                if i == end:
                    return distance[i]
    return 0


T = int(input())
for tc in range(1, T+1):
    V, E = map(int, input().split())

    graph = [[] for _ in range(V+1)]

    for _ in range(E):
        a, b = map(int, input().split())
        graph[a].append(b)
        graph[b].append(a)
    start, end = map(int, input().split())

    visited = [0] * (V+1)
    distance = [0] * (V+1)

    Q = deque()

    print(f'#{tc} {bfs(start, end)}')
