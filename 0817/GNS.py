import sys
sys.stdin = open('1221_input.txt')

digit = ['ZRO', 'ONE', 'TWO', 'THR', 'FOR', 'FIV', 'SIX', 'SVN', 'EGT', 'NIN']
T = int(input())
for tc in range(1, T+1):
    temp = input()
    arr = list(map(str, input().split()))
    count = [0] * (10)
    for i in range(len(arr)):
        if arr[i] == digit[0]:
            count[0] += 1
        elif arr[i] == digit[1]:
            count[1] += 1
        elif arr[i] == digit[2]:
            count[2] += 1
        elif arr[i] == digit[3]:
            count[3] += 1
        elif arr[i] == digit[4]:
            count[4] += 1
        elif arr[i] == digit[5]:
            count[5] += 1
        elif arr[i] == digit[6]:
            count[6] += 1
        elif arr[i] == digit[7]:
            count[7] += 1
        elif arr[i] == digit[8]:
            count[8] += 1
        elif arr[i] == digit[9]:
            count[9] += 1

    print('#{}'.format(tc))
    for i in range(10):
        for j in range(count[i]):
            print(digit[i], end=' ')
    print()
