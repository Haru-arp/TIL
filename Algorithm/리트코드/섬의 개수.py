def dfs(grid, i, j):
    # 더 이상 땅이 아닌 경우 종료
    if i < 0 or i >= len(grid) or j < 0 or j >= len(grid[0]) or grid[i][j] != 1:
        return 
    
    grid[i][j] = 0

    dfs(grid, i + 1, j)
    dfs(grid, i - 1, j)
    dfs(grid, i, j + 1)
    dfs(grid, i, j - 1)


grid = [[11110], [11010], [11000], [00000]]


count = 0
for i in range(len(grid)):
    for j in range(len(grid[0])):
        if grid[i][j] == 1:
            dfs(grid, i, j)
            #모든 육지 탐색 후 카운트 1 증가
            count += 1

print(count)
            