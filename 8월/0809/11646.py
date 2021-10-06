import sys
sys.stdin = open('11646_input.txt')
T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = list(map(int, input().split()))
    max = 0
    nakka = 0
    for i in range(len(arr)):
        great = 0
        for j in range(i, len(arr)):
            if arr[i] <= arr[j]:
                great += 1
        nakka = len(arr)-i-great
        if nakka > max:
            max = nakka
    print('#{} {}'.format(tc,max))

