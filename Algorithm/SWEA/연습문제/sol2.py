

def convert_to_string(num, base=10):
    if num // base == 0:
        return chr(num + ord('0'))
    return convert_to_string(num // base, base) + chr(num % base + ord('0'))

print ("숫자를 입력하세요:")
integer = int(input())
print(convert_to_string(integer), type(convert_to_string(integer)))