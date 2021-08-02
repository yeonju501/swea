for T in range(int(input())):
    N = int(input())
    route = [[0]*N for _ in range(N)]
    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]
    mode = 0
    x = y = 0
    route[x][y] = 1
    for i in range(2, N**2+1):
        x += dx[mode]
        y += dy[mode]
        route[x][y] = i
        if 0 <= x + dx[mode] < N and 0 <= y + dy[mode] < N and not route[x+dx[mode]][y+dy[mode]]:
            continue
        if mode != 3:
            mode += 1
        else:
            mode = 0
    print(f'{T+1}')
    for i in route:
        print(*i)

