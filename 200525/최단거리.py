import heapq

V, E = map(int, input().split())
K = int(input())
adj = {i:[] for i in range(1, V+1)}
for _ in range(E):
    s, e, c = map(int, input().split())
    adj[s].append([e, c])

# key 가중치
key = [float('inf')] * (V+1)

# 시작점 초기화
key[K] = 0
pq = []
heapq.heappush(pq, (0,K))

# 시작점에서 각각으로 가는 경로 가중치 적용
while pq:
    k, node = heapq.heappop(pq)

    for dest, wt in adj[node]:
        next_key = key[node] + wt
        if next_key < key[dest]:
            key[dest] = next_key
            heapq.heappush(pq, (next_key, dest))

for i in range(1, V+1):
    if key[i] > 123456789:
        print("INF")
    else:
        print(key[i])
