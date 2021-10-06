s = input().split()
stack = []
for i in range(len(s)):
    if s[i] >= '0' and s[i] <= '9':
        print(s[i], end=' ')
    else:
        stack.append(s[i])

for i in range(len(stack)):
    print(stack.pop(), end=' ')