import sys
sys.stdin = open('1486_input.txt')

def powerset(n, k, hap):
    global ans
    if hap-B >= ans:
        return
    if n == k:
        if 0 <= hap-B < ans:
            ans = hap-B
        return
    else:
        used[k] = 1
        powerset(n, k+1, hap+S[k])
        used[k] = 0
        powerset(n, k+1, hap)

for tc in range(1, int(input())+1):
    N, B = map(int, input().split())
    S = list(map(int, input().split()))
    used = [0] * N
    ans = 987654321
    powerset(N, 0, 0)
    print('#{} {}'.format(tc, ans))

