# import sys
# sys.stdin = open('1860_input.txt')

def check():
    s = cnt = b = 0
    while True:
        s += M
        cnt += K
        for i in range(b, b+K):
            if i == N:
                return 'Possible'
            if arr[i] >= s:
                cnt -= 1
            else:
                return 'Impossible'
        else:
            b += K

T = int(input())
for tc in range(1, T+1):
    print('#{}'.format(tc), end=' ')
    N, M, K = map(int, input().split()) # N명이 M초의 시간을 들이면 K개의 붕어빵
    arr = list(map(int, input().split()))
    arr.sort()
    print(check())


