def selection_sort(A):
    n=len(A)
    for j in range(n-1):
        smallest=j
        for i in range(j+1,n):
            if A[i]<A[smallest]:
                smallest=i
            A[j],A[smallest]=A[smallest],A[j]
    return A

A=[2,4,5,7,5,3,9,8]
print(selection_sort(A))