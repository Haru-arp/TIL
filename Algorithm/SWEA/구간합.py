T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    ai = list(map(int, input().split()))
    ans = 0 #답 저장하는 변수

    New_lst = []
    for i in range(N-M+1):
        result = 0
        for j in range(i, i+M):
            result += ai[j]
        New_lst.append(result)

    max_id = New_lst[0]
    for i in New_lst:
        if max_id < i:
            max_id = i

    min_id = New_lst[0]
    for i in New_lst:
        if min_id > i:
            min_id = i

    ans = max_id - min_id

    print(f'#{tc} {ans} ')
