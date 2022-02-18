import sys
from pprint import  pprint

sys.stdin = open('input.txt')

T = int(input())


for tc in range(1, T + 1):
    line = 5
    matrix_list = [list(input()) for _ in range(line)]

    max_len = 0
    for r in matrix_list:
        if len(r) > max_len:
            max_len = len(r)
    print_matrix = ''
    for i in range(max_len):
        for j in range(5):
            if i < len(matrix_list[j]):
                print_matrix += matrix_list[j][i]
    print(f'#{tc} {print_matrix}')

