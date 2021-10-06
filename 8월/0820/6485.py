import sys
sys.stdin = open('6485_input.txt')

T = int(input())
for tc in range(1, T+1):
    print('#{}'.format(tc), end=' ')
    N = int(input())
    A = [0] * 5001
    B = [0] * 5001
    for _ in range(N):
        a, b = map(int, input().split())
        A[a] += 1
        B[b] += 1
    for i in range(5000):
        A[i+1] += A[i]
        B[i+1] += B[i]

    P = int(input())
    for _ in range(P):
        j = int(input())
        print(A[j] - B[j-1], end=' ')
    print()




