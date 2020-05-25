# 다익스트라 : 하나의 시작 정점에서 모든 끝 정점까지의 최단 경로
import heapq

for tc in range(1, int(input())+1):
    V, E = map(int, input().split())
    adj = {i:[] for i in range(V+1)}
    for _ in range(E):
        s, e, c = map(int, input().split())
        adj[s].append([e, c])
        # adj[e].append([s, c])

    # key 가중치, check 이전 노드(어디로 부터 도착한 노드인지)
    key = [float('inf')] * (V+1)
    check = [-1] * (V+1)

    # 시작점 초기화
    key[0] = 0
    pq = []
    heapq.heappush(pq, (0,0))

    # 시작점에서 각각으로 가는 경로 가중치 적용
    while pq:
        k, node = heapq.heappop(pq)
        for dest, wt in adj[node]:
            next_key = key[node] + wt
            if next_key < key[dest]:
                key[dest] = next_key
                check[dest] = node
                heapq.heappush(pq, (next_key, dest))

    print("#{} {}".format(tc, key[V]))