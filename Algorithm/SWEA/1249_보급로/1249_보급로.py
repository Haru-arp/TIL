import sys
sys.stdin = open('input (1).txt')

def BFS(si, sj, ei, ej):
    q = [] # [1] q, v 생성
    v = [[100000] * N for _ in range(N)]

    # [2] q 초기데이터(들) 삽입, v 표시
    q.append((si, sj))
    v[si][sj] = arr[si][sj]

    while q:
        ci, cj = q.pop(0)

        # 네 방향/ 8 방향 / 숫자 차이가 일정 값 이하 ... 조건이 들어간다.
        for di, dj in ((-1, 0), (1, 0), (0, -1), (0, 1)):
            ni, nj = ci+di, cj+dj
            if 0 <= ni < N and 0 <= nj < N and v[ni][nj] > v[ci][cj] + arr[ni][nj]:
                q.append((ni,nj))
                v[ni][nj] = v[ci][cj] + arr[ni][nj]
    return v[ei][ej]

T = int(input())
for tc in range(1,T+1):
    N = int(input())
    arr = [list(map(int, input())) for _ in range(N)]
    ans = BFS(0,0,N-1,N-1)
    print(f'#{tc} {ans}')