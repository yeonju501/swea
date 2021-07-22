# 평균값 구하기
# T번 만큼 리스트에 입력 받기
T = int(input())
numsStr = []
for i in range(T):
    numsStr.append((input().strip(' ')).split(' '))
for i in range(len(numsStr)):
    hap = 0
    for numStr in numsStr[i]:
        hap += int(numStr)
    avgF = hap / len(numsStr[i])
    print(f'#{i + 1} {round(avgF)}')
# 입력 받은 값 리스트에 담아서 int로 만들기
# int로 만든 수 더해서 10으로 나누기
# 반올림하기

