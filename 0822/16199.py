Y, M, D = map(int, input().split())
A, B, C = map(int, input().split())
ans = 0
if M - B > 0:
    ans = A - Y - 1
elif M - B == 0:
    if D - C > 0:
        ans = A - Y - 1
    else:
        ans = A - Y
else:
    ans = A - Y


print(ans)
print(A-Y+1)
print(A-Y)