import sys
sys.stdin = open('input.txt')
T = int(input())
for tc in range(1, T+1):
    N, K = map(int, input().split()) #N = 수강생의 수 K = 과제를 제출한 사람의 수

    hws_check = list(map(int, input().split())) #제출한 사람
    count = list(range(1, N+1))

    for i in range(len(hws_check)):
        if hws_check[i] in count:
            count.remove(hws_check[i])

    print(f'#{tc}', *count)