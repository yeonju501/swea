import sys
sys.stdin = open('11807_input.txt')
T = int(input())
for tc in range(1, T+1):
    print('#{}'.format(tc), end=' ')
    # K는 간격 N은 정류장 M은 충전기
    K, N, M = map(int,input().split())
    stop = list(map(int, input().split()))
    result = 0
    while True:
        for i in range(len(stop)-1):
            if stop[i+1] > stop[i]
