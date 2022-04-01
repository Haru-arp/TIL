def dfs(v, visited=[]):
    visited.append(v)
    for w in lst[v]:
        if w not in visited:
            visited = dfs(w, visited)
    return visited


T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    lst = [[] for _ in range(N+1)]

    for i in range(M):
        x, y = map(int, input().split())
        lst[x].append(y)
        lst[y].append(x)

    print(f'{dfs(1)}')