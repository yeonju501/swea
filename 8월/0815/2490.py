arr = [input() for _ in range(3)]

for i in range(len(arr)):
    cnt = 0
    for j in range(len(arr[i])):
        if arr[i][j] == '1':
            cnt += 1
    if cnt == 0:
        print('D')
    elif cnt == 3:
        print('A')
    elif cnt == 2:
        print('B')
    elif cnt == 1:
        print('C')
    else:
        print('E')
