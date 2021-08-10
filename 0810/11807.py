import sys
sys.stdin = open('11807_input.txt')
T = int(input())
for tc in range(1, T+1):
    print('#{}'.format(tc), end=' ')
    # K는 간격 N은 정류장 M은 충전기
    K, N, M = map(int,input().split())
    stop = list(map(int, input().split()))
    result = 0
        # for i in range(len(stop)-1):
        #     if stop[i+1] - stop[i] > 3:
        #         break
    for i in range(len(stop)):
        for j in range(K, 0, -1):
            if stop[i]+j in stop:
                result += 1
                print(stop[i])
                N -= K
                break
        if N <= 0:
            break


