import sys

sys.stdin = open('input.txt')

T = int(input())
def dfs(idx, _sum):
    global min_result
    if idx == N:
        if _sum < min_result:
            min_result = _sum
        return
    if _sum >= min_result:
        return

    for i in range(N):
        #갔던 세로줄은 사용 불가능하게 변경
        if use_check[i]:
            use_check[i] = False
            dfs(idx+1, _sum + map_list[idx][i])
            use_check[i] = True





for tc in range(1, T + 1):
    N = int(input())
    map_list = [list(map(int, input().split())) for _ in range(N)]
    use_check = [True for _ in range(N)]
    min_result = 987654321
    dfs(0,0)
    print(f'#{tc} {min_result} ')

