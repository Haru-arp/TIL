import sys

sys.stdin = open('input.txt')

T = int(input())

#row, col 인덱스로 탐색할 수 있게 방향 설정 (달팽이 방향이니 우-하-좌-상)
dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]

for tc in range(1, T + 1):
    n = int(input())
    arr = [[0 for _ in range(n)] for _ in range(n)]

    #방향 표시용 리스트(우, 하, 좌, 상)
    d = [[1,0], [0,1], [-1,0], [0,-1]]
    num, f = 1, 0 #현재 숫자, 방향을 표시하기 위한 변수
    x, y = 0, 0#현재 위치

    while num <= n ** 2:
        arr[y][x] = num
        num += 1

        #변경한 위치가 범위를 벗어나나?
        check_x = x + d[f][0]
        check_y = y + d[f][1]

        #범위를 벗어나면 flag 바꿔줌
        if check_x < 0 or check_x >= n or check_y < 0 or check_y >= n or arr[check_y][check_x]:
            f = (f+1)%4

        #위치 변경
        x += d[f][0]
        y += d[f][1]

 
    print(f'#{tc} ')
    for i in range(n):
        print(' '.join(map(str, arr[i])))

