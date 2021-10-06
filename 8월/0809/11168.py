import sys
sys.stdin = open('11168_input.txt')

T = int(input())
for tc in range(1,T+1):
    H, W = map(int, input().split())
    n = 1
    print('#{}'.format(tc))
    for i in range(H):
        for j in range(W):
            if i%2 == 0:
                result = n + H*j
                print(result, end= ' ')
            else:
                result = n + H*j
                print(result, end= ' ')
        print()
        n += 1



