T = int(input())
arr = []
for i in range(T):
    arr.append(input().strip().split(' '))
print(arr)
for idx in range(len(arr)):
    max = 0
    for num in arr[idx]:
        if max < int(num):
            max = int(num)
    print(f'#{idx + 1} {max}')
    