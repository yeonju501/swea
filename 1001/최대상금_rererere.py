import sys
sys.stdin = open('최대상금_input.txt')

def change(n, k):
    global result
    if k == cnt:
        result = max(result, int(''.join(num)))
        return

    for i in range(len(num) - 1):
        for j in range(i + 1, len(num)):
            num[i], num[j] = num[j], num[i]
            if not ''.join(num) in num_list[k]:
                num_list[k].append(''.join(num))
                change(n, k+1)
            num[i], num[j] = num[j], num[i]

T = int(input())
for tc in range(1, T+1):
    num, cnt = input().split()
    cnt = int(cnt)
    num = list(num)
    num_list = [[] for _ in range(cnt)]
    result = 0
    change(len(num), 0)
    print(num_list)
    print('#{} {}'.format(tc, result))



