import sys
sys.stdin = open('input.txt')

def dfs(idx):
    global charge, result

    if idx >= len(lst):
        if result >= charge:
            result = charge
        return

    if result <= charge:
        return
    for i in range(idx+lst[idx], idx, -1):
        charge += 1
        dfs(i)
        charge -= 1

T = int(input())
for tc in range(1, T+1):
    lst = list(map(int, input().split()))
    N = lst[0]
    result = 987654321
    charge = 0
    dfs(1)

    print(f'#{tc} {result -1}') #출발점은 세지 않으므로 -1
