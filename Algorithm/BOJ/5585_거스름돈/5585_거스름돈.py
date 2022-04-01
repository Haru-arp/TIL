coin_lst = [500, 100, 50, 10, 5, 1]
money = int(input())
s_money = 1000 - money
cnt = 0

for _ in range(6):
    if s_money >= 500:
        cnt = cnt + (s_money // 500)
        s_money %= 500
        
    elif s_money >= 100:
        cnt = cnt + (s_money // 100)
        s_money %= 100

    elif s_money >= 50:
        cnt = cnt + (s_money // 50)
        s_money %= 50

    elif s_money >= 10:
        cnt = cnt + (s_money // 10)
        s_money %= 10

    elif s_money >= 5:
        cnt = cnt + (s_money // 5)
        s_money %= 5
    
    else:
        cnt = cnt + (s_money // 1)
        s_money %= 1

print(cnt)



