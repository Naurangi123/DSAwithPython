# POWER SOLUTION

def power(base, exponent):
    if exponent == 0:
        return 1
    return base * power(base, exponent-1)
print(power(5,3))

# FACTORIAL SOLUTION

def factorial(num):
    if num <= 1:
        return 1
    return num * factorial(num-1)
print(factorial(10))


# PRODUCT OF ARRAY SOLUTION

def productOfArray(arr):
    if len(arr) == 0:
        return 1
    return arr[0] * productOfArray(arr[1:])
print(productOfArray([2,4,6,8,9]))
# RECURSIVE RANGE SOLUTION

def recursiveRange(num):
    if num <= 0:
        return 0
    return num + recursiveRange(num - 1)
print(recursiveRange(7))
# FIBONACCI SOLUTION
def fib(num):
    if (num < 2):
        return num
    return fib(num - 1) + fib(num - 2)
print(fib(10))
