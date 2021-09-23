import sys
sys.stdin = open('4615_input.txt')

T = int(input())
N, M = map(int, input().split())
arr = [[0] * N for _ in range(N)]
black = [[N//2-1, N//2], [N//2, N//2-1]]
white = [[N//2-1, N//2-1], [N//2,N//2]]
arr[N//2-1][N//2-1] = 2
arr[N//2-1][N//2] = 1
arr[N//2][N//2-1] = 1
arr[N//2][N//2] = 2
b = w = 0
for _ in range(M):
    x, y, s = map(int, input().split())
    x -= 1
    y -= 1
    if s == 1:
        arr[x][y] = 1
        black.append([x, y])
        for i in black:
            if i[0] == x:
                for j in white:
                    if j[0] == x:
                        white.remove(j)
            if i[1] == y:
                for j in white:
                    if j[1] == y:
                        white.remove(j)


    elif s == 2:
        arr[x][y] = 2
        white.append(([x, y]))




for i in range(N):
    print(arr[i])
    b += arr[i].count(1)
    w += arr[i].count(2)
print(b, w)

