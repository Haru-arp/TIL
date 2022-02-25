import sys

sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    lst = list(map(int, input().split()))
    # 내 알고리즘 : 홀수에는 내림차순 짝수에는 오름차순 정렬
    # 홀수번쨰, 즉 짝수 인덱스에는 큰값, 홀수 인덱스에는 작은값
    #홀수번째 부분 내림차순 정렬
    for i in range(len(lst)):
        if i & 1:
            max_idx = i
            for j in range(i+1, N):
                if lst[j] < lst[max_idx]:
                    max_idx = j
            lst[i], lst[max_idx] = lst[max_idx], lst[i]

    #리스트 인덱스 number가 홀수일 때는 작은 값 정렬
        else:
            min_idx = i
            for j in range(i+1, N):
                if lst[j] > lst[min_idx]:
                    min_idx = j
            lst[i], lst[min_idx] = lst[min_idx], lst[i]
    print('#{}'.format(tc), *lst[:10])

