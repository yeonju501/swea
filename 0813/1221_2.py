def count_num(a, num):
    cnt = [0] * 10
    for i in range(0, N * 4, 4):
        if arr[i] == 'Z':
            cnt[0] += 1
        elif arr[i] == 'O':
            cnt[1] += 1
        elif arr[i] == 'T':
            if arr[i + 1] == 'W':
                cnt[2] += 1
            else:
                cnt[3] += 1
        elif arr[i] == 'F':
            if arr[i + 1] == 'O':
                cnt[4] += 1
            else:
                cnt[5] += 1
        elif arr[i] == 'S':
            if arr[i + 1] == 'I':
                cnt[6] += 1
            else:
                cnt[7] += 1
        elif arr[i] == 'E':
            cnt[8] += 1
        else:
            cnt[9] += 1
    return cnt


import sys
sys.stdin = open('1221_input.txt')

T = int(input())
for tc in range(1, T+1):
    print('#{}'.format(tc))
    info = input().split()
    N = int(info[1])
    arr = input()
    cnt1 = count_num(arr, N)
    result = 'ZRO ' * cnt1[0] + 'ONE ' * cnt1[1] + 'TWO ' * cnt1[2] + 'THR ' * cnt1[3] + 'FOR ' * cnt1[4] +\
        'FIV ' * cnt1[5] + 'SIX ' * cnt1[6] + 'SVN ' * cnt1[7] + 'EGT ' * cnt1[8] + 'NIN ' * cnt1[9]
    print(result)



