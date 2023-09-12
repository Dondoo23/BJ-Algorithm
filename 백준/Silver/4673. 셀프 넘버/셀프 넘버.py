number = set(range(1,10001))
new_number = set()
result = 0

for i in range(1,10001):
    result = i
    for j in str(i):
        result += int(j)
    new_number.add(result)
    
self_num = sorted(number - new_number)
for i in self_num:
    print(i)