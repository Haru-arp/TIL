n, k = 25, 5
result = 0

# while n >= k:
#     while n % k != 0:
#         n -= 1
#         result += 1
#     n //= k
#     result += 1
#
# while n > 1:
#     n -= 1
#     result += 1
#
# print(result)

while True:
    target = (n // k) * k
    result += (n - target)
    n = target
    if n < k:
        break
    result += 1
    n //= k
result += (n-1)
print(result)