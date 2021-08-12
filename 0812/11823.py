import sys
sys.stdin = open('11823_input.txt')

def search(N, P):
    start = 1
    end = P
    cnt = 0
    while start <= end:
        cnt += 1
        c = int((start + end) / 2)
        if c == N:
            return cnt
        elif c > N:
            end = c - 1
        else:
            start = c + 1
    return cnt

T = int(input())

for tc in range(1, T+1):
    print('#{}'.format(tc), end=' ')
    P, A, B = map(int, input().split())
    cntA = search(A, P)
    cntB = search(B, P)
    if cntA < cntB:
        print('A')
    elif cntB < cntA:
        print('B')
    else:
        print('0')




