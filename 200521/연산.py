from collections import deque
import sys
sys.stdin = open('연산_input.txt')
def calcul(n, m):
    q = deque()
    q.append((n,0))
    while q:
        x, cnt = q.popleft()
        if x == m:
            return
        for dx in [x+1, x-1, 2*x, x-10]:
            if 0 <= dx <= 1000000 and check[dx] == 0:
                check[dx] = cnt+1
                q.append((dx, cnt+1))

for tc in range(1, int(input())+1):
    N, M = map(int, input().split())
    check = [0] * (1000001)
    calcul(N, M)
    print("#{} {}".format(tc, check[M]))
