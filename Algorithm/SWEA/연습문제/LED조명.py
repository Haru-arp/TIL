T = int(input())
for tc in range(1, T+1):
    N = int(input())
    pattern = list(map(int, input().split()))
    numb = [x for x in range(1, N+1)] #각 조명 번호

    i = 0
    cnt = 0
    while True:
        if sum(pattern) == 0:
            break
        if pattern[i] == 0:
            i += 1

        if pattern[i] == 1:
            for j in range(len(numb)):
                if numb[j] % numb[i] == 0: #배수인 경우라면 반전시켜주고
                    if pattern[j] == 1:
                        pattern[j] = 0
                    else:
                        pattern[j] = 1
            i += 1
            cnt += 1 #몇번 반전했는지 세어라
    print(f'#{tc} {cnt}')
