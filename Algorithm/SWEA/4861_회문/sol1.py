import sys

sys.stdin = open('input.txt')

T = int(input())


for tc in range(1, T + 1):
    N, M = map(int, input().split())
    words = [list(input()) for _ in range(N)]

    #회문이 가로일때
    for i in range(N):
        for j in range(N-M+1): #한 줄 안에서 얼마나 돌건지
            temp1 = []
            temp2 = []
            rlt = []
            for k in range(M):
                temp1.append(words[i][j+k]) #행 하나에 다 넣고
            temp2.append(temp1[::-1])
            if temp2[0] == temp1:
                print(f'#{tc}', end='')
                print(''.join(temp2[0]))
    #회문이 세로일때
    for i in range(N):
        for j in range(N-M+1):
            temp1 = []
            temp2 = []
            result = []
            for k in range(M):
                temp1.append(words[j+k][i]) #열 하나에 다 넣고
            temp2.append(temp1[::-1]) #역배치한거 temp2에 넣기
            if temp2[0] == temp1:
                print(f'#{tc}', end='')
                print(''.join(temp2[0]))





