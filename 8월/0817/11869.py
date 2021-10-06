import sys
sys.stdin = open('11869_input.txt')

def compare(n, m):
    j = 0
    for i in range(len(m)):
        if m[i] != n[j]:
            j = 0
            continue
        elif j == len(n)-1:
            return 1
        else:
            j += 1
    return 0

T = int(input())
for tc in range(1, T+1):
    N = input()
    M = input()
    print('#{} {}'.format(tc, compare(N, M)))