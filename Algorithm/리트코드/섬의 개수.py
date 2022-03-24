import sys
sys.stdin = open('input.txt')
from pprint import pprint

def dfs(grid, i, j):
    # 더 이상 땅이 아닌 경우 종료
    if i < 0 or i >= len(grid) or j < 0 or j >= len(grid[0]) or grid[i][j] != 1:
        return 
    
    grid[i][j] = 3

    dfs(grid, i + 1, j)
    dfs(grid, i - 1, j)
    dfs(grid, i, j + 1)
    dfs(grid, i, j - 1)



grid = [list(map(int, input())) for _ in range(4)]
pprint(grid)


count = 0
for i in range(len(grid)):
    for j in range(len(grid[0])):
        if grid[i][j] == 1:
            dfs(grid, i, j)
            #모든 육지 탐색 후 카운트 1 증가
            count += 1

print(count)
            