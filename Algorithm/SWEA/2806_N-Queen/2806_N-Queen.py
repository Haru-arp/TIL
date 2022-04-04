import sys
sys.stdin = open('input.txt')

# info : 인덱스, 값 = 행, 몇번째 인덱스에 1 넣었는지
def check(info, turn):
    global N, cnt
    if turn == N: # 종료 조건 : 마지막 행까지 다 퀸을 놓고 넘어왔는지
        cnt += 1
        return
    tmp = [0] * N
    for i in range(len(info)):
        # 열 조건
        tmp[info[i]] = 1
        #왼쪽 대각선 조건
        if info[i]-(turn-i)>=0:
            tmp[info[i]-(turn-i)] = 1
        # 오른쪽 대각선 조건
        if info[i] + (turn-i) < N:
            tmp[info[i]+(turn-i)] = 1
    for j in range(N):
        if tmp[j] == 0:
            check(info + [j], turn+1)
T = int(input())
for tc in range(1, T+1):
    N = int(input())
    cnt = 0
    check([], 0)
    print(f'#{tc} {cnt}')