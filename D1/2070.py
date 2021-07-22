# 테스트 케이스 3개
# 부등호 출력
T = int(input())
numsStrArr = []
for i in range(T):
    numsStrArr.append(input().strip().split(' '))

for idx in range(len(numsStrArr)):
    if numsStrArr[idx][0] > numsStrArr[idx][1]:
        print(f'#{idx + 1} >')
    elif numsStrArr[idx][0] < numsStrArr[idx][1]:
        print(f'#{idx + 1} <')
    else:
        print(f'#{idx + 1} =')
    

