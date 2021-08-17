import sys
sys.stdin = open('3142_input.txt')
T = int(input())
for tc in range(1, T+1):
    print('#{}'.format(tc), end=' ')
    A, B = input().split()
    cnt = 0
    i = 0
    j = 0
    while True:
        if j == len(B):
            j = 0
            i += len(B)
            cnt += 1
        if len(A) - len(B) < i:
            break
        if A[i+j] != B[j]:
            i += 1
            j = 0
        elif A[i+j] == B[j]:
            j += 1
    print(len(A)-(cnt*(len(B)-1)))
