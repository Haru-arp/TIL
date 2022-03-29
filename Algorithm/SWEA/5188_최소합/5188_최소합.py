import sys
sys.stdin = open('input.txt')

dxy = [(0, 1), (1, 0)]

def dfs(x, y, ssum):
    global ans
    # 가지 치기 (합을 갱신하다가 ans값보다 크면 그 경로는 틀린 것이다.)
    if ssum >= ans:
        return

    if x == N-1 and y == N-1: # 도착지에 도착한 경우
        if ssum < ans:
            ans = ssum
        return

    for dx, dy in dxy:
        nx, ny = x + dx, y + dy

        if nx > -1 and nx < N and ny > -1 and ny < N:
            dfs(nx, ny, ssum+matrix[nx][ny])


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    matrix = [list(map(int, input().split())) for _ in range(N)]
    ans =  9999999
    dfs(0, 0, matrix[0][0])
    print(f'#{tc} {ans}')