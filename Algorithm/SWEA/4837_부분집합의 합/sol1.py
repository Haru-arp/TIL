import sys

sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T + 1):
    N, K = map(int, input().split())
    #1~12를 담고있는 집합
    A = list(range(1,13))
    cnt = 0 #정답세기위한 카운트
    #부분집합 생성
    for i in range(1 << 12):
        sub_set = [] #부분집합 담을 변수리스트
        sum_v = 0
        for j in range(12):
            if i & (1 << j):
                sub_set.append(A[j])
                sum_v += A[j]
        #부분집합 원소의 개수가 N이고 합이 K이면 cnt 값 1증가
        if len(sub_set) == N and sum_v == K:
            cnt = cnt + 1

    print(f'#{tc} {cnt}')
