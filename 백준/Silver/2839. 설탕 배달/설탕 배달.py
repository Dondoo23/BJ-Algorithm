N = int(input())

count = []
count_1 = 0
if N % 3 == 0: # 3으로 나누어 떨어지는 경우 count에 추가
  count.append(N//3)
  
if N % 5 == 0: # 5로 나누어 떨어지는 경우 count에 추가
  count.append(N//5)
  
cnt = 0
N_3 = N
while((N_3-3) >= 0): # 3씩 빼면서
  cnt += 1
  N_3 -= 3
  if N_3 % 3 == 0: # 3으로 나누어진다면 3씩 뺀 횟수 + 3으로 나눈 값
    count.append(N_3//3 + cnt)
    
  if N_3 % 5 == 0: # 3씩 뺀 횟수 + 5로 나눈 값
    count.append(N_3//5 + cnt)

cnt = 0
N_5 = N
while((N_5-5) >= 0): # 5씩 빼면서
  cnt += 1
  N_5 -= 5
  if N_5 % 3 == 0: # 5씩 뺀 횟수 + 3으로 나눈 값
    count.append(N_5//3 + cnt)
    
  if N_5 % 5 == 0: # 5씩 뺀 횟수 + 5로 나눈 값
    count.append(N_5//5 + cnt)
    
ans = 0 # 답
if not count: # count에 추가된 값이 없다면 -1
  ans = -1
else: # count에 추가된 값이 있다면(한번이라도 정확하게 봉지를 나누었다면 그 횟수)
  ans = min(count)

print(ans)
