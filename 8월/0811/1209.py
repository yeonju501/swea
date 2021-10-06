import sys
sys.stdin = open('1209_input.txt')
for i in range(1, 11):
    T = int(input())
    print('#{}'.format(T), end=' ')
    arr = [list(map(int, input().split())) for _ in range(100)]
    max = sum = sum2 = max2 = 0
    for i in range(len(arr)):
        sum = sum2 =0
        for j in range(len(arr[i])):
            sum += arr[i][j]
            sum2 += arr[j][i]
            if max < sum or sum2 > max:
                if sum < sum2:
                    max = sum2
                else:
                    max = sum

    for i in range(len(arr)):
        sum = sum2 = 0
        for j in range(len(arr[i])):
            if i == j:
                sum += arr[i][j]
            elif i + j == 100:
                sum2 += arr[i][j]
        if max2 < sum or max2 < sum2:
            if sum < sum2:
                max2 = sum2
            else:
                max2 =sum
    if max > max2:
        print(max)
    else:
        print(max2)


