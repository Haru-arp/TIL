N = int(input()) # 날짜의 1의 자리 숫자
car = list(map(int, input().split()))
cnt = 0
for i in range(len(car)):
    if N == car[i]:
        cnt += 1
    
print(cnt)