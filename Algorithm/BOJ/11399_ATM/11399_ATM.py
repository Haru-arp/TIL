N = int(input())
lst = list(map(int, input().split()))

s_lst = sorted(lst)

sol_lst = [0] * N
for i in range(len(s_lst)):
    if i == 0:
        sol_lst[i] = s_lst[i]
    else:
        sol_lst[i] = sol_lst[i-1] + s_lst[i]

min_time = sum(sol_lst)
print(min_time)