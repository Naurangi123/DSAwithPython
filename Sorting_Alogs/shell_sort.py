def shell_sort(A):
    n=len(A)
    inc=round(n/2)
    while(inc>0):
        i=inc
        for i in range(n-1):
            temp=A[i]
            j=i
            while(j>=inc and A[j-inc]>temp):
                A[j]=A[j-inc]
                j=j-inc
            A[j]=temp
    inc=round(inc/2)

A=[1,2,4,3,5,7,6,8,9]
print(shell_sort(A))