def make_set(x):
    p[x] = x

def find_set(x):
    if p[x] == x:
        return x
    else:
        # path compression
        p[x] = find_set(p[x])
        return p[x]

def union(x, y):
    px = find_set(x)
    py = find_set(y)
    if px != py:
        p[py] = px
    # if rank[px] > rank[py]:
    #     p[py] = px
    # else:
    #     p[px] = py
    #     if rank[px] == rank[py]:
    #         rank[py] += 1

V, E = map(int, input().split())
edges = [list(map(int, input().split())) for _ in range(E)]

# 간선을 간선가중치를 기준으로 연결
edges.sort(key=lambda x:x[2])

# make_set : 모든 정점에 대해 집합 생성
p = [0] * V
# 부모노드의 서브트리 깊이 => rank
# rank = [0] * V
for i in range(V):
    make_set(i)

# result 간선가중치, cnt 간선 갯수
cnt, result = 0, 0
mst = []
# 모든 간선에 대해서 반복 -> V-1개의 간선이 선택될 때 까지
for i in range(E):
    s, e, c = edges[i][0], edges[i][1], edges[i][2]
    # 사이클이면 스킵 : 간선의 두 정점이 서로 다른 집합(부모)이면 find_set
    if find_set(s) == find_set(e):
        continue
    result += c
    mst.append(edges[i])
    cnt += 1
    if cnt == V-1:
        break

#print(result) 간선가중치 합
#print(cnt) 간선 갯수
