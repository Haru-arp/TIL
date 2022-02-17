import sys

sys.stdin = open('input.txt')

T = int(input())


for tc in range(1, T + 1):
    string = input()
    reversed_str = string[::-1]

    print(f'#{tc} {reversed_str} ')

