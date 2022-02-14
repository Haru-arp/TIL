arr = list(map(int,input().split()))
lst = []

for i in range( 1 << len(arr)):
    sub_lst = []
    for j in range(len(arr)):
        if i & (1<<j):
            sub_lst.append(arr[j])
    lst.append(sub_lst) #부분집합을 만들어서 빈 리스트에 부분집합 넣기

count = 0     
for k in range(len(lst)):
    sum_r = 0
    for l in lst[k]:
        sum_r += l
    if sum_r == 1:
        count += 1
if count >=1:
    print("1")
else:
    print("0")





    