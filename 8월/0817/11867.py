import sys
sys.stdin = open('11867_input.txt')

def get_palindrome(array, n, m):
    for x in range(n):
        for y in range(n-m+1):
            for i in range(m//2+1):
                if array[x][y+i] != array[x][y+m-i-1]:
                    break
            else:
                return [x, y ,1]

            for j in range(m//2+1):
                if array[y+j][x] != array[y+m-j-1][x]:
                    break
            else:
                return [x, y, 2]


T = int(input())
for tc in range(1, T+1):
    print('#{}'.format(tc), end=' ')
    N, M = map(int, sys.stdin.readline().split())
    arr = [input() for _ in range(N)]
    ans = get_palindrome(arr, N, M)
    for i in range(M):
        if ans[2] == 1:
            print(arr[ans[0]][ans[1]+i], end='')
        else:
            print(arr[ans[1]+i][ans[0]], end='')
    print()