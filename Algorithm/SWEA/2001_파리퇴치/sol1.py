# import sys
#
# sys.stdin = open('input.txt')
#
# T = int(input())
# for tc in range(1, T + 1):
#     #배열의 행, 열 수 N과 파리채 크기 M
#     N, M = map(int, input().split())
#     # N by N 크기 배열 입력
#     matrix = [list(map(int, input().split())) for _ in range(N)]
#     fly = [] #영역별로 죽은 파리 수를 저장하는 리스트
#     #i는 0부터 N-1까지
#     for i in range(N-M+1):
#         #j는 0부터 N-1까지
#         for j in range(N-M+1):
#             #영역별 파리 수 총합을 저장하는 변수 초기화
#             total = 0
#             #ci는 0부터 M-1까지
#             for ci in range(M):
#                 #cj는 0부터 M-1까지
#                 for cj in range(M):
#                     #인덱스의 범위 안에 해당하면, total변수에 파리 수 저장
#                     if i + ci in range(N) and j + cj in range(N):
#                         total += matrix[i + ci][j + cj]
#             #영역별 파리 수 총합을 fly 리스트에 추가
#             fly.append(total)
#     max_value = fly[0]
#     for i in fly:
#         if i > max_value:
#             max_value = i
#     print(f'#{tc} {max_value}')

import sys
from pprint import pprint
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())
    matrix = [list(map(int, input().split())) for _ in range(N)]
    total = 0
    for i in range(N-M+1):
        for j in range(N-M+1):
            sum_v = 0
            for di in range(M):
                for dj in range(M):
                    sum_v += matrix[i+di][j+dj]
            if sum_v > total:
                total = sum_v
    print(f'#{tc} {total}')
