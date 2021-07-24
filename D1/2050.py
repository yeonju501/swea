a = input()
num = ''
for idx in range(len(a)):
    if a[idx].isupper():
        num += f'{ord(a[idx]) - 64} '
print(num.strip())