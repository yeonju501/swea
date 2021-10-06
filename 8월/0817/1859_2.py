import sys
sys.stdin = open('1859_input.txt')

def get_hap(idx, array, M):
    num_hap = 0
    for i in range(idx-1, -1, -1):
        num_hap += M - array[i]
    return num_hap


T = int(input())
for tc in range(1, T+1):
    N = input()
    arr = list(map(int, input().split()))
    hap = 0
    while True:
        m = max(arr)
        maxIdx = arr.index(m)
        hap += get_hap(maxIdx, arr, m)
        if maxIdx == len(arr)-1:
            break
        arr = arr[maxIdx+1:]
    print(f'#{tc} {hap}')
