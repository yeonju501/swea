import sys
sys.stdin = open('11822_input.txt')
T = int(input())
for tc in range(1, T+1):
    print('#{}'.format(tc), end=' ')
    A = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
    n = len(A)
    N, K = map(int, input().split())
    cnt = 0
    for i in range(1 << 12):
        sum = 0
        arr = []
        for j in range(13):
            if i & (1 << j):
                arr.append(A[j])
                sum += A[j]
        if sum == K and len(arr) == N:
            cnt += 1
    print(cnt)