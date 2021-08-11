import sys
sys.stdin = open('11807_input.txt')
T = int(input())
for tc in range(1, T+1):
    print('#{}'.format(tc), end=' ')
    # K는 간격 N은 정류장 M은 충전기
    K, N, M = map(int,input().split())
    road = [0]*(N+K)
    stop = list(map(int, input().split()))
    result = 0
    spot = 0
    for i in range(len(stop)):
        road[stop[i]] += 1
    while 0 <= spot <= N+K:
        for i in range(K, 0, -1):
            if road[spot+i] == 1 and N-spot > K:
                result += 1
                spot += i
                break
        else:
            break

    for i in range(len(stop)-1):
        if stop[i+1] - stop[i] > K:
            result = 0
            break
    print(result)

