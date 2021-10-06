def fibo(n):
    # memo를 위한 배열을 할당하고, 0,1을 초기화
    if n >= 2 and len(memo) <= n:
        memo.append(fibo(n-1) + fibo(n-2))
    return memo[n]

memo = [0, 1]
print(fibo(100))