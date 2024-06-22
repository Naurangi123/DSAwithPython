
import math

def binomial(x,y,n):
    sum=0
    for k in range(n+1):
        sum+=math.comb(n,k)*(x**k)* (y**(n - k))
    return sum

print(binomial(2,3,4))
