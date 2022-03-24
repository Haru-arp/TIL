T = [73, 74, 75, 71, 69, 72, 76, 73]

answer = [0] * len(T)
stack = []

for idx, curr in enumerate(T):
    while stack and curr > T[stack[-1]]:
        last = stack.pop()
        answer[last] = idx - last
    stack.append(idx)

print(answer)





