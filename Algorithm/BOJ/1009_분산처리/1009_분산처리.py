T = int(input())

for tc in range(1, T+1):
    a, b = map(int, input().split())

    if a == 1:
        print(1)
    else:
        last = a % 10
        last_num = [last]
        sum_last = (last ** 2 ) % 10
        while sum_last not in last_num:
            last_num.append(sum_last)
            sum_last = (sum_last * last) % 10
        if last_num[(b-1)%len(last_num)] == 0:
            print(10)
        else:
            print(last_num[(b-1)%len(last_num)])

