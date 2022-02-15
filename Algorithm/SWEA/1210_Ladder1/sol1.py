import sys

sys.stdin = open('input.txt')
#내가 생각한 로직: 도착점인 2를 찾고 거기서부터 올라가서 출발점 찾기
T = 10
dr = [-1, 0, 0]
dc = [0, 1, -1]
for tc in range(1, T + 1):
    t = int(input())
    #양 끝에 벽을 세워주려고 0 컬럼 추가
    arr = [[0]+list(map(int, input().split())) + [0] for _ in range(100)]

    # c = 도착점 column idx 구하기
    for j in range(102):
        if arr[99][j] == 2:
            c = j
    #방향 위로 초기화
    d = 0  #0:위, 1: 오 2 : 왼
    r = 99
    while True:
        if r == 0:
            break # 반복문 돌리다가 row 인덱스가 0이 되면 끝내고 리턴

        #왼쪽에 1이 있으면 왼쪽으로 계속 가다가 0이 나오면 반복문 종료
        if arr[r][c-1]:
            d = 2
            while True:
                r += dr[d]
                c += dc[d]
                if arr[r][c-1] == 0:
                    break
        #오른쪽에 1이 있으면 오른쪽으로 계속 가다가 0이 나오면 종료
        elif arr[r][c+1]:
            d = 1
            while True:
                r += dr[d]
                c += dc[d]
                if arr[r][c+1] == 0:
                    break
        #양 옆에 1이 하나도 없으면 계속 직진
        #또는 왼쪽이든 오른쪽이든 가다가 next col에서 0이면 d=0(위로)체인지
        d = 0
        r += dr[d]
        c += dc[d]

    print(f'#{tc} {c-1} ')

