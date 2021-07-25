T = int(input())
date = []
for i in range(T): 
    date.append(input())
for i in range(len(date)):
    y = int(date[i][:4])
    m = int(date[i][4:6])
    d = int(date[i][6:8])
    if 0 < m <= 12: 
        if m in [1, 3, 5, 7, 10, 12] and 1 <= d <= 31:
            print(f'#{i + 1} {y:04d}/{m:02d}/{d:02d}')
        elif m in [4, 6, 9, 11] and 1 <= d <= 30:
            print(f'#{i + 1} {y:04d}/{m:02d}/{d:02d}')
        elif m == 2 and 1 <= d <= 28:
            print(f'#{i + 1} {y:04d}/{m:02d}/{d:02d}')
        else:
            print(f'#{i + 1} -1')
    else:
        print(f'#{i + 1} -1')

