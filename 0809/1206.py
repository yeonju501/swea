import sys
sys.stdin = open('1206_input.txt')
for tc in range(1, 11):
    T = int(input())
    arr = list(map(int, input().split()))
    floor = 0
    for i in range(2, len(arr)-2):
        view = arr[i]
        for j in range(i-2, i+3):
            if i == j:
                continue
            elif arr[i] > arr[j]:
                gap = arr[i] - arr[j]
                if gap < view:
                    view = gap
            else:
                break
        else:
            floor += view
    print('#{} {}'.format(tc, floor))