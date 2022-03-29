import sys
sys.stdin = open('input.txt')

def dfs(current, tmp):
    global rlt
    if tmp < rlt:
        if 0 not in visited[1:] : #전부 방문했다면
            rlt = min(rlt, tmp + arr[current][0]) #결과값 갱신하고 함수 종료
            return
        for next in range(1,N):
            if arr[current][next] != 0 and visited[next] == 0:
                visited[next] = 1
                dfs(next, tmp + arr[current][next])
                visited[next] = 0

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]

    rlt = 100000
    for i in range(1, N):
        visited = [0]*N
        visited[i] = 1
        dfs(i, arr[0][i]) #(currend_y, tmp_sum)

    print(f'#{tc} {rlt}')