import sys

sys.stdin = open('input.txt')

def dfs(arr, i, j):
    if i < 0 or i >= n or j < 0 or j >= m or arr[i][j] != 0:
        return


    arr[i][j] = 1

    dfs(arr, i + 1, j)
    dfs(arr, i - 1, j)
    dfs(arr, i, j + 1)
    dfs(arr, i, j - 1)

n, m = map(int, input().split())
arr = [list(map(int, input())) for _ in range(n)]
cnt = 0

for i in range(n):
    for j in range(m):
        if arr[i][j] == 0:
            dfs(arr, i, j)
            cnt += 1

print(cnt)