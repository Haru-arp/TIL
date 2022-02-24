T = int(input())
for tc in range(1, T+1):
    mars_math = list(map(str, input().split()))
    answer = 0
    for i in range(len(mars_math)):
        if i == 0:
            answer += float(mars_math[i])
        else:
            if mars_math[i] == '@':
                answer *= 3
            elif mars_math[i] == '%':
                answer += 5
            elif mars_math[i] == '#':
                answer -= 7
    print("%0.2f" %answer)