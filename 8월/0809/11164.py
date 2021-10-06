import sys
sys.stdin = open('11164_input.txt') #default = 'r' (read)
T = int(input())
for tc in range(1, T+1):
    H, W = map(int, input().split())
    n = 0
    print('#{}'.format(tc))
    for i in range(H):
        for j in range(W):
            if i % 2:
                if j == 0:
                    n += W
                print(n-j, end=' ')
            else:
                n += 1
                print(n, end=' ')
        print()
