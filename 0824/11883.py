import sys
sys.stdin = open('11883_input.txt')

def powerset(n, k):
    if n == k:
        for i in range(N):
            for j in range(N):
                if bit[i]:
                    print(arr[i][j], end=' ')
                    break
    else:

T = int(input())
for tc in range(1, T+1):
    print('#{}'.format(tc), end= ' ')
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    bit = [0] * N
    powerset(N, 0)
