import sys
sys.stdin = open('input.txt')
def check_danjo(num):
    num_str = str(num)
    for k in range(len(num_str)-1):
        if num_str[k] > num_str[k+1]:
            return False
    return True

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    num_lst = list(map(int, input().split()))
    result = -1
    ans_lst = []
    for i in range(len(num_lst)):
        for j in range(i+1, len(num_lst)):
            num = num_lst[i] * num_lst[j]

            if result < num and check_danjo(num):
                result = num
                ans_lst.append(result)
    print(ans_lst)

    ans = max(ans_lst)
    print(f'#{tc} {ans}')