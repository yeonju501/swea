import sys
sys.stdin = open('11760_input.txt')

def change(n, x, y, hap):
    if x == n and y == n:
        hap += arr[x][y]
        result.append(hap)
        return
    elif x == n:
        hap += arr[x][y]
        change(n, x, y+1, hap)
    elif y == n:
        hap += arr[x][y]
        change(n, x+1, y, hap)
    else:
        hap += arr[x][y]
        change(n, x+1, y, hap)
        change(n, x, y+1, hap)

for tc in range(1, int(input())+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    ans = []
    result = []
    change(N-1, 0, 0, 0)
    print('#{} {}'.format(tc, min(result)))