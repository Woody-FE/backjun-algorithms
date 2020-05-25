for tc in range(1, int(input())+1):
    # 세로 N, 가로 M, 시간 K
    N, M, K = map(int, input().split())
    cnt = 0
    inactive_cell = {}
    active_cell = {}
    dead_cell = {}
    MAP = [list(map(int, input().split())) for _ in range(N)]
    # 초기값 구성
    for i in range(N):
        for j in range(M):
            if MAP[i][j] != 0:
                inactive_cell[(i, j)] = [MAP[i][j], MAP[i][j]]
    # K동안 반복
    for i in range(1, K+1):
        active_move_cell = {}
        dead_move_cel = {}
        for key, value in inactive_cell.items():
            if value[1] > 1:
                inactive_cell[key][1] -= 1
            else:
                active_move_cell[key] = [inactive_cell[key][0], inactive_cell[key][0]]
        for key, value in active_cell.items():
            x, y = key
            for dx, dy in [(1, 0), (-1, 0), (0,-1), (0, 1)]:
                cx, cy = x + dx, y + dy
                if (cx, cy) not in inactive_cell and (cx, cy) not in active_cell and (cx, cy) not in dead_cell:
                    inactive_cell[(cx,cy)] = [value[0], value[0]]
            if value[1] > 1:
                active_cell[key][1] -= 1
            else:
                dead_move_cel[key] = dead_move_cel.get(key, value)

        for k in dead_move_cel:
            dead_cell[k] = active_cell[k]
            del active_cell[k]

        for k, value in active_move_cell.items():
            active_cell[k] = value
            del inactive_cell[k]
        # print("k{} active{}".format(i, active_cell))
        # print("k{} inactive{}".format(i, inactive_cell))
    for i in active_cell:
        cnt += 1
    for i in inactive_cell:
        cnt += 1
    print("#{} {}".format(tc, cnt))