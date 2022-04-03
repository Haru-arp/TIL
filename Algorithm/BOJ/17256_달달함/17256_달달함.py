a = list(map(int, input().split()))
c = list(map(int, input().split()))

b_x = c[0]-a[2]
b_y = c[1]//a[1]
b_z = c[2]-a[0]

print(b_x, b_y, b_z)
