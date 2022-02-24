import sys

sys.stdin = open('input.txt')

T = 10
for tc in range(1, T + 1):
    N = int(input())
    Data = input()
    stack = []
    num_lst = []

    icp = {'*': 2, '+': 1, '(': 3} #넣을 때
    isp = {'*': 2, '+': 1, '(': 0} #스택 안

    #후위표기법
    for i in range(N):
        #숫자일때 숫자리스트 넣기
        if Data[i].isdigit():
            num_lst.append(Data[i])

        #연산자일때
        else:
            #스택이 빈 경우는 무조건 append 해야된다 괄호가 열린 괄호일때..
            if not stack:
                stack.append(Data[i])
                continue

            elif stack:
                #닫는 괄호인 경우에는 여는 괄호가 나올 때 까지 pop
                if Data[i] == ')':
                    while stack[-1] != '(':
                        num_lst.append(stack.pop())
                    stack.pop()
                #icp & isp 비교하자
                elif icp[Data[i]] > isp[stack[-1]]:
                    stack.append(Data[i])
                else:
                    #icp가 isp보다 작으면 계속 pop하고 연산자리스트에 append
                    while icp[Data[i]] <= isp[stack[-1]]:
                        num_lst.append(stack.pop())
                    stack.append(Data[i])
    #print(num_lst)
    #계산하기
    for i in range(len(num_lst)):
        if num_lst[i].isdigit():
            stack.append(num_lst[i])

        else:
            num2 = int(stack.pop())
            num1 = int(stack.pop())

            if num_lst[i] == "+":
                result = num1 + num2
            elif num_lst[i] == "*":
                result = num1 * num2

            stack.append(str(result))

    print(f'#{tc} {stack[0]}')

