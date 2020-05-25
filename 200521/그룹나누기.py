import sys
sys.stdin = open('그룹나누기_input.txt')

def make_set(n):
    p[n] = n

def find_set(n):
    if n == p[n]:
        return n
    else:
        p[n] = find_set(p[n])
        return p[n]

def union(x, y):
    global cnt
    root_x, root_y = find_set(x), find_set(y)
    if root_x != root_y:
        p[root_y] = root_x
        cnt += 1
for tc in range(1, int(input())+1):
    N, M = map(int, input().split())
    cnt = 0
    p = [0] * (N+1)
    for i in range(1, N+1):
        make_set(i)
    arr = list(map(int, input().split()))
    for i in range(M):
        union(arr[2*i], arr[2*i+1])
    print("#{} {}".format(tc, N-cnt))

