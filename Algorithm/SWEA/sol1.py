import sys

sys.stdin = open('input.txt')

T = 10
for tc in range(1, T + 1):
    length = int(input())
    buildingHeight = list(map(int, input().split()))
    ans = 0

    for i in range(2, length):
        curr_height = buildingHeight[i]
        if not curr_height:
            continue
        else:
            max_height = 0
            d_col = [-2, -1, 1, 2]
            for d in d_col:
                check_idx = i + d
                if buildingHeight[check_idx] > max_height:
                    max_height = buildingHeight[check_idx]
            if curr_height > max_height:
                ans += curr_height - max_height
    print(f'#{tc} {ans}')

