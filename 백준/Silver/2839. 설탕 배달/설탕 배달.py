N = int(input())

count = []
count_1 = 0
if N % 3 == 0: # 3으로 나누어 떨어질때
  count.append(N//3)
if N % 5 == 0:
  count.append(N//5)
  
cnt = 0
N_3 = N
while((N_3-3) >= 0):
  cnt += 1
  N_3 -= 3
  if N_3 % 3 == 0:
    count.append(N_3//3 + cnt)
  if N_3 % 5 == 0:
    count.append(N_3//5 + cnt)

cnt = 0
N_5 = N
while((N_5-5) >= 0):
  cnt += 1
  N_5 -= 5
  if N_5 % 3 == 0:
    count.append(N_5//3 + cnt)
  if N_5 % 5 == 0:
    count.append(N_5//5 + cnt)
ans = 0
if not count:
  ans = -1
else:
  ans = min(count)

print(ans)