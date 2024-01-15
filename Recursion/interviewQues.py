#Sum of digit

def sumOfDigit(n):
    if n==0:
        return 0
    else:
        return int(n%10)+sumOfDigit(int(n/10))

print(sumOfDigit(-15))

#Power of a number

def power(base,exponent):
    if exponent==0:
        return 1
    return base*power(base,exponent-1)
print(power(3,5))

#Decimal to Binary number

def decToBinary(n):
    if n==0:
        return 1
    else:
        return n%2+10*decToBinary(int(n/2))
n=int(input("Enter number to convert"))
print(decToBinary(n))
