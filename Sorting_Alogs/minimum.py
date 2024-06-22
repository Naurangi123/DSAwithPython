def min(arr):
    lowest=arr[0]
    n=len(arr)
    for i in range(2,n):
        if(arr[i]<lowest):
            lowest=arr[i]
    return lowest

arr=[7,9,8,4,6]

print(min(arr))