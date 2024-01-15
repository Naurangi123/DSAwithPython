def sum_even_num(arr):

    sum = 0
    for i in range(len(arr)):
        if i % 2 == 0:
            sum = sum+i
            i = i+1
    print("sum of even number is :", sum)


arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

sum_even_num(arr)
