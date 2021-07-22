T = int(input())
arrStr = []
for i in range(T):
    arrStr.append((input().strip(' ')).split(' '))

for idx in range(len(arrStr)):
    hap = 0
    for num in arrStr[idx]:
        if int(num) % 2 :
            hap += int(num)
    print(f'#{idx + 1} {hap}')

    