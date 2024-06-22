#eq=a^2+b^2=c^2

def pythagorean(a,b):
    c=(a**2+b**2)**0.5
    return c

print("Without round",pythagorean(5,4))
print("With round",round(pythagorean(5,4)))