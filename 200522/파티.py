import heapq
# N학생수, M개의 단방향 도로, X마을에서 파티
N, M, X = map(int, input().split())
adj = {i: [] for i in range(1, N+1)}

for _ in range(M):
    s, e, c = map(int, input().split())
    adj[s].append([e,c])

arr = [0] * (N+1)
for i in range(1, N+1):
    dist = [float('inf')] * (N+1)
    dist[i] = 0
    pq = []
    heapq.heappush(pq, (0, i))

    while pq:
        dst, node = heapq.heappop(pq)
        for dest, wt in adj[node]:
            next_dst = dist[node] + wt
            if next_dst < dist[dest]:
                dist[dest] = next_dst
                heapq.heappush(pq, (next_dst, dest))
    # print("i{}, distX{}".format(i, dist[X]))
    arr[i] += dist[X]

dist = [float('inf')] * (N + 1)
dist[X] = 0
pq = []
heapq.heappush(pq, (0, X))

while pq:
    dst, node = heapq.heappop(pq)
    for dest, wt in adj[node]:
        next_dst = dist[node] + wt
        if next_dst < dist[dest]:
            dist[dest] = next_dst
            heapq.heappush(pq, (next_dst, dest))

for i in range(1, N+1):
    arr[i] += dist[i]

print(max(arr))
