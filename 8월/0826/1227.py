import sys
sys.stdin = open('1227_input.txt')

def bfs(i, j):
    dx = [0, 1, 0, -1] # 좌하우상
    dy = [-1, 0, 1, 0]
    q = []
    q.append([i, j])
    while q:
        a = q.pop(0)
        i = a[0]
        j = a[1]
        visited[i][j] = 1
        for mode in range(4):
            if 0 <= i+dx[mode] < 100 and 0 <= j+dy[mode] < 100:
                if arr[i+dx[mode]][j+dy[mode]] == '3' and not visited[i+dx[mode]][j+dy[mode]]:
                    return 1
                if arr[i+dx[mode]][j+dy[mode]] == '0' and not visited[i+dx[mode]][j+dy[mode]]:
                    q.append([i+dx[mode], j+dy[mode]])
    return 0


for tc in range(1, 11):
    T = input()
    print('#{}'.format(tc), end=' ')
    arr = [list(input()) for _ in range(100)]
    visited = [[0] * 100 for _ in range(100)]
    for i in range(100):
        for j in range(100):
            if arr[i][j] == '2':
                print(bfs(i, j))
                break
