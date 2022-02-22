import sys

sys.stdin = open('input.txt')

T = int(input())

def paper(N):
    n = N//10 #10단위라서 10으로 나눴습니다.
    memo = [0]*(n+1) #리스트 생성
    memo[0] = memo[1] = 1 #1가지
    for i in range(2, n+1):
        memo[i] = memo[i-1] + memo[i-2] * 2
    return memo[-1]

for tc in range(1, T + 1):
    print(f'#{tc} {paper(int(input()))} ')

