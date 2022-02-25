import sys
sys.stdin = open('input.txt')
T = int(input())
for tc in range(1, T+1):
    N = int(input())
    ai_lst = list(map(int, input().split()))

    for i in range(len(ai_lst)):
        #짝수일때
        if i & 1:
            min_idx = i
            for j in range(i+1, N):
                if ai_lst[j] < ai_lst[min_idx]:
                    min_idx = j
            ai_lst[i], ai_lst[min_idx] = ai_lst[min_idx], ai_lst[i]
        else: #홀수일때
            max_idx = i
            for j in range(i+1, N):
                if ai_lst[j] > ai_lst[max_idx]:
                    max_idx = j
            ai_lst[i], ai_lst[max_idx] = ai_lst[max_idx], ai_lst[i]

    print(f'#{tc}', *ai_lst[:10])