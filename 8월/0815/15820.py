# 샘플 테스트 케이스 개수 시스템 테스트 케이스 개수
# 샘플 테스트케이스 정답
# 시스템...
t = s = 0
smp, sst = map(int, input().split())
for i in range(smp):
    ans, rst = map(int, input().split())
    if ans == rst:
        t += 1

for i in range(sst):
    ans, rst = map(int, input().split())
    if ans == rst:
        s += 1

if t == smp and s == sst:
    print('Accepted')
elif t != smp:
    print('Wrong Answer')
else:
    print('Why Wrong!!!')






     
