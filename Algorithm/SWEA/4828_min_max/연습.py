import sys

sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    ai = list(map(int, input().split()))
    # print(ai)
    max_ai = max(ai)
    min_ai = min(ai)
    ans = max_ai - min_ai
    print(f'#{tc} {ans}')