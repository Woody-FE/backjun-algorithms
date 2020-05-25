### 미해결 ###

from collections import deque
def search():
    while q:
        global result
        a, b, direct, val = q.popleft()
        if direct == 0:
            da, db = a, b+1
            if 0 <= da < 2001 and 0 <= db < 2001:
                if check[da][db] != 0 and check[a][b] !=0:
                    result += check[a][b]
                    check[a][b] = 0
                    result += check[da][db]
                    check[da][db] = 0
                elif check[da][db] == 0 and check[a][b] != 0:
                    q.append((da, db, direct, val))
                    check[da][db] = check[a][b]
                    check[a][b] = 0
        elif direct == 1:
            da, db = a, b-1
            if 0 <= da < 2001 and 0 <= db < 2001:
                if check[da][db] != 0 and check[a][b] !=0:
                    result += check[a][b]
                    check[a][b] = 0
                    result += check[da][db]
                    check[da][db] = 0
                elif check[da][db] == 0 and check[a][b] !=0:
                    q.append((da, db, direct, val))
                    check[da][db] = val
                    check[a][b] = 0
        elif direct == 2:
            da, db = a-1, b
            if 0 <= da < 2001 and 0 <= db < 2001:
                if check[da][db] != 0 and check[a][b] !=0:
                    result += check[a][b]
                    check[a][b] = 0
                    result += check[da][db]
                    check[da][db] = 0
                elif check[da][db] == 0 and check[a][b] !=0:
                    q.append((da, db, direct, val))
                    check[da][db] = val
                    check[a][b] = 0
        else:
            da, db = a+1, b
            if 0 <= da < 2001 and 0 <= db < 2001:
                if check[da][db] != 0 and check[a][b] !=0:
                    result += check[a][b]
                    check[a][b] = 0
                    result += check[da][db]
                    check[da][db] = 0
                elif check[da][db] == 0 and check[a][b] !=0:
                    q.append((da, db, direct, val))
                    check[da][db] = val
                    check[a][b] = 0

for tc in range(1, int(input())+1):
    N = int(input())
    result = 0
    check = [[0 for _ in range(2001)] for _ in range(2001)]
    q = deque()
    for _ in range(N):
        x, y, d, K = map(int, input().split())
        i, j = x + 1000, y + 1000
        q.append((i, j, d, K))
        check[i][j] = K
    search()
    print("#{} {}".format(tc, result))

