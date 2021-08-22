import sys
sys.stdin = open('1961_input.txt')

T = int(input())
for tc in range(1, T+1):
    print('#{}'.format(tc))
    N = int(input())
    arr = [input().split() for _ in range(N)]
    for i in range(N):
        for j in range(N):
            print(arr[N - j - 1][i], end='')
        print(' ', end='')
        for j in range(N):
            print(arr[N - i - 1][N - j - 1], end='')
        print(' ', end='')
        for j in range(N):
            print(arr[j][N - i - 1], end='')
        print()





