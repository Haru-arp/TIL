import sys

sys.stdin = open('input.txt')

T = 10
def idx_max():
    max_value = 0
    max_idx = 0
    for i in range(len(box_lst)):
        if max_value < box_lst[i]:
            max_value = box_lst[i]
            max_idx = i
    return max_idx

def idx_min():
    min_value = 12345667
    min_idx = 0
    for j in range(len(box_lst)):
        if min_value > box_lst[j]:
            min_value = box_lst[j]
            min_idx = j
    return min_idx


for tc in range(1, T + 1):
    N = int(input())
    box_lst = list(map(int, input().split()))
    for k in range(N):
        box_lst[idx_max()] -= 1
        box_lst[idx_min()] += 1

    print(f'#{tc} {box_lst[idx_max()]-box_lst[idx_min()]} ')

