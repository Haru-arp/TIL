import sys

sys.stdin = open('input.txt')

T = int(input())


for tc in range(1, T + 1):
    Forth = list(map(str, input().split()))
    stack = []
    for i in range(len(Forth)):
        if Forth[i].isdigit():
            stack.append(Forth[i])
        else:
            #문자열일 경우 마침표가 올 때 먼저 확인
            if Forth[i] == '.':
                if len(stack) == 1:
                    print(f'#{tc}', end=' ')
                    print(*stack)
                    break
                else:
                    print(f'#{tc}', end=' ')
                    print('error')
                    break
            #마침표가 아닐 때 계산해줌
            if len(stack) > 1:
                num1, num2 = int(stack.pop()), int(stack.pop())
                if Forth[i] == '+':
                    stack.append(num2+num1)
                if Forth[i] == '-':
                    stack.append(num2-num1)
                if Forth[i] == '*':
                    stack.append(num2*num1)
                if Forth[i] == '/':
                    stack.append(num2//num1)
            else: #스택에 문자가 1개 이하일때 문자열이 오면 error
                print(f'#{tc}', end=' ')
                print('error')
                break


