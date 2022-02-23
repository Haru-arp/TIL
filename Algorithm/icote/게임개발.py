n, m = map(int, input().split())

d = [[0] * m for _ in range(n)]

x, y , direction = map(int, input().split())
d[x][y] = 1

array = []
for i in range(n):
    array.append(list(map(int,input().split())))

dx = [-1, 0, 1, 0] #북 동 남 서 방향
dy = [0, 1, 0, -1]

def turn_left():
    global direction
    direction -= 1
    if direction == -1:
        direction = 3
#시뮬레이션 시작
count = 1
turn_time = 0
while True:
    turn_left()
    nx = x+dx[direction]
    ny = y+dy[direction]

    if d[nx][ny] == 0 and array[nx][ny] == 0: #회전한 이후에 정면에 가보지 않은 칸이 존재하는 경우에 이동
        d[nx][ny] = 1
        x = nx
        y = ny
        count += 1
        turn_time = 0
        continue
    else:
        turn_time += 1

    if turn_time == 4:
        nx = x - dx[direction]
        ny = y - dy[direction]
        #뒤로 갈 수 있다면 이동하기.
        if array[nx][ny] == 0:
            x = nx
            y = ny
        else: #뒤가 바다로 막혀있는 경우
            break
        turn_time = 0
print(count)


