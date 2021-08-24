import copy
import sys
sys.stdin = open('11879_input.txt')

def dfs(i, j):
    if i < 0 or j < 0 or j >= N or i >= N: # 벽체크
        return 0
    if arr[i][j] == '1': #벽
        return 0
    if visited[i][j] == '1':
        return 0
    if arr[i][j] == '3':
        visited[i][j] = '1'
        return 1
    visited[i][j] = '1'
    for mode in range(4):
        rst = dfs(i + dx[mode], j + dy[mode])
        if rst:
            return 1
    return 0
T = int(input())
for tc in range(1, T+1):
    print('#{}'.format(tc), end=' ')
    N = int(input())
    arr = [list(input()) for _ in range(N)]
    dx = [0, -1, 0, 1] # 우상좌하
    dy = [-1, 0, 1, 0]
    flag = 0
    x = y = 0
    visited = [[0]*N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            if arr[i][j] == '2':
                x = i
                y = j
    print(dfs(x, y))









