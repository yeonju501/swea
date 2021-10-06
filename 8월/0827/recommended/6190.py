import sys
sys.stdin = open('6190_input.txt')

T = int(input())
for tc in range(1, T+1):
    print('#{}'.format(tc), end=' ')
    N = int(input())
    arr = list(map(int, input().split()))
    rst = []
    for i in range(N):
        for j in range(i+1, N):
                a = arr[i] * arr[j]
                ans = str(a)
                for k in range(len(ans)-1):
                    if ans[k] > ans[k+1]:
                        break
                else:
                    rst.append(int(ans))
    if rst:
        print(max(rst))
    else:
        print(-1)

