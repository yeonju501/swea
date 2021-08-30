import sys
sys.stdin = open('11671_input.txt')

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(input()) for _ in range(N)]
    dx = [0, -1, 0, 1, 0, -2, 0, 2, 0, -3, 0, 3]
    dy = [1, 0, -1, 0, 2, 0, -2, 0, 3, 0,-3, 0]
    g = {'A': [], 'B': [], 'C': []}
    for i in range(N):
        for j in range(N):
            if arr[i][j] == 'A':
                g['A'].append([i, j])
            elif arr[i][j] == 'B':
                g['B'].append([i, j])
            elif arr[i][j] == 'C':
                g['C'].append([i, j])

    for key in g.keys():
        if g[key] and key == 'A':
            for a in g[key]:
                i = a[0]
                j = a[1]
                arr[i][j] = 'F'
                for d in range(4):
                    if 0 <= i + dx[d] < N and 0 <= j + dy[d] < N and arr[i+dx[d]][j+dy[d]] == 'H':
                        arr[i+dx[d]][j+dy[d]] = 'F'
        if g[key] and key == 'B':
            for a in g[key]:
                i = a[0]
                j = a[1]
                arr[i][j] = 'F'
                for d in range(8):
                    if 0 <= i + dx[d] < N and 0 <= j + dy[d] < N and arr[i + dx[d]][j + dy[d]] == 'H':
                        arr[i + dx[d]][j + dy[d]] = 'F'
        if g[key] and key == 'C':
            for a in g[key]:
                i = a[0]
                j = a[1]
                arr[i][j] = 'F'
                for d in range(12):
                    if 0 <= i + dx[d] < N and 0 <= j + dy[d] < N and arr[i + dx[d]][j + dy[d]] == 'H':
                        arr[i + dx[d]][j + dy[d]] = 'F'
    cnt = 0
    for i in range(N):
        for j in range(N):
            if arr[i][j] == 'H':
                cnt += 1
    print('#{} {}'.format(tc, cnt))
