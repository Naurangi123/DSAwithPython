def heapify(arr, n, i):
    largest = i
    left = 2 * i + 1
    right = 2 * i + 2

    if left < n and arr[left] > arr[largest]:
        largest = left

    if right < n and arr[right] > arr[largest]:
        largest = right

    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr, n, largest)

def heap_sort(arr):
    n = len(arr)

    # Build a maxheap.
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)

    # One by one extract elements
    for i in range(n - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]  # swap
        heapify(arr, i, 0)
    return arr

# delete a node(heap)
def heap_delete(arr, n, i):
    arr[i] = n
    n -= 1
    heapify(arr, n, i)  # Adjust the heap after deleting an element


# Max Heap find
def max_heap(arr,n):
    if(n<1):
        return 'heap underflow'
    max=arr[0]
    arr[0]=arr[n-1]
    n-=1
    heapify(arr,n,0)
    return max

arr = [23, 17, 14, 6, 13, 10, 1, 5, 7, 12]
print(heap_sort(arr))
n = len(arr)

print("Original array:", arr)

# Delete element at index 2
i = 2
heap_delete(arr, n, i)
n -= 1  # Decrease the size of the heap
print("Array after deleting element at index", i, ":", arr)

# Perform heap sort
sorted_array = heap_sort(arr)
print("Array after heap sort:", sorted_array)


Max_heap=max_heap(arr,n)
print("Max heap is :",Max_heap)
