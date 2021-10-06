import sys
sys.stdin = open('3142_input.txt')
def typing(a, b):
    i = j = cnt = 0
    while True:
        if j == len(b):
            cnt += 1
            j = 0
            i += len(b)
        if i > len(a)-len(b):
            break
        if a[i+j] == b[j]:
            j += 1
        elif a[i+j] != b[j]:
            j = 0
            i += 1
    return len(a) - cnt*(len(b)-1)

T = int(input())
for tc in range(1, T+1):
    arr = input().split()
    A = arr[0]
    B = arr[1]
    print('#{} {}'.format(tc, typing(A, B)))
