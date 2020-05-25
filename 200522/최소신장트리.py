import sys
sys.stdin = open('최소이동거리_input.txt')
import heapq
for tc in range(1, int(input())+1):
    V, E = map(int, input().split())
    adj = {i:[] for i in range(V+1)}
    for _ in range(E):
        s, e, c = map(int, input().split())
        adj[s].append([e, c])
        adj[e].append([s, c])

    key = [float('inf')] * (V+1)
    MST = [False] * (V+1)

    key[0] = 0
    pq = []
    heapq.heappush(pq, (0,0))
    result = 0
    while pq:
        k, node = heapq.heappop(pq)
        if MST[node]:
            continue
        MST[node] = True
        result += k
        for dest, wt in adj[node]:
            if not MST[dest] and key[dest] > wt:
                key[dest] = wt
                heapq.heappush(pq, (key[dest], dest))
    print("#{} {}".format(tc, result))