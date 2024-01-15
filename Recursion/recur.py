def recursiveMethod(n):
    if n<1:
        print("n less than 1")
    else:
        recursiveMethod(n-1)
        print(n)
recursiveMethod(5)

#Using Itretive method
def itrativeMethod(n):
    i=0
    power=1
    while i<n:
        power=power*2
        i=i+1
    return power
itrativeMethod(10)

 # SumOfArray
def productOfArray(arr):
    if len(arr) == 0:
        return 1
    return arr[0] * productOfArray(arr[1:])

print(productOfArray([1,2,3]))
print(productOfArray([1,2,3,10]))

def firstMethod():
    secondMethod()
    print("I am the first method")

def secondMethod():
    thirdMethod()
    print("I am the second method")

def thirdMethod():
    fourthMethod()
    print("I am the third method")

def fourthMethod():
    print("I am the fourth method")

firstMethod()
secondMethod()
thirdMethod()
firstMethod()