import sys
sys.stdin = open('11822_input.txt')

arr = list(range(1, 13))
SIZE = len(arr)

T = int(input())
for tc in range(1, T+1):
    N, K = map(int, input().split())
    ans = 0
    for i in range(1 << SIZE):
        sum = 0
        cnt = 0
        for j in range(SIZE):
            if i & (1 << j):
                sum += arr[j]
                cnt += 1
        if cnt == N and sum == K:
            ans += 1
    print('#{} {}'.format(tc, ans))
