N, M = map(int, input().split())
arr = list(map(int, input().split()))
max = 0
for i in range(1 << len(arr)):
    sum = 0
    arr2 = []
    for j in range(len(arr)+1):
        if i & (1 << j):
            arr2.append(arr[j])
            sum += arr[j]
    if sum <= M and len(arr2) == 3 and sum > max:
        max = sum
print(max)

for i in range(len(arr)-1):
    maxIdx = 0
    max = 0
    for j in range(i, len(arr)):
        if arr[j] > arr[i]:
            maxIdx = j
            arr[i], arr[maxIdx] = arr[maxIdx], arr[i]

max = 0
for i in range(0, len(arr)-2, 3):
    hap = 0
    for j in range(3):
        hap += arr[i+j]
        if hap <= M and max < hap:
            max = hap
print(max)





