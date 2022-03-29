import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    weight = list(map(int, input().split()))
    truck = list(map(int, input().split()))

    ans = 0
    for i in range(M):
        temp = []
        for j in range(N):
            if truck[i] >= weight[j]: #무게가 트럭 용량보다 작거나 같으면
                temp.append(weight[j]) # temp에 넣어주고
        if len(temp) != 0: # temp에 하나라도 들어가 있으면
            ans += max(temp) # 최대값을 ans에 더해주고
            for j in range(N): #최대값을 찾아서 0으로 바꾸고 나가기
                if weight[j] == max(temp):
                    weight[j] = 0
                    break

    print(f'#{tc} {ans}')