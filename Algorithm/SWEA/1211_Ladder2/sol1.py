import sys

sys.stdin = open('input.txt')

T = 10


for tc in range(1, T + 1):
    test = int(input())
    #100번 돌면서 데이터를 받는다.
    ladder = [list(map(int, input().split())) for _ in range(100)]
    #사다리 길이 중 제일 적은 길이의 저장용
    min_count = 10000
    #제일 짧은 사다리의 위치를 저장
    return_x = 0
    #제일 뒤 부터 앞까지 1인 위치를 찾아서 저장한다.
    start_list = [i for i in range(99, -1, -1) if ladder[0][i]]
    #시작할 수 있는 포인트 만큼 반복
    for start in start_list:
        #이동을 위해서 좌표 세팅
    #제일 위에서부터 시작하니까 y좌표는 0이다.
        d_y = 0
        #x좌표는 1인곳에서 시작해야 하고 그것은 start에 들어있다.
        d_x = start
        #현재 사다리의 이동칸수를 저장하기 위한 변수
        count = 0
        #좌우 이동을 방지하기 위한 변수.
        move = 0
        #y축이 99가 될 때 까지 반복
        #99라면 제일 밑이므로 더이상 계산할 필요가 없다.
        down = 0
        left = 1
        right = 2
        while d_y < 99:
            #밑으로 내려갔거나 오른쪽으로 이동했다면
            #오른쪽으로 갈 때 벽이 있는지 아닌지 확인하고
            #벽이 아니라면 1인지 체크한다.
            if (move == down or move == left) and d_x > 0 and ladder[d_y][d_x -1]:
                #조건이 맞다면 왼쪽으로 이동 후, 이동했던 것들을 left로 기록
                d_x -= 1
                move = left
            #밑으로 내려갔거나, 오른쪽으로 이동했다면
            #오른쪽으로 갈 때 벽이 아닌지 확인하고
            #벽이 아니라면 1인지 체크
            elif (move == down or move == right) and d_x < 99 and ladder[d_y][d_x+1]:
                d_x += 1
                move = right
            #왼쪽도 오른쪽도 못간다면 아래로
            #내려갈 수 있는지 체크했지만 else로 두자
            elif ladder[d_y + 1][d_x]:
            #아래로 이동하고 행동을 down으로 바꾸자
                d_y += 1
                move = down
            #이동을 할 때마다 count 기록한다.
            count += 1
            #이동행동을 체크하는 이유는 오른쪽으로 이동후, 왼쪽과 오른쪽이 1인 경우가 생긴다.
            # 그 때 무한루프에 빠질 수 있으므로 단방향으로 이동하기 위해 사용
        #끝까지 이동했다면 이동했던 count 를 현재 최소 카운트와 비교한다.
        if min_count > count:
            min_count = count
            return_x = start

    print(f'#{tc} {return_x}')

