import sys
sys.stdin = open('11825_input.txt')
T = int(input())
for tc in range(1, T+1):
    print('#{}'.format(tc), end=' ')
    N = int(input())
    arr = list(map(int, input().split()))
    for i in range(len(arr)-1):
        Idx = i
        for j in range(i+1, len(arr)):
            if i%2:
                if arr[Idx] > arr[j]:
                    Idx = j
            else:
                if arr[Idx] < arr[j]:
                    Idx = j
        arr[i], arr[Idx] = arr[Idx], arr[i]
    for i in range(10):
        print(arr[i], end=' ')
    print()



