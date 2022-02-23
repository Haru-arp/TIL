import sys

sys.stdin = open('input.txt')

T = int(input())


for tc in range(1, T + 1):
    text = input()
    ans = '' # 후위 표기법 나타낼 문자열

    stack = []

    for t in text:
        if t == '+' or t == '-' or t == '*' or t == '/': #연산자라면)
            stack.append(t) #스택에 연산자를 넣어주고)
        else:
            ans += t #숫자라면 빈 문자열에 넣어준다.
    while len(stack) > 0: #스택의 길이가 0보다 크면 반복하는데
        ans += stack.pop() #스택의 탑의 것들을 pop 해주면서 ans에 넣어준다.

    print(f'#{tc} {ans}')
