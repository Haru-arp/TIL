import sys

sys.stdin = open('input.txt')

T=int(input())
for test_case in range(1, T+1):
    area = [[0 for _ in range(10)] for _ in range(10)]
    count = 0 #겹치는 칸의 개수
    N = int(input())

    for i in range(1, N+1):
        row1, col1, row2, col2, color = map(int,input().split())

        for row in range(row1, row2+1):
            for col in range(col1, col2+1):
                if color == 1: #만약 색이 빨간색이면,
                    if area[row][col] == 0: #아무색이 없는 빈칸이면
                        area[row][col] = 1
                    elif area[row][col] == 2: #만약 색이 파란색이면
                        area[row][col]=3 #겹치는 부분을 보라색으로 칠하고
                        count += 1 #겹치는 부분의 칸의 개수를 세어준다.

                else: #만약 색이 파란색이면
                    if area[row][col] == 0: #색이 없으면
                        area[row][col] = 2 # 파란색으로 칠해라

                    elif area[row][col] == 1: #만약 색이 빨간색이면,
                        area[row][col] = 3
                        count += 1
    print(f'#{test_case} {count}')
