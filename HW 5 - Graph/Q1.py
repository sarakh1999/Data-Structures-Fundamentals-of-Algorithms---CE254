def BFS(Adj, s, mid, level):
    i = 1
    frontier = [s]
    level[s] = 0
    while frontier:
        next = []
        for u in frontier:
            for v, ind in Adj[u]:
                if ind > mid:
                    continue
                if level[v] == -1:
                    level[v] = i
                    next.append(v)
                elif (level[v] == level[u]):
                    return 1
        frontier = next
        i += 1
    return -1


def bfs(Adj, mid):
    level = [-1 for i in range(n)]
    for s in range(n):
        if level[s] == -1:
            if BFS(Adj, s, mid, level) == 1:
                return 1
    return -1


n, m = map(int, input().split())
adj = [[] for i in range(n)]
for i in range(m):
    u, v = map(int, input().split())
    u, v = u - 1, v - 1
    adj[u].append((v, i))
    adj[v].append((u, i))
start, end = 0, m
flag = True
while end - start > 1:
    mid = (end + start) // 2
    # 2 bakhshi nist
    if (bfs(adj, mid) != -1):
        end = mid
        flag=False
    else:
        start = mid
if(flag==False):
    print(end+1)
else:
    print(-1)
