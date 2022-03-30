
Number = ['ABC', 'DEF', 'GHI', 'JKL', 'MNO', 'PQRS', 'TUV', 'WXYZ']

li = list(input())

rlt = 0

for i in li:
    for j in Number:
        if i in j:
            rlt += Number.index(j)+3

print(rlt)