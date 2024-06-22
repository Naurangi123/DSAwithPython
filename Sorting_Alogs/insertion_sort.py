def insertion_sort(A):
    n=len(A) # length of Array

    for j in range(2,n): #loop for start 2 and goes lenth of Array(A)
        key=A[j] #take a value a[j] that means A[2] because loop start with 2
        A[j]=A[j-1]# insert A[2] value into A[1]
        i=j-1 # set i for j-1 that means 2-1=1
        while(i>0 and A[i]>key): # apply while loop to check a=condition is true or not 
            A[i+1]=A[i]
            i-=1
        A[i+1]=key
    return A

A=[2,4,5,7,5,3,9,8]
print(insertion_sort(A))
