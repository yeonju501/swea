import sys
sys.stdin = open('11770_input.txt')


def partition(A,l,r):
    p = A[l]
    i, j = l, r
    while i <= j:
        while i <= j and A[i] <= p:
            i += 1
        while i <= j and A[j] >= p:
            j -= 1
        if i < j:
            A[i], A[j] = A[j], A[i]
    A[l], A[j] = A[j], A[l]
    return j

def quick_sort(A, l, r):
    if l< r:
        s = partition(A, l, r)
        quick_sort(A, l, s-1)
        quick_sort(A, s+1, r)


for tc in range(1, int(input())+1):
    N = int(input())
    arr = list(map(int, input().split()))

    quick_sort(arr, 0, N-1)
    print('#{} {}'.format(tc, arr[N//2]))