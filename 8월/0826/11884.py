import sys
sys.stdin = open('11884_input.txt')

T = int(input())
for tc in range(1, T+1):
    print('#{}'.format(tc), end=' ')
    N, M = map(int, input().split())
    q = list(input().split())
    for i in range(M):
        a = q.pop(0)
        q.append(a)
    print(q[0])
