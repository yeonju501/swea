def countnum(rst):
    cnt = 0
    while rst != ['6', '1', '7', '4']:
        rst.sort(reverse=True)
        M = int(''.join(rst))
        rst.sort()
        m = int(''.join(rst))
        cnt += 1
        result = str(M-m)
        rst.clear()
        for i in result:
            rst.append(str(i))
    return cnt

T = int(input())
ans = []
for i in range(T):
    cnt = 0
    rst = 0
    Nstr = input()
    rst = []
    for i in Nstr:
        rst.append(i)
    ans.append(countnum(rst))

for i in ans:
    print(i)

