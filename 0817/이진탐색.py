def binary_search(a, key ,page):
    start = 1
    end = page
    cnt = 0
    while start <= end:
        middle = (start + end) // 2
        cnt += 1
        if key == a[middle]:
            return cnt
        elif key < a[middle]:
            end = middle
        else: 
            start = middle
    return -1


arr = [0] + list(range(1, 1001))
T = int(input())
for tc in range(1, T+1):
    P, A, B = map(int, input().split())
    a = binary_search(arr, A, P)
    b = binary_search(arr, B, P)

    ans = '0'
    if a > b: ans = 'B'
    elif a < b : ans = 'A'
    else: ans = '0'

    print('#{} {}'.format(tc, ans))