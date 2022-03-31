N, K = map(int, input().split())

coin_lst = []
for _ in range(N):
    coin_lst.append(int(input()))

count = 0
for i in range(N-1, -1, -1):
    if K == 0:
        break
    if coin_lst[i] > K:
        continue
    count += K//coin_lst[i]
    K %= coin_lst[i]
print(count)
