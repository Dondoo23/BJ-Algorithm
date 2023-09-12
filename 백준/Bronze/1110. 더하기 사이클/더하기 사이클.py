N = int(input())
result = N

count = 0

while True:
    count += 1
    first = result // 10
    second = result % 10
    new = (first + second) % 10
    result = second * 10 + new
    if result == N:
        break

print(count)