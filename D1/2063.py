N = int(input())
strArr = input().strip(' ').split(' ')
arr = []
for i in strArr:
    arr.append(int(i))
minIdx = 0
for idx in range(len(arr)):
    minIdx = idx
    for i in range(idx + 1, len(arr)):
        if arr[idx] > arr[i]:
            minIdx = i
            arr[idx], arr[minIdx] = arr[minIdx], arr[idx]
print(arr[len(arr) // 2])

        

