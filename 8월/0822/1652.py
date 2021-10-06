N = int(input())
arr = [input() for _ in range(N)]
cnt = cnt2 = 0
ans = ans2 = 0
for i in range(N):
    cnt = 0
    for j in range(N):
        if arr[i][j] == '.':
            cnt += 1
            if j == N-1 and cnt >= 2:
                ans += 1
                cnt = 0
        elif arr[i][j] == 'X' and cnt >= 2:
            ans += 1
            cnt = 0
        elif arr[i][j] == 'X' and cnt < 2:
            cnt = 0

for i in range(N):
    cnt2 = 0
    for j in range(N):
        if arr[j][i] == '.':
            cnt2 += 1
            if j == N-1 and cnt2 >= 2:
                ans2 += 1
                cnt2 = 0
        elif arr[j][i] == 'X' and cnt2 >= 2:
            ans2 += 1
            cnt2 = 0
        elif arr[j][i] == 'X' and cnt2 < 2:
            cnt2 = 0

print(ans, ans2)


