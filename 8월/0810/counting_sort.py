def counting_sort(A, B, k):
    # A : 원본
    # B : 결과
    # C : 카운트 배열
    C = [0] * k
    # 1. 카운팅
    for i in range(len(A)):
        C[A[i]] += 1
    # 2. 누적
    for i in range(1, len(C)):
        C[i] += C[i-1]
    # 3. 결과 배열에 해당 위치에 넣기
    for i in range(len(A)-1, -1, -1):
        B[C[A[i]] - 1] = A[i]
        C[A[i]] -= 1

a = [0, 4, 1, 3, 1, 2, 4, 1]    # 원본
b = [0] * len(a)                # 결과
counting_sort(a, b, 5)
print(a)
print(b)

