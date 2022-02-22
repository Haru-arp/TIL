# 클래스 선언
class Stack:

    # 초기 설정, 스택으로 사용할 리스트 선언
    def __init__(self):
        self.stack = []

    # In 함수 / Push 함수 List의 Append 함수 이용
    def push(self, data):
        self.stack.append(data)

    # Out 함수 / Pop 함수, List의 pop함수 이용
    def pop(self):
        if len(self.stack) <= 0:
            return ("No Data in Stack")
        else:
            return self.stack.pop()


stk = Stack()
stk.push("1")
stk.push("2")
stk.push("3")

stk.pop()
stk.pop()
stk.pop()
print(stk.stack)