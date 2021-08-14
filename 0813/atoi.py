def atoi(s):
    value = 0
    for i in range(len(s)):
        c = s[i]
        if c >= '0' and c <= '9':
            digit = ord(c) - ord('0')
            # 16진수 중 A ~ F
            #digit = ord(c) - ord('A') + 10
        else:
            break
        value = (value * 10) + digit
    return value

def atoi2(arr):
    value = 0
    for i in range(len(arr)):
        value = (value * 10) + arr[i]
    return value

a = '123'
print(a, type(a))
a1 = atoi(a)
print(a1, type(a1))

arr = [1, 2, 3]
int2 = atoi2(arr)
print(int2, type(int2))
