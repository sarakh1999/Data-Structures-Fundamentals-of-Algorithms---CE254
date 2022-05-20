import heapq
from math import inf


def dijkstra(spt, dist):
    while len(spt) > 0:
        d, node = heapq.heappop(spt)
        while len(spt) > 0 and mark[node]:
            d, node = heapq.heappop(spt)
        mark[node] = 1
        for v, c in adj[node]:
            if dist[v] > dist[node] + c:
                dist[v] = dist[node] + c
                heapq.heappush(spt, (dist[v], v))
    return dist


n, m = map(int, input().split())
s, t = map(int, input().split())
s, t = s - 1, t - 1
adj = [[] for i in range(2 * n)]
mark = [0 for i in range(2 * n)]
dist = [inf for i in range(2 * n)]
dist[s] = 0

for i in range(m):
    first, second, weight = map(int, input().split())
    first, second = first - 1, second - 1
    if weight % 2 == 0:
        adj[first].append((second, weight))
        adj[first + n].append((second + n, weight))
    else:
        adj[first].append((second + n, weight))
        adj[first + n].append((second, weight))

spt = [(inf, i) for i in range(2 * n)]
spt[s] = (0, s)
heapq.heapify(spt)
d = dijkstra(spt, dist)
if d[t] == inf:
    print(-1)
else:
    print(d[t])
