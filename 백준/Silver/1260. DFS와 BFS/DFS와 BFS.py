def dfs(c):
    vs[c] = 1 # 방문 표시
    ans_dfs.append(c) # 방문 노드 추가
    for n in adj[c]:
        if not vs[n]: # 방문하지 않은 노드인 경우
            dfs(n)
            
def bfs(s):
    q = []
    
    q.append(s) # q에 초기데이터 삽입
    vs[s] = 1
    ans_bfs.append(s)
    
    while q:
        c = q.pop(0)  
        for n in adj[c]:
            if not vs[n]: # 방문하지 않은 노드라면 큐에 삽입
                q.append(n)
                vs[n] = 1
                ans_bfs.append(n)
                
            
    while q:
        s = q.pop(0)
        if not vs[s]:
            bfs(s)

n, m, v = map(int,input().split()) # n개의 정점, m개의 간선, 시작 정점v

adj = [[] for _ in range(n+1)]

for _ in range(m):
    s, e = map(int,input().split())
    adj[s].append(e)
    adj[e].append(s) # 양방향
    
for i in range(1,n+1): # 오름차순 정렬
    adj[i].sort() 

vs = [0]*(n+1)
ans_dfs = []
dfs(v)

vs = [0]*(n+1)
ans_bfs = []
bfs(v)

print(*ans_dfs)
print(*ans_bfs)