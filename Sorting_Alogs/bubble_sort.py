def bubble_sort(A):
    n=len(A)
    for i in range(n): #start with 7 n=7
        for j in range(1,n-i): #start with 1 and goes to n-1(n=7,(7=1))
            if A[j] < A[j-1]:# a[7]=6,a[6]=7
                A[j],A[j-1]=A[j-1],A[j] #a[7],a[6]=a[6],a[7] swap each other
    return A # return Array

A=[5,2,1,4,3,6,7]
print(bubble_sort(A))
