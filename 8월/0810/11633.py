import sys
sys.stdin = open('11633_input.txt')
T = int(input())
for tc in range(1, T+1):
    print('#{}'.format(tc), end=' ')
    N, M = map(int, input().split())
    arr = list(map(int, input().split()))
    if M%2:
        m = M//2
        max = 0
        min = 90000000000000
        for i in range(m, len(arr)-m):
            sum = 0
            for j in range(i-m, i+m+1):
                sum += arr[j]
            if sum > max:
                max = sum
            if sum < min:
                min = sum
        print(max - min)
    else:
        m = M // 2
        max = 0
        min = 90000000000000
        for i in range(m, len(arr) - m + 1):
            sum = 0
            for j in range(i - m, i + m):
                sum += arr[j]
            if sum > max:
                max = sum
            if sum < min:
                min = sum
        print(max - min)
