import sys
sys.stdin = open('11159_input.txt') #default = 'r' (read)

T = int(input())
for tc in range(1, T+1):
    H, W = map(int, input().split())
    num = 1
    print('#{}'.format(tc))
    for i in range(H):
        for j in range(W):
            print(num, end=' ')
            num += 1
        print()

