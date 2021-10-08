import sys
sys.stdin = open('1970_input.txt')

for tc in range(1, int(input())+1):
    money = int(input())
    cur = [0] * 8
    arr = [50000, 10000, 5000, 1000, 500, 100, 50, 10]
    for i in range(8):
        if money >= arr[i]:
            cur[i] += money//arr[i]
            money %= arr[i]
    print(f'#{tc}')
    print(*cur)