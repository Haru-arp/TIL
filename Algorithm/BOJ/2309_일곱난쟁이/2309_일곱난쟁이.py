dwarfs = [int(input()) for _ in range(9)]

dwarfs.sort()
dwarfs_sum = sum(dwarfs)

num_1 = 0
num_2 = 0

for i in range(9):
    for j in range(i+1, 9):
        if dwarfs_sum - (dwarfs[i] + dwarfs[j]) == 100:
            num_1, num_2 = dwarfs[i], dwarfs[j]

            break
dwarfs.remove(num_1)
dwarfs.remove(num_2)

for dwarf in dwarfs:
    print(dwarf)

