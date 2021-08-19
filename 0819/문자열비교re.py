import sys
sys.stdin = open('11869_input.txt')

def brute_force(p, t):
    N = len(t)
    M = len(p)
    for i in range(N-M+1):
        for j in range(M):
            flag = 1 # flag 사용하기
            if t[i+j] != p[j]:
                flag = 0
                break
        if flag:
            return 1
    return 0

T = int(input())
for tc in range(1, T+1):
    pattern = input()
    text = input()
    print('#{} {}'.format(tc, brute_force(pattern, text)))