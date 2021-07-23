n = int(input())
hap = 0
while n > 0:
    hap += n % 10
    n = n // 10
print(hap)
