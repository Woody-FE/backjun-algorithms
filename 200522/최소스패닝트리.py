import heapq
V, E = map(int, input().split())
adj = {i:[] for i in range(1, V+1)}
for _ in range(E):
    s, e, c = map(int, input().split())
    adj[s].append([e,c])
    adj[e].append([s,c])

key = [float('inf')] * (V+1)
mst = [False] * (V+1)
pq = []
heapq.heappush(pq, (0, 1))
key[1] = 0
result = 0
while pq:
    k, node = heapq.heappop(pq)
    if not mst[node]:
        result += k
        mst[node] = True
    else:
        continue
    for dest, wt in adj[node]:
        if not mst[dest] and key[dest] > wt:
            key[dest] = wt
            heapq.heappush(pq, (key[dest], dest))
print(result)
