word = input().lower() #입력한 문자를 소문자로 입력받기
word_list = list(set(word)) #중복 제거 후 리스트로 묶기
cnt = []

for i in word_list:
    count = word.count(i)
    cnt.append(count)

if cnt.count(max(cnt)) >= 2:
    print("?")
else:
    print(word_list[(cnt.index(max(cnt)))].upper())