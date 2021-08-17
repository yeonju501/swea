import sys
sys.stdin = open('3142_input.txt')

T = int(input())
for tc in range(1, T+1):
    arr = input().split()
    A = arr[0]
    B = arr[1]
    cnt = 0
    start = 0
    end = len(A) - len(B)

    while start <= end:
        if A[start:start + len(B)] == B:
            cnt += 1
            start += len(B)
        else:
            start += 1
    ans = len(A) - (cnt * (len(B)-1))
    print('#{} {}'.format(tc, ans))