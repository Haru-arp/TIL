from collections import deque

def bfs(v):
    queue = deque()
    queue.append(1)
    visited[1] = 1

    while queue:
        v = queue.popleft()
        print(v)
        for i in lst[v]:
            if visited[i] != 1:
                queue.append(i)
                visited[i] = 1


T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    visited = [0] * (N+1)
    lst = [[] for _ in range(N+1)]

    for i in range(M):
        x, y = map(int, input().split())
        lst[x].append(y)
        lst[y].append(x)

    bfs(1)