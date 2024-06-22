
def merge_sort(A, p, q, r):
    n1 = q - p + 1
    n2 = r - q

    L = [0] * (n1 + 1)
    R = [0] * (n2 + 1)

    for i in range(n1):
        L[i] = A[p + i]

    for j in range(n2):
        R[j] = A[q + j]

    L[n1] = float('inf')  # Using infinity as sentinel value
    R[n2] = float('inf')  # Using infinity as sentinel value
    i = j = 0

    for k in range(p, r + 1):
        if L[i] <= R[j]:
            A[k] = L[i]
            i += 1
        else:
            A[k] = R[j]
            j += 1
    return A

A = [15,10,5,20,25,30,40,35]

print(merge_sort(A,1,4,8))
