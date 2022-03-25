import sys
sys.stdin = open('input.txt')
from pprint import pprint

def dfs(graph, i, j):
    if i < 0 or i >= n or j < 0 or j >= m or graph[i][j] != 0:
        return

    graph[i][j] = '#'

    dfs(graph, i+1, j)
    dfs(graph, i-1, j)
    dfs(graph, i, j+1)
    dfs(graph, i, j-1)


n, m = map(int, input().split())

graph = [list(map(int, input())) for _ in range(n)]
count = 0
for i in range(n):
    for j in range(m):
        if graph[i][j] == 0:
            dfs(graph, i, j)
            count += 1
print(count)