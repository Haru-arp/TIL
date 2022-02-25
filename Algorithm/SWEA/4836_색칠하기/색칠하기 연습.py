from pprint import pprint
import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    matrix = [[0] * 10 for _ in range(10)]
    cnt = 0 #보라색 칸 수 세는 변수
    N = int(input())

    for _ in range(1, N+1):
        row1, col1, row2, col2, color = map(int, input().split())

        for row in range(row1, row2+1):
            for col in range(col1, col2+1):
                if color == 1:
                    if matrix[row][col] == 0:
                        matrix[row][col] = 1  #빨간색으로 칠함
                    elif matrix[row][col] == 2:
                        matrix[row][col] = 3
                        cnt += 1
                elif color == 2:
                    if matrix[row][col] == 0:
                        matrix[row][col] = 2
                    elif matrix[row][col] == 1:
                        matrix[row][col] = 3
                        cnt +=1
    print(f'#{tc} {cnt}')

