from collections import deque

def dfs(graph, v, visited):
    visited.append(v)
    print(v, end=' ')

    for e in graph[v]:
        if e not in visited:
            dfs(graph, e, visited)

def bfs(graph, v):
    queue = deque([v])
    visited = [v]

    while queue:
        now = queue.popleft()
        print(now, end=' ')

        for e in graph[now]:
            if e not in visited:
                queue.append(e)
                visited.append(e)


n, m, v = map(int, input().split())
graph = [[] for _ in range(n+1)]
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

for i in range(1, n+1):
    graph[i].sort()

visited = []
dfs(graph, v, visited)
print()

bfs(graph, v)

