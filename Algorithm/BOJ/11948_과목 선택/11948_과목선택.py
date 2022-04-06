sum = 0
A = []
for _ in range(4):
    A.append(int(input()))

A.sort()


for i in range(1, 4):
    sum += A[i]

B = []
for _ in range(2):
    B.append(int(input()))
B.sort()
sum += B[1]

print(sum)