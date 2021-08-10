import sys
sys.stdin = open('11785_input.txt')
T = int(input())
for tc in range(1, T+1):
    print('#{}'.format(tc), end=' ')
    N = int(input())
    num = list(map(int, input().split()))
    max = num[0]
    min = num[0]
    for i in range(len(num)):
        if max < num[i]:
            max = num[i]
        if num[i] < min:
            min = num[i]
    print(max-min)


