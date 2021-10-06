import sys
sys.stdin = open('11172_input.txt')
T = int(input())
for tc in range(1, T+1):
    N = int(input())
    result = 1
    print('#{}'.format(tc))
    for i in range(1, N+1):
        for j in range(1, N+1):
            result = i*j
            print(result, end= ' ')
        print()

