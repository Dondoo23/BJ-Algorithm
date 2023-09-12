N = int(input())
data = list(map(int, input().split()))
max_score = max(data)

result = 0

for score in data:
    result += score / max_score * 100

result /= N
print(result)