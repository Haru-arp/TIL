M = int(input())
N = int(input())
lst = []

for i in range(1, N+1):
    if (i*i >=M and i*i <=N):
        lst.append(i)
min = N*N
sum = 0
for j in lst:
    sum += j*j
    if j*j <= min:
        min = j*j
if sum == 0:
    print(-1)
else:
    print(sum)
    print(min)
