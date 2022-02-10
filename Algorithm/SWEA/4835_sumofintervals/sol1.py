import sys

sys.stdin = open('input.txt')

T = int(input())


for tc in range(1, T + 1):
    N, M = map(int, input().split())
    ai = list(map(int, input().split()))
    ans = 0

    New_list = [] #빈 리스트 생성
    for i in range(N-M+1): #구간에 맞는 range 예를들어 정수의 개수가 5고 구간의 개수가 3일때 5-3+1 하면 3이 나온다
        result = 0
        for j in range(i, i+M):
            result += ai[j]
        New_list.append(result) #반복하면서 그 구간합을 리스트에 추가해서 만든다.
    # 구간합 리스트에서 최대값 구하기
    max_id = New_list[0]
    for i in New_list:
        if max_id < i:
            max_id = i
    # 구간합 리스트에서 최소값 구하기
    min_id = New_list[0]
    for i in New_list:
        if min_id > i:
            min_id = i

    ans = max_id - min_id

    print(f'#{tc} {ans}')

