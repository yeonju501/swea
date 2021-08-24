import sys
sys.stdin = open('11874_input.txt')

def f(k):
    if k <= 1:
        return 1
    else:
        return f(k-1) + 2 * f(k-2)

memo = [1, 1]
for i in range(2, 31):
    memo.append((memo[i-1] + 2 * memo[i-2]))
T = int(input())
for tc in range(1, T+1):
    N = int(input())
    print('#{} {}'.format(tc, f(N//10)))
    print('#{} {}'.format(tc, memo[N//10]))