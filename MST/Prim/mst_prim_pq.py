import heapq
# V 정점, E 간
V, E = map(int, input().split())
# 인접한 정점
adj = {i: [] for i in range(1,V+1)}
# 간선 수 만큼 포문 반복해서 초기화
for i in range(E):
    # s 시작, e 도착, c가중
    s, e, c = map(int, input().split())
    adj[s].append([e,c])
    adj[e].append([s,c])
#print(adj)

# key, mst, 우선순위큐 준비
INF = float('inf')
key = [INF] * (V+1)
mst = [False] * (V+1)
pq = []

# 시작 정점 선택: 1
key[1] = 0

# 큐에 시작 정점을 넣음 => (key, 정점이 되는 인덱스)
# 우선순위 큐 -> 이진힙 -> heapq 라이브러리 사용
# 힙큐에다가 시작점 푸쉬 -> key를 우선순위로 하기위에 앞에다가 배치
heapq.heappush(pq, (0, 1))
result = 0
while pq:
    # 최소값 찾기
    k, node = heapq.heappop(pq)
    # mst로 선택
    if mst[node] == False:
        result += k
        mst[node] = True
    # key 갱신 => key 배열 / 큐
    # dest 목적지, wt 가중치
    for dest, wt in adj[node]:
        if not mst[dest] and key[dest] > wt:
            key[dest] = wt
            # 큐 갱신 => 새로운 (key, 정점) 삽입 => 필요없는 원소는 스킵 => 이렇게하면 pop할 요소가 줄어듬
            heapq.heappush(pq, (key[dest], dest))

