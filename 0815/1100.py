arr =[input() for _ in range(8)]
cnt = 0
for i in range(len(arr)):
    for j in range(len(arr[i])):
        if j%2 == 0 and i%2 == 0 and arr[i][j] == 'F' or j%2 and i%2 and arr[i][j] == 'F':
            cnt += 1
print(cnt)
    