import sys
sys.stdin = open('1859_input.txt')


def max_idx(array):
    m_idx = 0
    for i in range(len(array)):
        if array[i] > array[m_idx]:
            m_idx = i
    return m_idx


T = int(input())
for tc in range(1, T+1):
    N = input()
    arr = list(map(int, input().split()))
    hap = margin = 0
    while len(arr) > 1:
        hap = 0
        maxIdx = max_idx(arr)
        for i in range(maxIdx):
            hap += arr[i]
        margin += (arr[maxIdx] * maxIdx) - hap
        arr = arr[maxIdx+1:]
    print(f'#{tc} {margin}')




