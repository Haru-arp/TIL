import sys
sys.stdin = open('input.txt')
T = int(input())

for tc in range(1, T+1):
    # n값과 16진수 값을 공백을 기준으로 받아오기.
    n, h = input().split()
    # 16진수를 10진수로 바꾼 것을 다시 2진수로 바꾸기
    # 내장함수 format(value, 'b') 사용
    # int(string, base)
    b = format(int(h, 16), 'b')

    print(f'#{tc}', end=' ')
    # 앞에 0을 채워주기 위해서 cnt 변수 안에 앞에 얼만큼 비워지는지 넣기.
    cnt = int(n)*4 - len(b)
    for _ in range(cnt):
        print(0, end='')
    print(b)

