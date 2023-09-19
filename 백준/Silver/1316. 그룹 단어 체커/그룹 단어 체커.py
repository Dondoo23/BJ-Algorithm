n = int(input())
word_list = list()

for i in range(n):
    m = input()
    word_list.append(m)

count = 0
for word in word_list:
    check = list()
    l = len(word)
    check.append(word[0])
    for i in range(1,l):
        if (word[i] in check) and (word[i-1] != word[i]):
            count += 1
            break
        elif (word[i] not in check):
            check.append(word[i])

print(n - count)