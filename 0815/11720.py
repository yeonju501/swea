T = int(input())
hap = 0
num = input()
while num != '':
    hap += int(num[-1])
    num = num[:-1]
print(hap)