
def partition(arr,p,r):
    x=arr[r]
    i=p-1
    for j in range(p,r-1):
        if(arr[j]<=x):
            i+=1
            arr[i],arr[j]=arr[j],arr[i]
    arr[i+1],arr[i]=arr[i+1],arr[i]
    return i+1

def quick_sort(arr,p,r):
    if(p<r):
        q=partition(arr,p,r)
        quick_sort(arr,p,q-1)
        quick_sort(arr,q+1,r)
    return arr


arr=[36,15,40,1,6,60,20,55,25,50,20]
p=0
r=len(arr)-1
sorted_arr = quick_sort(arr, p, r)
print("Sorted Array :",sorted_arr)