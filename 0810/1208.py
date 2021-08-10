import sys
sys.stdin = open('1208_input.txt')
for tc in range(1, 11):
    print('#{}'.format(tc), end=' ')
    N = int(input())
    arr = list(map(int, input().split()))
    for _ in range(N):
        max = 0
        min = 100
        M_Idx = m_Idx = 0
        for i in range(len(arr)):
            if arr[i] > max:
                max = arr[i]
                M_Idx = i
            if arr[i] < min:
                min = arr[i]
                m_Idx = i
        arr[M_Idx] -= 1
        arr[m_Idx] += 1
    max = 0
    min = 100
    for i in range(len(arr)):
        if arr[i] > max:
            max = arr[i]
        if arr[i] < min:
            min = arr[i]
    print(max - min)






