import sys
sys.stdin = open('input.txt')

def dfs(idx, sum_v):
    global min_v
    # 다 방문했으면?
    if 0 not in visited:
        if min_v > sum_v:
            min_v = sum_v
        return
    elif min_v < sum_v:
        return
    for i in range(N):
        if i == idx:   # 현재위치면?
            continue
        if visited[i]: # 이미 방문했으면?
            continue
        if i == 0 and 0 in visited[1:]: # 아직 방문하지 않은 곳이 있는데 출발지로 왔으면 오면 안되니까
            continue
        visited[i] = 1 # 방문 표시
        dfs(i, sum_v + arr[idx][i]) # 소비량을 더 더해준다.
        visited[i] = 0 # 방문 표시 해제


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    visited = [0] * N
    min_v = 987654321
    dfs(0, 0)
    print(f'#{tc} {min_v}')