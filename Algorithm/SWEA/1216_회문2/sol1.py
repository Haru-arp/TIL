import sys

sys.stdin = open('input.txt')

T = 10


for tc in range(1, T + 1):
    tc_n = int(input())
    N = 100
    board = [list(input()) for _ in range(N)] # 100 * 100글자판
    board_T = list(zip(*board)) #Transpose
    ans = 0 #최대 길이 값

    for i in range(N, 0, -1): #회문 길이를 100부터 1까지 검사하는데
        for j in range(N):
            for k in range(N-i+1): # 0부터 99-i+1 까지
                word = ''.join(board[j][k:k+i]) #가로 검사
                word2 = ''.join(board_T[j][k:k+i]) #세로검사
                #회문이 나오게 되면?
                if word == word[::-1] or word2 == word2[::-1]:
                    #최대값 갱신하고 반복문 나오기
                    if ans < i:
                        ans = i
                    break
            if ans > 0:
                break
        if ans > 0:
            break

    print(f'#{tc} {ans}')

