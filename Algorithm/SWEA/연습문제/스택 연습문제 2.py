def check(line):
    # 스택 초기화
    stack = []
    # 길이만큼 반복하면서 확인
    for char in line:
        # 만약 열린괄호가 온다면 스택에 추가해줌
        if char == '(' or char == '{':
            stack.append(char)
        # 만약 닫힌 괄호가온다면
        elif char == ')' or char == '}':
            # 검사할 스택이 없다면 비어있는것!
            if not stack:
                return 0
            # 스택의 가장위가 가장 안의 괄호이기 때문에 팝으로 확인
            # pop을 비교문에만 써도 pop이 실행됨
            elif char == ')' and stack.pop() != '(':
                return 0
            elif char == '}' and stack.pop() != '{':
                return 0
    # 만약 여는 괄호가 남아있다면 no
    if stack:
        return 0
    return 1


print("#{} {}".format(tc, check(line)))