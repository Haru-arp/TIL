import sys

sys.stdin = open('input.txt')

T = 10
for tc in range(1,T+1):

    N = int(input())
    emp = input()

    emp_int = ''
    emp_temp = []
    for str in emp:
        if str == '*':
            emp_temp.append(str)
        elif str == '+':
            while emp_temp:
                emp_int += emp_temp.pop()
            emp_temp.append(str)
        else:
            emp_int += str
    #print(emp_int)
    while emp_temp:
        emp_int += emp_temp.pop()
    print(emp_int)

    result = []
    for str in emp_int:

        if str == '*':
            emp2 = result.pop()
            emp1 = result.pop()
            emp3 = emp1 * emp2
            result.append(emp3)

        elif str == '+':
            emp2 = result.pop()
            emp1 = result.pop()
            emp3 = emp1 + emp2
            result.append(emp3)

        else:
            result.append(int(str))
    print("#{} {}".format(tc, result[0]))