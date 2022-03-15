import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    pizza = list(map(int, input().split()))
    cheese = []

    for i in range(M):
        cheese.append([i+1, pizza[i]]) #리스트에 인덱스와 함께 치즈 값 넣어주기
    in_pizza = cheese[:N] #화덕에 N개만 넣을 수 있음.
    remain_pizza = cheese[N:]

    while len(in_pizza) > 1: #하나만 남으면 끝
        check = in_pizza.pop(0) #일단 맨 앞에 피자 꺼내고\
        check[1] //= 2 #[0]이면 인덱스 숫자, [1]이면 치즈의 값
        if check[1] == 0:
            if remain_pizza:
                in_pizza.append(remain_pizza.pop(0))
        else: #치즈가 0이 아니라면 다시 넣는다.
            in_pizza.append(check)

    print(f'#{tc} {in_pizza[0][0]}')