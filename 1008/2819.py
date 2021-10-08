import sys
sys.stdin = open('2819_input.txt')

def check(i, j, num, cnt):
    global ans
    if cnt == 7:
        ans.append(num)
        return
    else:
        dx = [0, 0, 1, -1]
        dy = [1, -1, 0, 0]
        for d in range(4):
            x = i + dx[d]
            y = j + dy[d]
            if 0 <= x < 4 and 0 <= y < 4:
                check(x, y, num+arr[x][y], cnt+1)


for tc in range(1, int(input())+1):
    arr = [input().split() for _ in range(4)]
    ans = []
    for i in range(4):
        for j in range(4):
            check(i, j, arr[i][j], 1)
    print('#{} {}'.format(tc, len(set(ans))))
