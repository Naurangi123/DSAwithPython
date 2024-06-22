def merge(A, beg, mid, end):
    n1 = mid - beg + 1
    n2 = end - mid

    LeftArray = [0] * n1
    RightArray = [0] * n2

    # Copy data to temp arrays
    for i in range(n1):
        LeftArray[i] = A[beg + i]
    for j in range(n2):
        RightArray[j] = A[mid + 1 + j]

    i = j = 0
    k = beg

    while i < n1 and j < n2:
        if LeftArray[i] <= RightArray[j]:
            A[k] = LeftArray[i]
            i += 1
        else:
            A[k] = RightArray[j]
            j += 1
        k += 1

    while i < n1:
        A[k] = LeftArray[i]
        i += 1
        k += 1

    while j < n2:
        A[k] = RightArray[j]
        j += 1
        k += 1

A = [12, 31, 25, 8, 32, 17, 40, 42]
merge(A, 0, 3, 7)
print(A)