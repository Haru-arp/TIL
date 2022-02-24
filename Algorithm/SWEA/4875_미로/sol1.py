'''
-문제 :
    미로: 2(출발) 3(도착) 0(통로) 1(벽)
    도착할 수 있으면 1 출력 아니면 0 출력
    미로는 N by N ( 5<= N <= 100)

DFS로 시작점에서 4방향 체크하면서 목적지를 찾아가보자
stack에는 이동 가능한 곳들을 담아주고 방문한 곳은 기본 배열에서 0으로 초기화 되있던것을 1로 바꾸어주고,
목적지인 3에 도착하면 반복문 벗어나기. break.
'''
import sys

sys.stdin = open('input.txt')

T = int(input())

moves = [(1, 0), (-1, 0), (0, -1), (0, 1)] #상 하 좌 우 델타값)

def isWall(x,y):
    if x < 0 or y < 0 or y >= N or x >= N:
        return True #벽입니다.
    return False #벽이 아닙니다.

for tc in range(1, T + 1):
    N = int(input())
    maze = [list(map(int, input())) for _ in range(N)]
    x, y = 0, 0

    #시작지점인 2 구하기
    for i in range(N):
        if 2 in maze[i]:
            x = maze[i].index(2) #열
            y = i #행
            break
    #이동 가능한 곳을 저장하는 stack에 첫번째 위치 인덱스 넣어주기.
    stack = [(y, x)]
    result = 0
    while stack:
        #스택에서 시작점 인덱스 가져오기.
        y, x = stack.pop()
        #현재 위치는 방문 했으므로 1로 변경
        maze[y][x] = 1

        for _y, _x in moves:
            #상하좌우 방향으로 인덱스 이동하기..
            dy = y + _y
            dx = x + _x

            #벽인지 체크하고 주변이 막혔다면 다음 인덱스로 이동..
            if isWall(dy, dx):
                continue

            #간 곳이 3이라면 result = 1로 바꾸고 break
            if maze[dy][dx] == 3:
                result = 1
                break

            #0이라면 이동할 수 있는 곳이다. stack에 저장하자.
            elif not maze[dy][dx]:
                stack.append((dy, dx))
        else: #상하좌우 다 검사했는데 break가 없으면 계속 이동
            continue
        break #break로 이곳에 도달했다면 while문 종료.

    print(f'#{tc} {result} ')

