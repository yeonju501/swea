def fact(n):
    # 기본 파트
    if n == 1:
        return 1
    # 유도 파트
    else:
        return n * fact(n-1)

print(fact(4))