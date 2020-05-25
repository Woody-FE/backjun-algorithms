import sys
sys.stdin = open('최소이동거리_input.txt')
import heapq

for tc in range(1, int(input())+1):
    V, E = map(int, input().split())
    adj = {i:[] for i in range(V+1)}
    for _ in range(E):
        s, e, c = map(int, input().split())
        adj[s].append([e, c])
    key = [float('inf')] * (V+1)
    # check = [-1] * (V+1)

    key[0] = 0
    pq = []
    heapq.heappush(pq, (0,0))

    while pq:
        k, node = heapq.heappop(pq)
        for dest, wt in adj[node]:
            next_key = key[node] + wt
            if next_key < key[dest]:
                key[dest] = next_key
                # check[dest] = node
                heapq.heappush(pq, (next_key, dest))

    print("#{} {}".format(tc, key[V]))