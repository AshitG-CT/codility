def solution(A, K):
    n = len(A)  # n = 5, K = 3
    print('n **', n)
    print('k **', K)

    for i in range(n - 1):
        print('A[i] + 1 **', A[i] + 1)
        print('A[i + 1] **', A[i + 1])
        if (A[i] + 1 < A[i + 1]):
            return False
    print('A[0] **', A[0])
    print('A[n - 1] **', A[n - 1])
    if (A[0] != 1 and A[n - 1] != K):
        return False
    else:
        return True
A = [1, 1, 2, 3, 3]
print(solution(A, 3))