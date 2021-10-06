ans = list(map(int, input().split()))
result = 0
score = [100, 100, 200, 200, 300, 300, 400, 400, 500]
for i in range(len(ans)):
    if ans[i] > score[i]:
        result -= 10000
        break
    result += ans[i]
    
if result < 0:
    print('hacker')
elif result >= 100:
    print('draw')
else:
    print('none')


        
