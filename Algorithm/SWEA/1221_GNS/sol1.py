import sys

sys.stdin = open('input.txt')

T = int(input())
for t in range(1, T+1):
    N = input()
    str_dict = {"ZRO":0, "ONE":0, "TWO":0, "THR":0, "FOR":0, "FIV":0, "SIX":0, "SVN":0, "EGT":0, "NIN":0}
    str_lst = input().split()
    result = ''
    for s in str_lst:
        str_dict[s] += 1

    for key, value in str_dict.items():
        temp = ' '.join([key] * value)
        result += temp + ' '
    print(f'#{t} ')
    print(result[:len(result)-1])


