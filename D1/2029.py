T = int(input())
ts = []
for i in range(T):
    ts.append(input())
for i in range(len(ts)):
    arr = ts[i].split(' ')
    val = int(arr[0]) // int(arr[1])
    remainder = int(arr[0]) % int(arr[1])
    print(f'#{i + 1} {val} {remainder}')

