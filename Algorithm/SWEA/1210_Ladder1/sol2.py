import sys

sys.stdin = open('input.txt')

T = 10

dr = [-1, 0, 0] #상
dc = [0, 1, -1] # 우, 좌


for tc in range(1, T + 1):
    t = int(input())
    arr = [[0] + list(map(int, input().split())) + [0] for _ in range(100)]

    for j in range(102):
        if arr[99][j] == 2:
            c = j
    d = 0 #0 = 위, 1 = 오른쪽 2 = 왼쪽
    r = 99

    while True:
        if r == 0:
            break

        if arr[r][c-1] == 1:
            d = 2
            while True:
                r += dr[d]
                c += dc[d]
                if arr[r][c-1] == 0:
                    break
        elif arr[r][c+1] == 1:
            d = 1
            while True:
                r += dr[d]
                c += dc[d]
                if arr[r][c+1] == 0:
                    break

        d = 0
        r += dr[d]
        c += dc[d]

    print(f'#{tc} {c-1} ')