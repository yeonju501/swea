# 샘플 테스트 케이스 개수 시스템 테스트 케이스 개수
# 샘플 테스트케이스 정답
# 시스템...
t = s = 0
smp, sst = map(int, input().split())
for i in range(smp+sst):
    ans, rst = map(int, input().split())
    if i < smp and ans != rst:
        t += 1
    elif i >= sst and ans != rst:
        s += 1
if t:
    print('Wrong Answer')
elif s:
    print('Why Wrong!!!')
else:
    print('Accepted')
    





     
